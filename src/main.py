import gc
from time import sleep_ms, time
from Models.Api import Api
from Models.Api import get_binance_price
from Models.RpiPico import RpiPico
from Models.Max7219 import Max7219
from Models.Rotary_irq_rp2 import RotaryIRQ

# Importo variables de entorno
import env

# Habilito recolector de basura
gc.enable()

DEBUG = env.DEBUG

# Tiempo entre actualizaciones del valor de la moneda
time_to_read_currency = 300

# Rpi Pico Model Instance
rpi = RpiPico(ssid=env.AP_NAME, password=env.AP_PASS, debug=DEBUG, alternatives_ap=env.ALTERNATIVES_AP, hostname=env.HOSTNAME)

rpi.led_on()

# Preparo la instancia para la comunicación con la API
#api = Api(controller=rpi, url=env.API_URL, path=env.API_PATH, token=env.API_TOKEN, device_id=env.DEVICE_ID, debug=env.DEBUG)

sleep_ms(100)

# Inicializo Pantalla
spi = rpi.set_spi(10, 11, None, 9, bus=1, baudrate=1000000)
display = Max7219(spi, 9)

# Inicializa el display
display.reset()  # Resetear la pantalla
display.set_intensity(1)
display.write_to_buffer_with_dots("Inicio..")
display.display()
need_api_update = True

# Pausa preventiva al desarrollar (ajustar, pero si usas dos hilos puede ahorrar tiempo por bloqueos de hardware ante errores)
sleep_ms(3000)

# Diccionario de monedas
currency_map = { "ADA": "ada", "BTC": "btc", "ETH": "eth", "BNB": "bnb",
                 "SOL": "sol", "DOT": "dot", }

# Inicialización del encoder
r = RotaryIRQ(pin_num_dt=15,
              pin_num_clk=14,
              min_val=0,
              max_val=len(currency_map) - 1,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_BOUNDED)

in_selection = False
val_old = r.value()  # Valor inicial del encoder

# Moneda seleccionada inicialmente
selected_currency = "ADA"


# Función que maneja la pulsación del botón del encoder
def encoder_press (pin):
    global in_selection, val_old, selected_currency, need_api_update
    print('Se ha pulsado el encoder')

    # Si no estamos en selección, entramos al menú
    if not in_selection:
        in_selection = True
        print("Entrando al menú de selección de moneda...")
        display.write_to_buffer(f"SEL-{selected_currency}")
        display.display()
    else:
        # Si estamos en selección, salimos del menú
        in_selection = False
        print("Saliendo del menú...")
        display.write_to_buffer(f"CURR-{selected_currency}")
        display.display()
        need_api_update = True

    # Esperamos a que se suelte el botón para evitar múltiples presiones
    while pin.value() == 0:
        sleep_ms(50)


# Función para actualizar la moneda seleccionada en el menú
def update_currency_selection ():
    global val_old, selected_currency
    val_new = r.value()

    # Solo actualizamos si el valor del encoder ha cambiado
    if val_new != val_old:
        val_old = val_new

        # Verificamos que el valor del encoder está dentro del rango válido de índices
        if 0 <= val_new < len(currency_map):
            # Usamos el valor del encoder para seleccionar la moneda correspondiente
            selected_currency = list(currency_map.keys())[val_new]
            print(f"Moneda seleccionada: {selected_currency}")
            display.write_to_buffer(f"SEL- {selected_currency}")
            display.display()
        else:
            print("Valor de encoder fuera de rango: ", val_new)

    sleep_ms(50)


# Callback para la interrupción del botón del encoder (para manejar las pulsaciones)
SW = rpi.set_callback_to_pin(13, encoder_press)


# Tiempo en el que se llamó a la función
last_called_time = time()

def thread0 ():
    """
    Primer hilo, flujo principal de la aplicación.
    En este hilo colocamos toda la lógica principal de funcionamiento.
    """

    global need_api_update, selected_currency, last_called_time

    if env.DEBUG:
        print('')
        print('Inicia hilo principal (thread0)')

    # Bucle principal que maneja la selección del encoder
    while True:
        if in_selection:
            # Si estamos en el menú, actualizamos la moneda seleccionada con el encoder
            update_currency_selection()
        else:
            if need_api_update or time() - last_called_time > time_to_read_currency:
                price = get_binance_price(selected_currency, 'EUR')
                need_api_update = False

                if price:
                    display.write_to_buffer_with_dots(f"{selected_currency}-{price:.2f}E")
                    display.display()

        sleep_ms(50)


while True:
    try:
        thread0()
    except Exception as e:
        if env.DEBUG:
            print('Error: ', e)

        if env.DEBUG:
            print('Memoria antes de liberar: ', gc.mem_free())

        gc.collect()

        if env.DEBUG:
            print("Memoria después de liberar:", gc.mem_free())
    finally:
        sleep_ms(5000)
