#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
#ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
#función de su respuesta le muestre un menú con los ingredientes disponibles para que
#elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están
#en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
#vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzería Bella Napoli.")
print("Tipos de pizza disponible: ")
print("1. Vegetariana.")
print("2.No vegetariana.")

tipo = input("¿Quieres una pizza vegetariana? (si/no): ").lower

ingredientes_base = ["mozzarella" , "tomate"]

if(tipo == "si" or tipo == "sí"):
    print("Has elegido una pizza vegetariana.")
    print("Ingredientes disponibles: ")
    print("1.Pimiento.")
    print("2.Tofu.")
    opcion = input("Elige un ingrediente (1 o 2): ")

    if(opcion == 1):
        ingrediente = "pimiento"
    elif(opcion == 2):
        ingrediente = "tofu"
    else:
        print("Opcion no valida, se le pondra pimiento por defecto.")
        ingrediente = "pimiento"

    pizza_tipo = "Vegetariana"

else:
    print("Has elegido pizza no vegetariana.")
    print("Ingredientes disponibles: ")
    print("1.Pepperoni.")
    print("2.Jamon.")
    print("3.Salmon.")
    opcion = input("Elige un ingrediente (1,2 o 3): ")
    if(opcion == 1):
        ingrediente = "pepperoni"
    elif(opcion == 2):
        ingrediente = "jamon"
    elif(opcion == 3):
        ingrediente = "salmon"
    else:
        print("Opcion no valida, se le pondra jamon por defecto.")
        ingrediente = "jamon"

    pizza_tipo = "No Vegetariana"

print("\nTu pizza es", pizza_tipo)
print("Lleva estos ingredientes: ")
print(",".join(ingredientes_base + [ingrediente]))