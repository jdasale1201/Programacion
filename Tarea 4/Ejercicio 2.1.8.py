def rango(a):
    if a == 1:
        return 0.0
    elif a == 2:
        return 0.4
    elif a == 3:
        return 0.6

def menu():
    print("\n--- Niveles de desempeño ---")
    print("1. Inaceptable")
    print("2. Aceptable")
    print("3. Meritorio")
    print("0. Salir")

try:
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input("Elige uno de los niveles para los empleados: "))

        match opcion:
            case 1:
                dineroExtra = rango(1) * 2400
                print("Ganará:", 2400 + dineroExtra)
            case 2:
                dineroExtra = rango(2) * 2400
                print("Ganará:", 2400 + dineroExtra)
            case 3:
                dineroExtra = rango(3) * 2400
                print("Ganará:", 2400 + dineroExtra)
            case 0:
                print("Saliendo del programa...")
            case _:
                print("Opción no válida. Inténtalo de nuevo.")

except ValueError:
    print("Valor incorrecto. Debes introducir un número válido.")

