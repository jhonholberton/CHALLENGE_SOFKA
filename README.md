<img src="https://img.freepik.com/vector-gratis/juego-concurso-preguntas-jovenes-inteligentes-jugando-concurso-television-showman-trivia-concurso-television-juegos-diseno-dibujos-animados_176411-25.jpg" style="height:100%;width:100%" />

# CHALLENGE SOFKA - CONCURSO DE PREGUNTAS Y RESPUESTAS

## RESUMEN

En este reto vamos a modelar un concurso de preguntas y respuestas, la intención es diseñar una solución que permita tener un banco de preguntas con diferentes opciones para una única respuesta, además cada pregunta debe estar en una categoría o un grupos de preguntas similares del mismo nivel, por cada ronda se deberá asignar un premio a conseguir, las rondas del juego son nivel que van aumentando en la medida que el jugador gana premios.

Dentro del reto se debe considerar lo siguiente:

- Manejo de clases u objetos a nivel de modelamiento.
- Persistencia de datos o guardado de históricos.
- Manejos de listas o colecciones y ciclos de control adecuados
- Conocimiento de cualquier lenguaje de programación.
- Manejo de Git (versión de control).

## TEGNOLOGIAS UTILIZADAS

### - Python

Python es un lenguaje de programación de propósito general y alto nivel. Su filosofía de diseño enfatiza la legibilidad del código con el uso de sangría significativa. Sus construcciones de lenguaje y su enfoque orientado a objetos tienen como objetivo ayudar a los programadores a escribir código claro y lógico para proyectos de pequeña y gran escala.

### - SQLite

SQLite es una base de datos SQL autónoma basada en archivos. SQLite viene incluido con Python y se puede usar en cualquiera de sus aplicaciones de Python sin tener que instalar ningún software adicional.

Cuando nos conectamos a una base de datos SQLite, accedemos a datos que finalmente residen en un archivo en nuestra computadora. Las bases de datos SQLite son motores SQL con todas las funciones que se pueden usar para muchos propósitos.

### - Tkinter

Tkinter es la biblioteca GUI estándar para Python . Python, cuando se combina con Tkinter, proporciona una forma rápida y fácil de crear aplicaciones GUI. Tkinter proporciona una poderosa interfaz orientada a objetos para el kit de herramientas Tk GUI.

Para poder usar nuestro juego se debe instalar el modulo de Tkinter (instalacion en linux), a continuacuon le dejamos un enlace para que se guie en la instalacion del mismo:

https://julioecheverri.wordpress.com/2016/01/06/instalar-tkinter-en-linux/

una vez lo hayamos instalado y hayamos clonado el repositorio solo debemos ejecutar nuestro archivo ejecutar.py y dara inicio al juego.

#### Files
Files | Description |
-------- | ----------- |
**ejecutar.py** | aqui se encuentra el motor del funcionamieto del juego |
**juego.py**     | aqui se encuentra la estructura de la ejecucion de juego juego |
**preguntas.py**      | aqui se crea la tabla de preguntas apartir del archivo banco.json|
**Mi_Base.db**  | base de datos para el juego |
**banco.json**    | apartir de este archivo se crea la tabla de preguntas en la base de datos |
**alertas.py** | envio de mensajes emergentes durante la ejecucion del juego |




## Author

* **github** [jhonholberton](https://github.com/jhonholberton)
* **Linkedin:** https://www.linkedin.com/in/jhon-gonzalez-354487202