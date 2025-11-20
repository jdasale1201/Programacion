#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

def triangulo(a):
    if a <= 0:
        print("El número tiene que ser mayor a 0.")
        return
    else:
        for i in range(1,a + 1):
            linea = ""
            for j in range(2*i-1,0,-2):
                linea = linea + str(j)
            print(linea)

try:
    numero = int(input("Dame un número entero mayor a 0: "))
    triangulo(numero)
except ValueError:
    print("Valor inválido.")