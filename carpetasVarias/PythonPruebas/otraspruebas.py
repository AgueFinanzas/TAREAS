import tkinter as tk
from tkinter import *
from tkinter import messagebox

ventana=tk.Tk()
ventana.geometry("720x400")
ventana.title("Anotador")
ventana.configure(bg="lightblue")


posicion_y = 45
posicion_x = 10
limite_x = 600
limite_y = 220

contador_filas = 0
maximo_filas = 3

def CuadroDinamico():
    global posicion_x
    global posicion_y
    global contador_filas

    if contador_filas >= maximo_filas:
        messagebox.showinfo ("Límite alcanzado","Cerrá algún Post-it para abrir otro")
        return
    
    # texto=tk.Text(ventana,height=5,width=10,font=12)
    # texto.place(x=posicion_x , y=posicion_y)
    # posicion_x += 100

    if posicion_x >= limite_x:
        posicion_x = 10
        posicion_y += 100
        contador_filas += 1
    
# Crear un frame para el cuadro de texto y el botón de cierre
    frame = tk.Frame(ventana)
    frame.place(x=posicion_x, y=posicion_y)
    posicion_x += 110
    # Crear un nuevo cuadro de texto
    texto = tk.Text(frame, height=5, width=10, font=10)
    texto.pack(side=tk.LEFT)
    # Crear el botón de cierre
    boton_cerrar = tk.Button(frame, text="X", command=frame.destroy, font=("Arial", 6),width=1,height=1)
    boton_cerrar.pack(side=tk.RIGHT)

altoBoton=1
anchoBoton=1
boton=tk.Button(ventana,text="+",height=altoBoton,width=anchoBoton,font=12, command=CuadroDinamico).place(x=10,y=10)


ventana.mainloop()




 # Crear un frame para el cuadro de texto y el botón de cierre
  #  frame = tk.Frame(ventana)
  #  frame.place(x=posicion_x, y=posicion_y)

    # Crear un nuevo cuadro de texto
   # texto = tk.Text(frame, height=5, width=30, font=12)
   # texto.pack(side=tk.LEFT)

    # Crear el botón de cierre
   # boton_cerrar = tk.Button(frame, text="X", command=frame.destroy, font=("Arial", 8))
    #boton_cerrar.pack(side=tk.RIGHT)












#crear una ventana para guardar cuadros de textos
#la ventana tendrá que aparecer vacía al principio
#arriba a la izquierda tendrá que tener un botón que
#una vez que lo apriete el mismo agregará un cuadro de texto arriba
#a la izquierda también y que podrá ser cerrado






#def on_button_click():
#    print("¡Botón presionado!")
#root = tk.Tk()
#button = tk.Button(root, text="Presionar", command=on_button_click)#










#texto=tk.Text(ventana,height=10,width=10).place(x=10,y=50)

#texto=tk.Text(ventana,height=10,width=10).place(x=10,y=50)

#def crear_cuadro():
#   cuadro_texto = tk.Text(ventana, height=5, width=10, font=12)
#    cuadro_texto.place(x=10, y=50)






   # elif posicion_x == limite_x and posicion_y == 45:
     #   posicion_x=10
     #   posicion_y=300
