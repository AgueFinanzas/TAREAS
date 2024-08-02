import tkinter as tk
from tkinter import *

ventana=tk.Tk()
ventana.geometry("375x600")
ventana.title("Anotador")
ventana.configure(bg="lightblue")


texto=tk.Text(ventana,height=10,width=10).place(x=10,y=50)




altoBoton=1
anchoBoton=1

boton=tk.Button(ventana,text="+",height=altoBoton,width=anchoBoton,font=12).place(x=10,y=10)



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