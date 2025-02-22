import random

DIFFICULTYS = {
    "easy": [0, 30],
    "middle": [0, 50],
    "hard": [0, 80],
    "hardcore": [0, 100],
    "vezoenelano": [0, 200],
    "corinamachado": [0, 1000],
    "elianaisabel": [0, 50000],
}

class NumberRandom:
    def __init__(self, diff=None):
        self.dificultad = diff
        self.turn = 0
        self.isGuess = False
        self.prev = 0
        if diff != None:
            self.numberToGuess = random.randint(DIFFICULTYS[diff][0], DIFFICULTYS[diff][1])
            self.rango = DIFFICULTYS[diff].copy()

    def compare(self, number):
        if self.prev == number:
            return None
        
        self.prev = number
        self.turn += 1

        if number > self.numberToGuess:
            if number < self.rango[1]: self.rango[1] = number
            return "Prueba un número menor."
        elif number < self.numberToGuess:
            if number > self.rango[0]: self.rango[0] = number
            return "Prueba un número mayor."
        elif number == self.numberToGuess:
            self.isGuess = True
            return f"Ganaste, con {self.turn} turnos"

        if self.dificultad in ["hardcore", "vezoenelano"]:
            if self.turn > 8:
                return "Perdiste prro, te excediste de turnos."
    
    def showNumber(self):
        print(self.numberToGuess)