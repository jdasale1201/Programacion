#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("El segundo número no puede ser 0.")
    else:
        return a / b

try:
    num1 = int(input("Dame el primer número como entero: "))
    num2 = int(input("Dame el segundo número como entero: "))
    resultado = division(num1, num2)
    print(f"El resultado de la división es: {resultado}")
except ValueError:
    print("Debe ser un número entero.")
except ZeroDivisionError as cero:
    print(cero)
except Exception as cero:
    print("Ocurrió un error inesperado:", cero)
