import tkinter as tk
from tkinter import *
from math import *

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("392x350")

#Cuadro donde van las cuentas y resultados
cuadroDeCuentas = tk.Entry(ventana,width=58,bd=5,bg="white",insertwidth=1).place(x=11,y=10)



altoBoton=4
anchoBoton=12

#Fila 1
Boton1=Button(ventana,text="1",height=altoBoton,width=anchoBoton).place(x=10,y=40)
Boton2=Button(ventana,text="2",height=altoBoton,width=anchoBoton,).place(x=100,y=40)
Boton3=Button(ventana,text="3",height=altoBoton,width=anchoBoton,).place(x=190,y=40)
Botonmas=Button(ventana,text="+",height=altoBoton,width=anchoBoton,).place(x=280,y=40)

#Fila 2
Boton4=Button(ventana,text="4",height=altoBoton,width=anchoBoton,).place(x=10,y=115)
Boton5=Button(ventana,text="5",height=altoBoton,width=anchoBoton,).place(x=100,y=115)
Boton6=Button(ventana,text="6",height=altoBoton,width=anchoBoton,).place(x=190,y=115)
Botonmenos=Button(ventana,text="-",height=altoBoton,width=anchoBoton,).place(x=280,y=115)

#Fila 3
Boton7=Button(ventana,text="7",height=altoBoton,width=anchoBoton,).place(x=10,y=190)
Boton8=Button(ventana,text="8",height=altoBoton,width=anchoBoton,).place(x=100,y=190)
Boton9=Button(ventana,text="9",height=altoBoton,width=anchoBoton,).place(x=190,y=190)
Botonmulti=Button(ventana,text="*",height=altoBoton,width=anchoBoton,).place(x=280,y=190)

#Fila 4
Boton0=Button(ventana,text="0",height=altoBoton,width=anchoBoton,).place(x=10,y=265)
Botonce=Button(ventana,text="CE",height=altoBoton,width=anchoBoton,).place(x=100,y=265)
Botonigual=Button(ventana,text="=",height=altoBoton,width=anchoBoton,).place(x=190,y=265)
Botondivi=Button(ventana,text="/",height=altoBoton,width=anchoBoton,).place(x=280,y=265)




#botón tiene que poner su número cuando lo cliqueás
#se guarda en una variable, en el cuadro de entrada
#se pone el otro botón en otra variable en el mismo cuadro de entrada
#se hace la operación
#se muestra el resultado
#se borra a cero cuando se apreta "CE"












ventana.mainloop()