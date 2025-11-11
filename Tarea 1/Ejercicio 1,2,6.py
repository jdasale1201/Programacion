#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)
precio = int(input("Introduce precio sin IVA: "))
IVA = 10
total = (precio * IVA/100) + precio
print("El precio total es: ", total)
print("El precio sin IVA es: ", precio)
print("El IVA es de: ", IVA, "%")