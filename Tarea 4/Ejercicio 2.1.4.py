#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def ParoImpar(a):
    if(a % 2 == 0):
        return True
    else:
        return False


try:
    num = int(input("Dime un número entero: "))
    if ParoImpar(num):
        print("El número es par.")
    else:
        print("Es impar.")
except  ValueError:
    print("Debe ser un número entero.")
