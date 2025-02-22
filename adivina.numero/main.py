# QUE VAMOS A HACER????
# HACER UN PROGRAMA QUE ME AYUDE A ADIVINAR UN NUMERO AL AZAR 
# DEBE CONTAR CON DIFICULTADES, ESTAS ESTARAN DEFINIDAS POR EL RANGO DE BUSQUEDA DEL NUMERO
# EASY: 0 - 30
# MIDDLE: 0 - 60
# HARDC0RE: 0 - 100

#VARIABLES A USAR: 
# OPTION = Level Difficulty
# GUESS = Number to Guess
# NUMBER = Number to Introduce

import tkinter as tk
from rannum import NumberRandom, DIFFICULTYS

option = list(DIFFICULTYS.keys())
guessVar = NumberRandom()

def validarEntrada(txt, motivo, content):
    maxL = 5
    if len(content) > maxL:
        return False
    if motivo == "1":
        if not txt.isdigit():
            return False
    return True

def handleButton():
    global guessVar
    guessVar = NumberRandom(opcVar.get())
    frameJuego.grid(row=2, column=0, pady=(0,20))
    numVar.set(0)
    turns.config(text=f"Turnos: {guessVar.turn}")
    rango.config(text=f"Rango: {guessVar.rango}")
    numero.config(state="normal")
    labelHint.config(text="Presiona Enter para empezar!")

def handleEnter(event):
    global guessVar
    if not guessVar.isGuess:
        msg = guessVar.compare(numVar.get())
        if guessVar.isGuess: numero.config(state="disabled")
        turns.config(text=f"Turnos: {guessVar.turn}")
        rango.config(text=f"Rango: {guessVar.rango}")
        if msg != None:
            labelHint.config(text=msg)

ventana = tk.Tk()
ventana.title("Guess a Number - The Game...")
ventana.option_add("*Font", ("Inter", 10))

validacion = ventana.register(validarEntrada)

#? Titulo
label = tk.Label(ventana, text="Adivina el número...", font=("Inter Bold", 18))
label.grid(row=0, column=0, padx=30, pady=(10, 0))

#- Frame Config
frameConfig = tk.Frame(ventana)
frameConfig.grid(row=1, column=0, pady=(0, 10))

#? Label (Dificultad)
tk.Label(frameConfig, text="Dificultad:").grid(row=0, column=0)

#? Menu de Opciones
opcVar = tk.StringVar()
opcVar.set(option[0])
opciones = tk.OptionMenu(frameConfig, opcVar, *option)
opciones.grid(row=0, column=1)

#? Boton Empezar
boton = tk.Button(frameConfig, text="Jugar", command=handleButton)
boton.grid(row=0, column=2, padx=10)

#- Frame Juego
frameJuego = tk.Frame(ventana)

#? Label (Turnos)
turns = tk.Label(frameJuego)
turns.grid(row=0, column=0)

#? Label (Rango)
rango = tk.Label(frameJuego)
rango.grid(row=0, column=2)

tk.Label(frameJuego, text="Ingresa un número:", font=("Inter", 12)
        ).grid(row=1, column=0, columnspan=3)

#? Entrada (Numero)
numVar = tk.IntVar(ventana)
numero = tk.Entry(frameJuego, textvariable=numVar, width=5, font=("Inter Bold", 20), justify="center", validate="key", validatecommand=(validacion, "%S", "%d", "%P"))
numero.bind("<Return>", handleEnter)
numero.grid(row=2, column=0, columnspan=3)

#? Label (Pista)
labelHint = tk.Label(frameJuego, text="Presiona Enter para empezar", font=("Inter Bold", 12))
labelHint.grid(row=3, column=0, columnspan=3, pady=10)

ventana.resizable(False, False)
ventana.mainloop()