#Escribir un programa que pida al usuario un número entero positivo y muestre porpantalla todos los números impares desde 1 hasta ese número separados por comas.

try:
    número = int(input("Dame un número entero positivo y mayor a 0: "))
    if número <= 0:
        print("Debe ser mayor a 0")
    else:
        impares = []
        for i in range(1,número):
            if i % 2 != 0:
                impares.append(str(i))
        print(", ".join(impares))
except ValueError:
    print("Valor no válido.")