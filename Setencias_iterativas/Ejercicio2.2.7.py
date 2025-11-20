#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablaMultiplicar(a):
    for i in range(1,11):
        resultado = i * a
        print(f"{i} x {a} es: {resultado}")

try:
    numero = int(input("Dame un número entero: "))
    tablaMultiplicar(numero)
except ValueError:
    print("Valor inválido.")