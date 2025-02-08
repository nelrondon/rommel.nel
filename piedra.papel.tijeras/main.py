import tkinter as tk
import random

def setContador():
    if estadoJuego == None:
        return f"{puntos[0]} vs {puntos[1]}"
    else:
        return f"{estadoJuego}: {puntos[0]} vs {puntos[1]}"

def setOpcion(opcion):
    global estadoJuego
    opChosse = random.choice(opciones)
    resultLabel.config(text=(opChosse.capitalize()))

    if opcion == opChosse:
        estadoJuego = "Empate"
    elif (opcion == "piedra" and opChosse == "papel") or (opcion == "papel" and opChosse == "tijera") or (opcion == "tijera" and opChosse == "piedra"):
        estadoJuego = "Perdiste"
        puntos[0] += 1
    else:
        estadoJuego = "Ganaste"
        puntos[1] += 1

    contador.config(text=setContador())

#? Definiendo la ventana y algunas opciones
ventana = tk.Tk()
ventana.title("Ideas de ChatGPT #1")
ventana.option_add("*Font", ("Inter", 12))

#? Definiendo algunas variables
opciones = ["piedra", "papel", "tijera"]
puntos = [0, 0]
estadoJuego = None

#? Definiendo los widgets
title = tk.Label(ventana, text="Piedra, Papel o Tijeras", font=("Inter Bold", 16))
subtitle = tk.Label(ventana, text="La maquina escoge...")
resultLabel = tk.Label(ventana, text="...", font=("Inter Bold", 32))
contador = tk.Label(ventana, text=setContador())

instruccion = tk.Label(ventana, text="Selecciona opcion para jugar...")

piedra = tk.Button(ventana, text="Piedra", command= lambda : setOpcion("piedra"))
papel = tk.Button(ventana, text="Papel", command= lambda : setOpcion("papel"))
tijera = tk.Button(ventana, text="Tijera", command= lambda : setOpcion("tijera"))

#? Renderizando los widgets
title.grid(row=0, column=0, columnspan=3, padx=20, pady=(10, 0))
subtitle.grid(row=1, column=0, columnspan=3)
resultLabel.grid(row=2, column=0, columnspan=3)
contador.grid(row=3, column=0, columnspan=3)
instruccion.grid(row=4, column=0, columnspan=3)
piedra.grid(row=5, column=0, pady=20)
papel.grid(row=5, column=1, pady=20)
tijera.grid(row=5, column=2, pady=20)


ventana.resizable(False, False)
ventana.mainloop()