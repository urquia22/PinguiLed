#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""/*	---------------------------------------------------------------------
	Pinguino example to control the activation and deactivation of three 
	pins of the pinguino board 18f4550, through an interface developed in 
	python with the tkinter library, by means of serial communication 
	using the pynguino communication library CDC_8bit.pde to be seen in 
	PinguiLed.py
 
	Ejemplo de Pinguino para controlar la activación y desactivación de 
	tres pines de la tarjeta pingüino  18f4550, a través de una interfaz
	desarrollada en python con la biblioteca tkinter, mediante 
	comunicación serial usando la biblioteca de comunicación pynguino 
	CDC_8bit.pde para ser visto en PinguiLed.py
 
 
	author			Angel Urquia 
	email			urquia22@gmail.com
        date                    02/01/2018
	-----------------------------------------------------------------------
	will need
	-----------------------------------------------------------------------
	1)cdc_8bit.pde
	2)Pynguino
	3)Board Pinguno 18f4550
	4)Three led diodes
	----------------------------------------------------------------------*/"""
from pynguino import PynguinoCDC 
from Tkinter import *     			#Import libraries // Importamos Librerias 
pinguino = PynguinoCDC()			#This would be our pinguino board // Esta seria nuestra tarjeta pinguino 
 
pinguino.pinMode(5, "OUTPUT")                   #Pins as output // Pines como salida 
pinguino.pinMode(6, "OUTPUT")
pinguino.pinMode(7, "OUTPUT")
 
ven = Tk() 					#It is the main window // Tk() Es la ventana principal
ven.title('Por: Angel Urquia')
 
# Frame for the circles // Marco para los circulos
P = Frame(ven, width=500, height = 500)
P.grid(row=1, column=0, padx=0, pady=5)
 
#Canvas draw frame content for Led1 // Contenido del marco de dibujo de lienzo para Led1
marco = Canvas(P, width=50, height=50, bg='gray')
marco.grid(row=1, column=0, padx=0, pady=0)
 
#Canvas draw frame content for Led2 // Contenido del marco de dibujo de lienzo para Led2
marco2 = Canvas(P, width=50, height=50, bg='gray')
marco2.grid(row=1, column=1, padx=0, pady=0)
 
#Canvas draw frame content for Led3 // Contenido del marco de dibujo de lienzo para Led3
marco3 = Canvas(P, width=50, height=50, bg='gray')
marco3.grid(row=1, column=2, padx=0, pady=0)
 
#Frame for the background image // Marco para la imagen de fondo
tabla = Frame(ven, width=260, height = 200)
tabla.grid(row=0, column=0, padx=0, pady=0)
 
# background image // imagen fondo
img = PhotoImage(file="pinguino.gif") 
marco1 = Canvas(tabla, width=258, height=195, bg='blue')
marco1.grid(row=0, column=0, padx=5, pady=5)
 
# led 1 on
def led_on ():
	led = marco.create_oval(3, 3, 48, 48, width=4, fill="red",dash=(5,))
	pinguino.digitalWrite(6, "HIGH")
 
# led 1 off
def led_off ():
	led = marco.create_oval(3, 3, 48, 48, width=4, fill="white",dash=(5,))
	pinguino.digitalWrite(6, "LOW")
 
# led 2 on
def led_on2 ():
	led2 = marco2.create_oval(3, 3, 48, 48, width=4, fill="red",dash=(5,))
	pinguino.digitalWrite(7, "HIGH")
# led 2 off
def led_off2 ():
	led2 = marco2.create_oval(3, 3, 48, 48, width=4, fill="white",dash=(5,))
	pinguino.digitalWrite(7, "LOW")
 
# led 3 on
def led_on3 ():
	led3 = marco3.create_oval(3, 3, 48, 48, width=4, fill="red",dash=(5,))
	pinguino.digitalWrite(5, "HIGH")
# led 3 off
def led_off3 ():
	led3 = marco3.create_oval(3, 3, 48, 48, width=4, fill="white",dash=(5,))
	pinguino.digitalWrite(5, "LOW")
 
# Frame for text // Marco para texto 
P1 = Frame(ven, width=50, height = 100)
P1.grid(row=5, column=0, padx=0, pady=5)
texto = Label(P1, text="Interfaz de Control Pinguino")
texto.grid(row=5, column=0, padx=10, pady=2)
 
# Two actions the same button // Dos acciones el mismo boton
# Action button1 // Accion boton1
def toggle():
 
    if      boton1.config('text')[-1] == 'Encender':
            boton1.config(text='Apagar')
	    boton1.config(bg='red')
	    led_on ()
 
    else:
            boton1.config(text='Encender')
	    boton1.config(bg='green')
	    led_off()
 
# Action button2 // Accion boton2
def toggle2():
 
    if      boton2.config('text')[-1] == 'Encender':
            boton2.config(text='Apagar')
	    boton2.config(bg='red')
	    led_on2 ()
 
    else:
            boton2.config(text='Encender')
	    boton2.config(bg='green')
	    led_off2()
 
 
# Action button3 // Accion boton3
def toggle3():
 
    if      boton3.config('text')[-1] == 'Encender':
            boton3.config(text='Apagar')
	    boton3.config(bg='red')
	    led_on3 ()
 
    else:
            boton3.config(text='Encender')
	    boton3.config(bg='green')
	    led_off3()
 
# Main // Pincipal
marco1.create_image(130, 98, image=img)
led_off()
led_off2()
led_off3()
 
# create button1 // crear boton1
boton1 = Button(text="Encender", width=6, command=toggle,bg='green', fg='white', bd=10, font="times", activebackground='white', activeforeground='black')
boton1.grid(row=2, column=0, padx=0, pady=5)
 
# create button2 // crear boton2
boton2 = Button(text="Encender", width=6, command=toggle2,bg='green', fg='white', bd=10, font="times", activebackground='white', activeforeground='black')
boton2.grid(row=3, column=0, padx=0, pady=5)
 
# create button3 // crear boton3
boton3 = Button(text="Encender", width=6, command=toggle3,bg='green', fg='white', bd=10, font="times", activebackground='white', activeforeground='black')
boton3.grid(row=4, column=0, padx=0, pady=5)
 
ven.config(bg="blue") # background color // color de fondo
ven.mainloop()
