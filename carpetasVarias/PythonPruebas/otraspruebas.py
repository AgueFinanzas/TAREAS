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


