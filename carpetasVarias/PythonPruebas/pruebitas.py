import tkinter as tk

def insertar_numero(numero):
    """Inserta el número en el cuadro de entrada."""
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(numero))

def sumar():
    """Realiza la suma y muestra el resultado."""
    global operacion
    global primer_numero
    primer_numero = float(entrada.get())
    operacion = '+'
    entrada.delete(0, tk.END)

def calcular():
    """Calcula el resultado según la operación definida."""
    segundo_numero = float(entrada.get())
    if operacion == '+':
        resultado = primer_numero + segundo_numero
    entrada.delete(0, tk.END)
    entrada.insert(0, str(resultado))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Cuadro de entrada
entrada = tk.Entry(ventana, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entrada.grid(row=0, column=0, columnspan=4)

# Botones numéricos
boton0 = tk.Button(ventana, text="0", command=lambda: insertar_numero(0))
boton1 = tk.Button(ventana, text="1", command=lambda: insertar_numero(1))
boton2 = tk.Button(ventana, text="2", command=lambda: insertar_numero(2))
boton3 = tk.Button(ventana, text="3", command=lambda: insertar_numero(3))
boton4 = tk.Button(ventana, text="4", command=lambda: insertar_numero(4))
boton5 = tk.Button(ventana, text="5", command=lambda: insertar_numero(5))
boton6 = tk.Button(ventana, text="6", command=lambda: insertar_numero(6))
boton7 = tk.Button(ventana, text="7", command=lambda: insertar_numero(7))
boton8 = tk.Button(ventana, text="8", command=lambda: insertar_numero(8))
boton9 = tk.Button(ventana, text="9", command=lambda: insertar_numero(9))

# Botones de operaciones
boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_calcular = tk.Button(ventana, text="=", command=calcular)

# Posicionamiento de los botones en la cuadrícula
boton0.grid(row=4, column=1)
boton1.grid(row=3, column=0)
boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)
boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)
boton7.grid(row=1, column=0)
boton8.grid(row=1, column=1)
boton9.grid(row=1, column=2)
boton_sumar.grid(row=4, column=0)
boton_calcular.grid(row=4, column=2)

# Variables globales
operacion = ""
primer_numero = 0

# Ejecutar la aplicación
ventana.mainloop()
