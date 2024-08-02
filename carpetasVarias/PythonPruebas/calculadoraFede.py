import tkinter as tk
from tkinter import *
from math import *

panelCalculadora=tk.Tk()
panelCalculadora.geometry("400x600")
panelCalculadora.title("Calculadora")
panelCalculadora.configure(bg="lightblue",)

visorCalculadora=Entry(panelCalculadora,bg="white",width=50,bd=2).place(x=10,y=10)

texto=tk.Text(panelCalculadora,height=10,width=10).place(x=10,y=50)
texto=tk.Text(panelCalculadora,height=10,width=10).place(x=100,y=50)

#etiqueta=tk.Label(panelCalculadora,text="HOLA")
#etiqueta.pack()



panelCalculadora.mainloop()
