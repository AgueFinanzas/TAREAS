import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Ejemplo de POO con Tkinter")
        self.geometry("400x300")
        
        # Crear un botón
        self.boton = tk.Button(self, text="Crear Cuadro de Texto", command=self.crear_cuadro_texto)
        self.boton.pack(pady=20)
        
        # Posiciones iniciales
        self.posicion_x = 10
        self.posicion_y = 50
        self.limite_x = 300
        self.espaciado_y = 60
        self.contador_filas = 0
        self.numero_filas_maximo = 6

    def crear_cuadro_texto(self):
        # Verificar si se ha alcanzado el límite de filas
        if self.contador_filas >= self.numero_filas_maximo:
            tk.messagebox.showinfo("Límite alcanzado", "Límite de filas alcanzado. No se pueden crear más cuadros de texto.")
            return

        # Crear un frame para el cuadro de texto y el botón de cierre
        frame = tk.Frame(self)
        frame.place(x=self.posicion_x, y=self.posicion_y)

        # Crear un cuadro de texto
        texto = tk.Text(frame, height=5, width=30, font=12)
        texto.pack(side=tk.LEFT)

        # Crear el botón de cierre
        boton_cerrar = tk.Button(frame, text="X", command=frame.destroy, font=("Arial", 8), width=2, height=1)
        boton_cerrar.pack(side=tk.RIGHT)

        # Actualizar la posición x
        self.posicion_x += 320

        # Verificar si se ha alcanzado el límite de x
        if self.posicion_x > self.limite_x:
            # Restablecer la posición x y mover a la siguiente fila
            self.posicion_x = 10
            self.posicion_y += self.espaciado_y
            self.contador_filas += 1

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
