# PinguiLed
Interfacing  for controlling led lights with penguin board

# Instructions
Pinguino example to control the activation and deactivation of three pins of the penguin borad 18f4550, through an interface developed in python with the tkinter library, by means of serial communication using the pynguino communication library CDC_8bit.pde to be seen in Pinguiled.py

Ejemplo de Pinguino para controlar la activación y desactivación de tres pines de la pingüino borad 18f4550, a través de una interfaz desarrollada en python con la biblioteca tkinter, mediante comunicación serial usando la biblioteca de comunicación pynguino CDC_8bit.pde para ser visto en Pinguiled.py

1) Clone the repository

2) Install libraries 
   a) pip install pynguino.
   b) pip install pyserial.

3) Load the .pde in the Pinguino pic, CDC_8bit.pde from Yeison Cardona, https://bitbucket.org/yeisoneng/pynguino-2.0/raw/tip/pinguino/CDC/cdc_8bit.pde.

4) Connect led diodes on pin 5, 6 and 7.

5) Pinguino board pic18f4550 connected via usb to pc.

# How to Start the Example?
1) Pinguino board pic18f4550 connected via usb to pc.
2) Open the terminal.
3) Placed in the folder where your Pinguiled.py file is located. execute $ cd /home/usuario/folder where is your file.
4) As administrator execute # python Pinguiled.py and will open the sale with the graphical interfacing.
5) Activate the buttons and you can turn on the LEDs connected to the penguin board.

