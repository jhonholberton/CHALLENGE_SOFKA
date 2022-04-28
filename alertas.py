#!/usr/bin/python3
"""envio de mensajes emergentes durante la ejecucion del juego"""
from tkinter import Frame, Label, Tk, BOTH, YES, mainloop


class alerta():
    """clase que contiene los contenedores y metodos para enviar alertas"""

    def __init__(self, mensaje):
        """constructor"""
        self.inicio = Tk()
        self.inicio.title("Aviso")
        self.mensaje = mensaje

    def contenedor(self):
        """contenedores y metodos para dibujar la ventana de alertas"""
        self.micontenedor = Frame(self.inicio)
        self.micontenedor.pack(expand=YES, fill=BOTH)
        self.etiqueta1 = Label(
            self.micontenedor, text=self.mensaje, font=("Arial", 28))
        self.etiqueta1.pack()
        self.inicio.mainloop()