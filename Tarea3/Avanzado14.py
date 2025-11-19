#Utilizando el ejercicio anterior, indica los divisores del número.
from Avanzado13 import primo

def es_primo(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    
    print(f"Sus divisores son: {divisores}")
    
    if len(divisores) == 2:
        print("Es primo.")
        return True
    else:
        print("No es primo.")
        return False


numero = int(input("Introduce un número: "))
es_primo(numero)
