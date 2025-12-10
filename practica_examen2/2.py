#Solicita dos números y un operador (+, –, *, /).
# Realiza la operación o muestra un mensaje si el operador no es válido.

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def menu():
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")

try:
    num1 = int(input("Dame un número entero: "))
    num2 = int(input("Dame otro número entero: "))
except ValueError:
    print("Error de valor.")

opcion = -1

menu()
try:
    opcion = int(input("Elige una opcion: "))
    match opcion:
        case 1:
            print("La suma es: ", suma(num1, num2))
        case 2:
            print("La resta es: ", resta(num1, num2))
        case 3:
            print("La multiplicación es: ", multiplicacion(num1, num2))
        case 4:
            try:
                print("La división es: ", division(num1, num2))
            except ZeroDivisionError:
                print("No se puede dividir entre 0.")
        case _:
            print("Opción no válida.")
except ValueError:
    print("Debes introducir un número válido.")