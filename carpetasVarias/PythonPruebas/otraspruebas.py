import tkinter as tk
from tkinter import *

ventana=tk.Tk()
ventana.geometry("375x600")
ventana.title("Anotador")
ventana.configure(bg="lightblue")


texto=tk.Text(ventana,height=10,width=10).place(x=10,y=10)
texto=tk.Text(ventana,height=10,width=10).place(x=100,y=10)
texto=tk.Text(ventana,height=10,width=10).place(x=190,y=10)
texto=tk.Text(ventana,height=10,width=10).place(x=280,y=10)




ventana.mainloop()


#crear una ventana para guardar cuadros de textos
#la ventana tendrá que aparecer vacía al principio
#arriba a la izquierda tendrá que tener un botón que
#una vez que lo apriete el mismo agregará un cuadro de texto arriba
#a la izquierda también y que podrá ser cerrado


