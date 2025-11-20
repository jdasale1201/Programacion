#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

try:
    numero = int(input("Dame un número entero positivo y mayor a 0: "))
    
    if numero <= 0:
        print("Debe ser mayor a 0")
    else:
        for i in range(1, numero + 1):
            print(str("*") * i)

except ValueError:
    print("Valor no válido.")
