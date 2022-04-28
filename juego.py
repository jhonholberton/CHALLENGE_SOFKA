#!/usr/bin/python3
"""inicio del juego"""
from tkinter import BOTH, LEFT, YES, Button, Frame, Label, Tk, messagebox
import sqlite3
import random


class juego():
    """clase que contiene todos los metodos para iniciar el programa"""

    niveles = 0
    def __init__(self, alias):
        """contructror"""
        self.jugar = Tk()
        self.jugar.title("QUIEN QUIERE SER PROGRAMADOR?")
        self.jugar.resizable(0,0)
        self.jugar.geometry("900x700+500+200")
        self.alias = alias

    def contenedor(self):
        """contenedores y metodos para dibujar la ventana del juego"""
        self.micontenedor = Frame(self.jugar)
        self.micontenedor.pack(expand=YES, fill=BOTH)
        self.contenedor_preguntas = Frame(self.micontenedor)
        self.contenedor_preguntas.config(height="200")
        self.contenedor_preguntas.pack_propagate(False)
        self.contenedor_preguntas.pack(fill="x")
        self.etiqueta1 = Label(
            self.contenedor_preguntas, text="Pregunta", font=("Arial", 18))
        self.etiqueta1.pack(fill="y")
        self.etiqueta2 = Label(
            self.contenedor_preguntas, text="Ronda", font=("Arial", 18))
        self.etiqueta2.pack(fill="y")
        self.contenedor_respuestas = Frame(self.micontenedor)
        self.contenedor_respuestas.config(height="750")
        self.contenedor_respuestas.pack(fill="x")
        self.contenedor_respuestas.pack_propagate(False)
        self.boton1 = Button(self.contenedor_respuestas, text="respuesta1", bd="20", width="49", height="9", justify=LEFT, wraplength=400)
        self.boton1.grid(row=0, column=0)
        self.boton2 = Button(self.contenedor_respuestas, text="respuesta2", bd="20", width="49", height="9", justify=LEFT, wraplength=400)
        self.boton2.grid(row=0, column=1)
        self.boton3 = Button(self.contenedor_respuestas, text="respuesta3", bd="20", width="49", height="9", justify=LEFT, wraplength=400)
        self.boton3.grid(row=1, column=0)
        self.boton4 = Button(self.contenedor_respuestas, text="respuesta4", bd="20", width="49", height="9", justify=LEFT, wraplength=400)
        self.boton4.grid(row=1, column=1)
        self.boton5 = Button(self.contenedor_respuestas, text="Rendirse", bd="24", width="105", height="4", justify=LEFT, wraplength=400)
        self.boton5.grid(row=2, column=0, columnspan=3)
        self.correr_juego()
        self.jugar.mainloop()

    def correr_juego(self):
        """metodo para establecer niveles de cada ronda del juego y preguntas"""
        if self.niveles < 5:
            self.niveles+=1
            dificultad = ""
            if self.niveles == 1:
                dificultad = "muyfacil"
            elif self.niveles == 2:
                dificultad = "facil"
            elif self.niveles == 3:
                dificultad = "basico"
            elif self.niveles == 4:
                dificultad = "intermedio"
            else:
                dificultad = "dificil"
            conexion = sqlite3.connect("Mi_Base.db")
            c = conexion.cursor()
            c.execute("SELECT * FROM Preguntas WHERE dificultad=?", (dificultad,))
            listaPreguntas = []
            listaRespuestasCorrectas = []
            listaRespuestasErradas1 = []
            listaRespuestasErradas2 = []
            listaRespuestasErradas3 = []

            for i in c:
                listaPreguntas.append(i[1])
                listaRespuestasCorrectas.append(i[2])
                listaRespuestasErradas1.append(i[3])
                listaRespuestasErradas2.append(i[4])
                listaRespuestasErradas3.append(i[5])
            c.close()
            index = random.randrange(0, 5)
            consulta = [
                listaPreguntas[index],
                listaRespuestasCorrectas[index],
                listaRespuestasErradas1[index],
                listaRespuestasErradas2[index],
                listaRespuestasErradas3[index],
            ]
            numero = random.randrange(0, 4)
            self.etiqueta1.config(text=consulta[0])
            self.etiqueta2.config(text=f'Ronda: {self.niveles}')
            respuestas = [
                consulta[1],
                consulta[2],
                consulta[3],
                consulta[4],
            ]
            random.shuffle(respuestas)
            self.boton1.config(text=respuestas[0])
            self.boton1.config(
                command=lambda: self.validar_respuesta(respuestas[0], consulta[1])
            )
            self.boton2.config(text=respuestas[1])
            self.boton2.config(
                command=lambda: self.validar_respuesta(respuestas[1], consulta[1])
            )
            self.boton3.config(text=respuestas[2])
            self.boton3.config(
                command=lambda: self.validar_respuesta(respuestas[2], consulta[1])
            )
            self.boton4.config(text=respuestas[3])
            self.boton4.config(
                command=lambda: self.validar_respuesta(respuestas[3], consulta[1])
            )
            self.boton5.config(
                command=lambda: self.me_rindo(False)
            )
        else:
            self.me_rindo(True)

    def validar_respuesta(self, validar1, validar2):
        """metodo para validar las respuestas"""
        if validar1 == validar2:
            self.correr_juego()
        else:
            respuesta = messagebox.askyesno("Aviso", "Perdiste!!!\nQuieres intentarlo de nuevo? ", parent=self.jugar)
            if respuesta == True:
                self.jugar.destroy()
                reiniciar = juego(self.alias)
                reiniciar.contenedor()
            else:
                self.jugar.destroy()

    def me_rindo(self, gano):
        """metodo para validar si se gana o pierde"""
        premio = 0
        nivel = self.niveles -1 if gano == False else self.niveles
        for i in range(0, nivel):
            premio += 200
        conexion = sqlite3.connect("Mi_Base.db")
        c = conexion.cursor()
        sentencia = "UPDATE Usuarios SET puntaje=? WHERE alias=?"
        datos = (premio, self.alias)
        c.execute(sentencia, datos)
        conexion.commit()
        c.close()
        respuesta = messagebox.askyesno("Aviso", "Ganaste, felicidades!!!\ntus puntos fueron " + str(premio) + "\nDesea jugar de nuevo?", parent=self.jugar)
        if respuesta == True:
            self.jugar.destroy()
            reiniciar = juego(self.alias)
            reiniciar.contenedor()
        else:
            self.jugar.destroy()
