import tkinter as tk
from tkinter import *

ventana=tk.Tk()
ventana.geometry("800x400")
ventana.title("Anotador")
ventana.configure(bg="lightblue")


#texto=tk.Text(ventana,height=10,width=10).place(x=10,y=50)

#texto=tk.Text(ventana,height=10,width=10).place(x=10,y=50)

#def crear_cuadro():
#   cuadro_texto = tk.Text(ventana, height=5, width=10, font=12)
#    cuadro_texto.place(x=10, y=50)

posicion_y = 45
posicion_x = 10
limite_x = 700
def CuadroDinamico():
    global posicion_x
    global posicion_y
    texto=tk.Text(ventana,height=5,width=10,font=12)
    texto.place(x=posicion_x , y=posicion_y)
    posicion_x += 100

    if posicion_x >= limite_x:
        posicion_x = 10
        posicion_y = 150
        



altoBoton=1
anchoBoton=1
boton=tk.Button(ventana,text="+",height=altoBoton,width=anchoBoton,font=12, command=CuadroDinamico).place(x=10,y=10)









ventana.mainloop()
#crear una ventana para guardar cuadros de textos
#la ventana tendrá que aparecer vacía al principio
#arriba a la izquierda tendrá que tener un botón que
#una vez que lo apriete el mismo agregará un cuadro de texto arriba
#a la izquierda también y que podrá ser cerrado



#def on_button_click():
#    print("¡Botón presionado!")
#root = tk.Tk()
#button = tk.Button(root, text="Presionar", command=on_button_click)#