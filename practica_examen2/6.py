#Pide un número y un límite.
# Muestra su tabla de multiplicar desde x1 hasta x límite.

def tabla(a):
    for i in range(1,11):
        resultado = a * i
        print(resultado)

try:
    num = int(input("Dame un número entero: "))
    tabla(num)
except ValueError:
    print("Valor inválido.")