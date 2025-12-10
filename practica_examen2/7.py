#El usuario introduce números sin límite.
# El programa suma todos hasta que ingrese 0, y muestra el total.

total = 0
numero = -1

print("Introduce números hasta que pongas el 0: ")

while numero != 0:
    try:
        numero = float(input("Introduce un número(0 para salir.):"))
    except ValueError:
        print("Pon un número válido.")
        numero = 0
    else:
        total = total + numero

print(f"La suma total es: {total}")