#!/usr/bin/python3
"""colsulta de base y tablas de datos de las preguntas y demas parametros requeridos por medio de sqlite"""
import sqlite3
import json

conexion = sqlite3.connect("Mi_Base.db")
c = conexion.cursor()

c.execute(
    "CREATE TABLE IF NOT EXISTS Preguntas (id INTEGER PRIMARY KEY UNIQUE, pregunta VARCHAR(200), respuesta VARCHAR(200),\
    respuesta_incorrecta1 VARCHAR(200), respuesta_incorrecta2 VARCHAR(200), respuesta_incorrecta3 VARCHAR(200),\
        categoria VARCHAR(50), dificultad VARCHAR(20))"
)

with open("banco.json") as file:
    data = json.load(file)
    
    for key, value in data.items():
        sql = "INSERT INTO Preguntas (id, pregunta, respuesta, respuesta_incorrecta1,\
            respuesta_incorrecta2 ,respuesta_incorrecta3, categoria, dificultad)\
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        datos = (
            key,
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
            value[5],
            value[6]
        )
        c.execute(sql, datos)
conexion.commit()

c.close()
