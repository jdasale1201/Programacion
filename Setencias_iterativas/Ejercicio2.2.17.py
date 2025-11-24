#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def sumaDigito(a):
    resultado = 0
    caracter = str(a)
    if a < 0:
        print("Debe ser mayor a 0.")
    else:
        for digito in caracter:
            numero = int(digito)
            resultado += numero
        return resultado

try:
    num = int(input("Dime un número para sumar sus dígitos: "))
    print("La suma de los dígitos es: ", sumaDigito(num))
except ValueError:
    print("Valor inváliido.")