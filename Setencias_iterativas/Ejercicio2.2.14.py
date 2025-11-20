#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def cuentaNumero():
    salir = 0
    acumular = 0
    while True:
        numero = int(input("Dime un numero entero: "))
        if numero == salir:
            return acumular
        acumular = numero + acumular

try:
    print("Pon '0' para salir.")
    print(cuentaNumero())
except ValueError:
    print("Valor no válido.")