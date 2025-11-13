# Escribe otro programa que pida una lista de números como la anterior y al
#final muestre por pantalla el máximo y mínimo de los números, en vez de la media.

def pedirNumero(a):
    num = (input("Dame un número entero (fin para acabar): "))
    if num.lower() == 'fin':
        return False
    numeros.append(int(num))
    return True

try:
    numeros = []
    seguir = True
    while seguir:
        seguir = pedirNumero(numeros)
    print(f"El número más grande es: {max(numeros)}.")
    print(f"El número más pequeño es: {min(numeros)}.")
except ValueError:
    print("Valor no válido.")