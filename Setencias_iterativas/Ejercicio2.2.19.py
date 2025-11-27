#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3- finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error.
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las
# opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión
# del menú y el programa finalizará.

def menu():
    print("\nEl menú tiene las siguientes opciones:")
    print("1. Comenzar programa.")
    print("2. Imprimir listado.")
    print("3. Finalizar programa.")

def opcion1():
    print("Hola buenos días.")

def opcion2():
    print("Hola buenas noches.")

def opcion3():
    print("Saliendo del programa...")

opcion = 0

while opcion != 3:
    menu()
    try:
        opcion = int(input("Elige una opción: 1, 2 o 3: "))
    except ValueError:
        print("Indique una opción válida.")
        opcion = 0 
    else:
        match opcion:
            case 1:
                opcion1()
            case 2:
                opcion2()
            case 3:
                opcion3()
            case _:
                print("Opción incorrecta. Intente de nuevo.")
