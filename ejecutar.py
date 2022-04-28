#!/usr/bin/python3
"""aqui se encuentra el motor del funcionamieto del juego"""
from tkinter import BOTH, CENTER, LEFT, YES, Button, Entry, Frame, Label, Tk
from datetime import datetime
import sqlite3
from juego import juego
from alertas import alerta


class inscripcion:
    """clase que contiene todos los metodos para ejecutar el programa"""

    resultado = False
    def __init__(self):
        """contructor"""
        self.inicio = Tk()
        self.inicio.title("QUIEN QUIERE SER PROGRAMADOR?")

    def contenedor(self):
        """contenedores y metodos para dibujar la ventana de registro"""
        self.micontenedor = Frame(self.inicio)
        self.micontenedor.pack(expand=YES, fill=BOTH)
        self.etiqueta1 = Label(
            self.micontenedor, text="Nombre completo", font=("Arial", 14)
        )
        self.etiqueta1.grid(row=0, column=0)
        self.texto1 = Entry(self.micontenedor, width=50, font=("Arial", 12))
        self.texto1.grid(row=0, column=1)
        self.etiqueta2 = Label(
            self.micontenedor, text="Fecha de nacimiento", font=("Arial", 14)
        )
        self.etiqueta2.grid(row=1, column=0)
        self.texto2 = Entry(
            self.micontenedor, width=50, font=("Arial", 12), justify=CENTER
        )
        self.texto2.grid(row=1, column=1)
        self.etiqueta3 = Label(self.micontenedor, text="Edad", font=("Arial", 14))
        self.etiqueta3.grid(row=2, column=0)
        self.texto3 = Entry(self.micontenedor, width=50, font=("Arial", 12))
        self.texto3.grid(row=2, column=1)
        self.etiqueta4 = Label(
            self.micontenedor, text="Correo electronico", font=("Arial", 14)
        )
        self.etiqueta4.grid(row=3, column=0)
        self.texto4 = Entry(self.micontenedor, width=50, font=("Arial", 12))
        self.texto4.grid(row=3, column=1)
        self.etiqueta5 = Label(self.micontenedor, text="Alias", font=("Arial", 14))
        self.etiqueta5.grid(row=4, column=0)
        self.texto5 = Entry(self.micontenedor, width=50, font=("Arial", 12))
        self.texto5.grid(row=4, column=1)
        self.etiqueta6 = Label(self.micontenedor, text="Contraseña", font=("Arial", 14))
        self.etiqueta6.grid(row=5, column=0)
        self.texto6 = Entry(self.micontenedor, width=50, font=("Arial", 12), show="*")
        self.texto6.grid(row=5, column=1)
        self.boton1 = Button(
            self.micontenedor,
            text="Registrarse",
            bd="5",
            command=lambda: self.Guardarbd(
                self.texto1.get(),
                self.texto2.get(),
                self.texto3.get(),
                self.texto4.get(),
                self.texto5.get(),
                self.texto6.get(),
            ),
        )
        self.boton1.grid(row=6, column=0, columnspan=2)
        self.texto2.insert(0, "DD-MM-AAAA")
        self.texto2.bind("<FocusIn>", lambda e: self.cambio_texto())
        self.texto2.bind("<FocusOut>", lambda e: self.cambio_texto1())

    def contenedor_inicio(self):
        """contenedores y metodos para dibujar la ventana de inicio de sesion"""
        self.micontenedor2 = Frame(self.inicio)
        self.micontenedor2.pack(expand=YES, fill=BOTH)
        self.etiqueta5 = Label(self.micontenedor2, text="Alias", font=("Arial", 14))
        self.etiqueta5.grid(row=0, column=0)
        self.texto5 = Entry(self.micontenedor2, width=50, font=("Arial", 12))
        self.texto5.grid(row=0, column=1)
        self.etiqueta6 = Label(
            self.micontenedor2, text="Contraseña", font=("Arial", 14)
        )
        self.etiqueta6.grid(row=2, column=0)
        self.texto6 = Entry(self.micontenedor2, width=50, font=("Arial", 12), show="*")
        self.texto6.grid(row=2, column=1)
        self.boton2 = Button(
            self.micontenedor2,
            text="Iniciar sesión",
            bd="5",
            command=lambda: self.validar_sesion(self.texto5.get(), self.texto6.get()),
        )
        self.boton2.grid(row=6, column=0, columnspan=2)
        self.boton3 = Button(
            self.micontenedor2,
            text="Registrarse",
            bd="5",
            command=lambda: self.cambio_ventana(),
        )
        self.boton3.grid(row=8, column=0, columnspan=2)
        self.inicio.mainloop()

    def validar_sesion(self, alias, contrasena):
        "metodo para validar campos de inicio de sesion"
        if alias == "":
            la_alerta = alerta("campo de alias es obligatorio")
            la_alerta.contenedor()
            return
        if contrasena == "":
            la_alerta = alerta("campo de contraseña es obligatorio")
            la_alerta.contenedor()
            return
        conexion = sqlite3.connect("Mi_Base.db")
        c = conexion.cursor()
        c.execute(
            "SELECT alias, contraseña FROM Usuarios WHERE alias = ? AND contraseña = ?",
            [alias, contrasena],
        )
        verificador = ""
        for i in c:
            verificador = i[0]
        if verificador == alias:
            c.close()
            empezar = juego(alias)
            self.inicio.destroy()
            empezar.contenedor()
        else:
            c.close()
            la_alerta = alerta("usuario o contraseña incorrecta, por favor verifique")
            la_alerta.contenedor()

    def cambio_ventana(self):
        """metodo para hacer sucesión de una ventana a otra"""
        self.micontenedor2.destroy()
        self.contenedor()

    def cambio_texto(self):
        if self.texto2.get() == "DD-MM-AAAA":
            self.texto2.delete(0, "end")

    def cambio_texto1(self):
        """metodo para verificar que el formato de la fecha de nacimiento"""
        if self.texto2.get() == "":
            self.texto2.insert(0, "DD-MM-AAAA")
            self.texto2.config(justify=CENTER)
        else:
            self.texto2.config(justify=LEFT)
            formato = self.texto2.get()
            validacion = "%d-%m-%Y"
            try:
                self.resultado = bool(datetime.strptime(formato, validacion))
            except ValueError:
                self.resultado = False

    def Guardarbd(self, nombre, fecha_nacimiento, edad, correo, alias, contrasena):
        """metodo para validar que cada uno de los campos en registro esten completos y cargar el resgistro a la base de datos"""
        self.cambio_texto1()
        if self.resultado == False:
            la_alerta = alerta("Error de formato en la fecha, debe ser DD-MM-AAAA")
            la_alerta.contenedor()
            return
        if nombre == "":
            la_alerta = alerta("campo de nombre es obligatorio")
            la_alerta.contenedor()
            return
        if alias == "":
            la_alerta = alerta("campo de alias es obligatorio")
            la_alerta.contenedor()
            return
        if correo == "":
            la_alerta = alerta("campo de correo es obligatorio")
            la_alerta.contenedor()
            return
        if edad == "":
            la_alerta = alerta("campo de edad es obligatorio")
            la_alerta.contenedor()
            return
        if contrasena == "":
            la_alerta = alerta("campo de contraseña es obligatorio")
            la_alerta.contenedor()
            return
        conexion = sqlite3.connect("Mi_Base.db")
        c = conexion.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS Usuarios (nombre VARCHAR(20), edad INT,\
            fecha_nacimiento VARCHAR(10),correo VARCHAR(30), alias VARCHAR(10) PRIMARY KEY, contraseña VARCHAR(10), puntaje INT DEFAULT 0)"
        )
        sql = "INSERT INTO Usuarios (nombre, fecha_nacimiento, edad, correo, alias, contraseña) VALUES (?, ?, ?, ?, ?, ?)"
        datos = (nombre, fecha_nacimiento, edad, correo, alias, contrasena)
        try:
            edad = int(edad)
            try:
                c.execute(sql, datos)
                conexion.commit()
                c.close()
            except sqlite3.IntegrityError:
                la_alerta = alerta("El alias ya existe")
                la_alerta.contenedor()
                c.close()
        except ValueError:
            la_alerta = alerta("La edad debe ser un numero")
            la_alerta.contenedor()
        if c:
            empezar = juego(alias)
            self.inicio.destroy()
            empezar.contenedor()


if __name__ == "__main__":
    ventana = inscripcion()
    ventana.contenedor_inicio()
