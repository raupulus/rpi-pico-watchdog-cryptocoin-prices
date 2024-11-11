# CryptoWatchDog - Raspberry Pi Pico W - Watchdog para Precios de Criptomonedas

Este proyecto en MicroPython permite monitorear los precios de criptomonedas y mostrarlos en una pantalla de 8 dígitos con 7 segmentos utilizando el chip MAX7219. El proyecto también incluye un codificador rotatorio (encoder) para permitir la navegación o ajuste de parámetros (como la criptomoneda a monitorizar).

Sitio web del autor: [https://raupulus.dev](https://raupulus.dev)

![Imagen del Proyecto](docs/images/img1.jpg "Imagen Principal de raspberry pi pico w")

Repository [https://gitlab.com/raupulus/rpi-pico-watchdog-cryptocoin-prices](https://gitlab.com/raupulus/rpi-pico-watchdog-cryptocoin-prices)

## Descripción

Este proyecto tiene como objetivo proporcionar una forma visual de monitorear los precios de criptomonedas en tiempo real, utilizando una Raspberry Pi Pico W con la capacidad de mostrar la información en una pantalla de 8 dígitos basada en el MAX7219. El código está desarrollado en MicroPython y se conecta a la red para obtener los precios actualizados de las criptomonedas, que luego se visualizan en la pantalla.

Además, el proyecto incluye un codificador rotatorio que permite la interacción con el sistema para cambiar el valor o configurar opciones, como la criptomoneda que se está monitoreando.

<p align="center">
  <img src="docs/images/2.jpg" alt="Raspberry pi pico w image 1" height="150">
  <img src="docs/images/3.jpg" alt="Raspberry pi pico w image 2" height="150">
  <img src="docs/images/4.jpg" alt="Raspberry pi pico w image 3" height="150">
  <img src="docs/images/scheme_thumbnail.jpg" alt="Raspberry pi pico w esquema de pines" height="150">
</p>

## Requisitos

- **Hardware:**
  - Raspberry Pi Pico W.
  - Pantalla de 8 dígitos de 7 segmentos (con chip MAX7219).
  - Codificador rotatorio (encoder).
  
- **Software:**
  - MicroPython (debe estar instalado en la Raspberry Pi Pico W).
  - Librerías para controlar el MAX7219 y el codificador rotatorio.

## Componentes y Pinout

### Pantalla 7 segmentos (MAX7219)

La pantalla de 8 dígitos de 7 segmentos se controla utilizando el chip MAX7219, que se conecta a la Raspberry Pi Pico W de la siguiente manera:

- **SCK (Serial Clock)**: Pin GPIO 10
- **DIN (Serial Data Input)**: Pin GPIO 11
- **CS (Chip Select)**: Pin GPIO 9

### Codificador Rotatorio (Encoder)

El codificador rotatorio está conectado a los siguientes pines de la Raspberry Pi Pico W:

- **DT (Data)**: Pin GPIO 15
- **CLK (Clock)**: Pin GPIO 14
- **SW (Switch)**: Pin GPIO 13

### Raspberry Pi Pico W

El pinout de la Raspberry Pi Pico W se puede consultar en la documentación oficial. A continuación, se presentan las conexiones clave utilizadas en este proyecto:

| **Pin**         | **Función**                     |
|-----------------|----------------------------------|
| GPIO 10         | SCK (para MAX7219)              |
| GPIO 11         | DIN (para MAX7219)              |
| GPIO 9          | CS (para MAX7219)               |
| GPIO 15         | DT (para el encoder rotatorio)  |
| GPIO 14         | CLK (para el encoder rotatorio) |
| GPIO 13         | SW (para el encoder rotatorio)  |

## Contenido del Repositorio

- **src/**: Código fuente del proyecto.
- **src/Models**: Modelos/Clases para separar entidades que intervienen.
- **docs/**: Documentación adicional, esquemas y guías de instalación.

## Instalación

### 1. Preparar el entorno

1. Asegúrate de tener **MicroPython** instalado en tu Raspberry Pi Pico W. Si no lo has hecho, puedes seguir las instrucciones de la documentación oficial de MicroPython para instalarlo.
   
2. Clona este repositorio en tu computadora:

   ```bash
   git clone https://github.com/raupulus/rpi-pico-watchdog-cryptocoin-prices.git
   ```

3. Copia el archivo *.env.example.py* a *env.py* y rellena los datos para 
     conectar al wireless.

4. Copia los archivos de código fuente a tu Raspberry Pi Pico W usando una 
   herramienta como **Thonny** o cualquier otro IDE compatible con MicroPython.

### 2. Conexión de los componentes

Conecta los componentes a tu Raspberry Pi Pico W siguiendo el **pinout** descrito anteriormente.

- Conecta el MAX7219 a los pines GPIO 9, 10 y 11 para manejar la pantalla de 8 dígitos.
- Conecta el codificador rotatorio a los pines GPIO 13, 14 y 15.

### 3. Ejecutar el código

Una vez que todo esté conectado, ejecuta el código en tu Raspberry Pi Pico W. Deberías ver los precios de las criptomonedas en la pantalla de 7 segmentos y poder interactuar con el codificador rotatorio para cambiar la criptomoneda monitoreada.

## Funcionamiento

El código obtiene los precios de las criptomonedas de una API y los muestra en la pantalla de 7 segmentos.

La pantalla mostrará la criptomoneda actualmente seleccionada, y el codificador rotatorio permite navegar entre las criptomonedas disponibles.

### Interacción con el codificador rotatorio:

- **Rotación**: Cambia entre las criptomonedas disponibles.
- **Presión del botón (SW)**: Selecciona la criptomoneda para mostrar su precio.

## Licencia

Este proyecto está licenciado bajo la Licencia **GPLv3**. Puedes ver los detalles completos de la licencia en el archivo [LICENSE](./LICENSE).
