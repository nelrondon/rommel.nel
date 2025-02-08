import random

DIFFICULTYS = {
    "easy": [0, 30],
    "middle": [0, 50],
    "hard": [0, 80],
    "hardcore": [0, 100],
    "vezoenelano": [0, 200],
    "corinamachado": [0, 1000],
}

class NumberRandom:
    def __init__(self, diff):
        self.dificultad = diff
        self.numberToGuess = random.randint(DIFFICULTYS[diff][0], DIFFICULTYS[diff][1])
        self.turn = 0
        self.rango = DIFFICULTYS[diff].copy()

    def compare(self, number):
        self.turn += 1

        if number > self.numberToGuess:
            if number < self.rango[1]: self.rango[1] = number
            print(">> Prueba un número menor.")
        elif number < self.numberToGuess:
            if number > self.rango[0]: self.rango[0] = number
            print(">> Prueba un número mayor.")
        elif number == self.numberToGuess:
            print(f"Ganaste, con {self.turn} turnos")

        if self.dificultad in ["hardcore", "vezoenelano"]:
            if self.turn > 8:
                print("Perdiste prro, te excediste de turnos.")
                return False
            
        return number != self.numberToGuess
    
    def showNumber(self):
        print(self.numberToGuess)