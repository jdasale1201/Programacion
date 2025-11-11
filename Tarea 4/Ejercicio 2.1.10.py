#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
#ingredientes para cada tipo de pizza aparecen a continuación.
#• Ingredientes vegetarianos: Pimiento y tofu.
#• Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
#función de su respuesta le muestre un menú con los ingredientes disponibles para que
#elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están
#en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
#vegetariana o no y todos los ingredientes que lleva.

def presentación():
    print("Bienvenido a la pizzería Bella Napoli.")
    print("Tipos de pizza disponibles:")
    print("1. Vegetariana")
    print("2. No vegetariana")
    print("0. Salir")

def vegano():
    print("Has elegido una pizza vegetariana.")
    print("Ingredientes disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    print("0. No quiero más ingredientes.")

def carne():
    print("Has elegido una pizza no vegetariana.")
    print("Ingredientes disponibles:")
    print("1. Pepperoni")
    print("2. Jamón")
    print("3. Salmón")
    print("0. No quiero más ingredientes.")

tipo_pizza = ""
ingredientes_seleccionados = ["mozzarella", "tomate"]
opcion = -1

while opcion != 0:
    presentación()

    try:
        opcion = int(input("Elige el tipo de pizza (1, 2 o 0 para salir.): "))
    except ValueError:
        print("Opción inválida, escoge una opción disponible.\n")
        continue
    match opcion:
        case 1:
            tipo_pizza = "vegetariana"
            vegano()
            ingrediente = -1
            while True:
                try:
                    ingrediente = int(input("Elige un ingrediente (1, 2 o 0 para salir.): "))
                except ValueError:
                        print("Opción inválida, escoge una opción disponible.\n")
                        continue
                match ingrediente:
                        case 1:
                            ingredientes_seleccionados.append("pimientos")
                            print("Has elegido pimiento.\n")
                        case 2:
                            ingredientes_seleccionados.append("tofu")
                            print("Has elegido tofu.\n")
                        case 0:
                            print("Saliendo del menú de ingredientes.\n")
                            break
                        case _:
                            print("Opción no válida. Por favor elige 1, 2 o 0 para salir.\n")

        case 2:
            tipo_pizza = "no vegetariana"
            carne()
            ingrediente = -1
            while True:
                try:
                    ingrediente = int(input("Elige un ingrediente (1, 2, 3 o 0): "))
                except ValueError:
                            print("Opción inválida, escoge una opción disponible.\n")
                            continue
                match ingrediente:
                            case 1:
                                ingredientes_seleccionados.append("pepperoni")
                                print("Has elegido pepperoni.\n")
                            case 2:
                                ingredientes_seleccionados.append("jamón")
                                print("Has elegido jamón.\n")
                            case 3:
                                ingredientes_seleccionados.append("salmón")
                                print("Has elegido salmón.\n")
                            case 0:
                                print("Saliendo del menú de ingredientes.\n")
                                break
                            case _:
                                print("Opción no válida. Por favor elige 1, 2, 3 o 0.\n")

        case 0:
            print("Gracias por visitar Bella Napoli.")

        case _:
            print("Elige una opción válida, por favor.\n")

print(f"Tu tipo de pizza es {tipo_pizza} y tiene estos ingredientes: \n")
print(", ".join(ingredientes_seleccionados))
print("Gracias por venir.")