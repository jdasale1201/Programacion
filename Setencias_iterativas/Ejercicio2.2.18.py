#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la  suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron  números pares. 

def sumaDigito():
    salir = -1
    par = []
    while True:
        numero = int(input("Dime un número entero: "))
        if numero == salir:
            return len(par)
        elif numero < 0:
            print("Debe ser un número mayor a 0.")
        else:
            resultado = 0
            for digito in str(numero):
                resultado += int(digito)
            print(f"La suma de los dígitos de {numero} es: {resultado}")
            if numero % 2 == 0:
                par.append(numero)

try:
    print("Pon '-1' para finalizar.")
    cantidad_pares = sumaDigito()
    print(f"Cantidad de números pares ingresados: {cantidad_pares}")
except ValueError:
    print("Valor inválido.")