#Pide al usuario su edad y muestra:
# “Menor de edad” si es < 18
# “Adulto” si está entre 18 y 64
# “Adulto mayor” si es 65 o más.

def preguntaEdad(a):
    if a < 0:
        print("No puedes tener edad negativa.")
    elif a < 18:
        print("Eres menor de edad.")
    elif a >= 18 and a <= 64:
        print("Eres adulto.")
    else:
        print("Eres un anciano.")

try:
    edad = int(input("Dime tu edad: "))
    preguntaEdad(edad)
except ValueError:
    print("Valor inválido.")
