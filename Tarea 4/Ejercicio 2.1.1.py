#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def eresMayorEdad(a):
    if a < 0 or a > 120:
        raise NameError("Edad fuera de rango")
    else:
        if a >= 18:
            return True
        else:
            return False

#PROGRAMA PRINCIPAL

try:
    edad = int(input("Dime tu edad: "))
    if eresMayorEdad(edad):
        print("Eres mayor de edad.")
    else:
        print("Toma un zumito de piña.")
except ValueError:
    print("Pon un número entero")
except Exception as ex:
    print(f"Ha ocurrido algo malo: {ex}")