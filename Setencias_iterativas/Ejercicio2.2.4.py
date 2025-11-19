#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

try:
    número = int(input("Dame un número entero positivo y mayor a 0: "))
    if número <= 0:
        print("Debe ser mayor a 0")
    else:
        for i in range(número,0,-1):
            print(i)
except ValueError:
    print("Valor no válido.")