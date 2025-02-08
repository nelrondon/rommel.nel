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
from rannum import NumberRandom, DIFFICULTYS

volverAJugar = True
option = list(DIFFICULTYS.keys())
print("\nBIENVENIDO AL JUEGO DE ADIVINA EL NUMERO.")

while volverAJugar:
    dificultad = ""
    while dificultad not in option:
        dificultad = input('INGRESA DIFICULTAD: ')

    print(f"OPCION SELECCIONADA => {dificultad} \n")

    guess = NumberRandom(dificultad)
    game = True
    while game:
        try:
            number = int(input(f'INTRODUCE UN NUMERO {guess.rango}: '))
            game = guess.compare(number)
        except ValueError:
            pass

    volverAJugar = input("DESEA VOLVER A JUGAR?: (s/n)") == "s"
    print()







