#Leer números enteros positivos de teclado, 
# hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

def cuentaNumero():
    salir = 0
    numero = 0
    acumular = []
    while numero != salir:
        numero = int(input("Dime un numero entero: "))
        if numero == salir:
            return max (acumular)
        elif numero > 0:
            acumular.append(numero)
        else:
            print("Solo números positivos.")


try:
    print("Pon '0' para salir.")
    print(cuentaNumero())
except ValueError:
    print("Valor no válido.")