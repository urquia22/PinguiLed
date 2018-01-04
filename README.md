# PinguiLed
Python interfacing for controlling led lights with pinguino board

# Instructions
Pinguino example to control the activation and deactivation of three pins of the pinguino board 18f4550, through an interface developed in python with the tkinter library, by means of serial communication using the pynguino communication library CDC_8bit.pde to be seen in PinguiLed.py

Ejemplo de Pinguino para controlar la activación y desactivación de tres pines de la pingüino board 18f4550, a través de una interfaz desarrollada en python con la biblioteca tkinter, mediante comunicación serial usando la biblioteca de comunicación pynguino CDC_8bit.pde para ser visto en PinguiLed.py
# Requirements
1) Clone the repository

2) Install libraries 
   a) pip install pynguino.
   b) pip install pyserial.

3) Load the .pde in the Pinguino pic, CDC_8bit.pde from Yeison Cardona, https://bitbucket.org/yeisoneng/pynguino-2.0/raw/tip/pinguino/CDC/cdc_8bit.pde.

4) Connect led diodes on pin 5, 6 and 7.

5) Pinguino board pic18f4550 connected via usb to pc.
# Requisitos 
1) Clonar el repositorio
2) Instalar librerias
a) pip install pynguino.
b) pip install pyserial.

3) Cargue el archivo .pd en la Tarjeta Pinguino , CDC_8bit.pde de Yeison Cardona, https://bitbucket.org/yeisoneng/pynguino-2.0/raw/tip/pinguino/CDC/cdc_8bit.pde.

4) Conecte los diodos LED en los pines 5, 6 y 7.

5) Tarjeta Pinguino pic18f4550 conectado a través de USB a la PC.

# How to Start the Example?
1) Pinguino board pic18f4550 connected via usb to pc.
2) Open the terminal.
3) Placed in the folder where your PinguiLed.py file is located. execute $ cd /home/usuario/folder where is your file.
4) As administrator execute # python PinguiLed.py and will open the window with the graphical interfacing.
5) Activate the buttons and you can turn on the LEDs connected to the pinguino board.
# Como iniciar el ejemplo?
1) Tablero Pinguino pic18f4550 conectado a través de USB a la PC.
2) Abra la terminal.
3) Colocado en la carpeta donde se encuentra el archivo PinguiLed.py. ejecuta $ cd / home / usuario / carpeta donde esta tu archivo.
4) Como administrador, ejecute # python PinguiLed.py y abrirá la ventana con la interfaz gráfica.
5) Active los botones y puede encender los LED conectados a la placa de pingüino.

