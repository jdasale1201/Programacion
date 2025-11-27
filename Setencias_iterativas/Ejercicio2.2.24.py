#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números
# mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números
# primos ingresados.

from Ejercicio2210 import primo
#import Ejercicio2.2.10
numero = 1
primos = 0

try:
    while (numero !=0):
        numero = int(input("Introduce un numero(zero para terminar): "))
        if numero ==1:
            print("Error, el 1 no vale.")
        else:
            numero=abs(numero)
            #cuidado con el 0
            if primo(numero):
                primos+=1
except ValueError:
    print("Valor inválido.")

print(f"Has introducido {primos} primos.")
