#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def primo(num):
    if num < 2:
        print("No es primo")
        return
    i = 2
    encontrado = False
    while i * i <= num and not encontrado:
        if num % i == 0:
            encontrado = True
        i = i + 1

    if encontrado:
        return False
    else:
        return True

try:
    num = int(input("Dime un número: "))
    n = primo(num)
    if n == False:
        print("No es primo.")
    else:
        print("Es primo.")
except ValueError:
    print("Error inesperado.")