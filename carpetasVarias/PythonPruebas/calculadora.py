import tkinter as tk
from tkinter import *
from math import *

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("392x600")


cuadroDeCuentas = tk.Entry(ventana,width=58,bd=5,bg="white",insertwidth=1).place(x=11,y=10)

altoBoton=4
anchoBoton=12

Boton0=Button(ventana,text="0",height=altoBoton,width=anchoBoton).place(x=10,y=40)
Boton1=Button(ventana,text="1",height=altoBoton,width=anchoBoton,).place(x=100,y=40)
Boton2=Button(ventana,text="2",height=altoBoton,width=anchoBoton,).place(x=190,y=40)
Boton3=Button(ventana,text="3",height=altoBoton,width=anchoBoton,).place(x=280,y=40)

Boton3=Button(ventana,text="4",height=altoBoton,width=anchoBoton,).place(x=10,y=130)
Boton3=Button(ventana,text="5",height=altoBoton,width=anchoBoton,).place(x=100,y=130)
Boton3=Button(ventana,text="6",height=altoBoton,width=anchoBoton,).place(x=190,y=130)

ventana.mainloop()