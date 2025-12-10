#Genera un número aleatorio entre 1 y 50.
# El usuario debe adivinarlo; el programa dará pistas (“más alto”, “más bajo”).
# Finaliza cuando acierta.

import random

numero_secreto = random.randint(1,50)
intento = -1

print("Intenta adivinar el número que hay entre 1 y 50: ")

while intento != numero_secreto:
    try:
        intento = int(input("Introduce intento: "))
    except ValueError:
        print("Debe ser un número entero.")
        intento = -1
    else:
        if intento < numero_secreto:
            print("El número es más alto.")
        elif intento > numero_secreto:
            print("El número es más bajo.")
        else:
            print("Ese es el número, ENHORABUENA.")