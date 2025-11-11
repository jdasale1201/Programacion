#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo. 
precio = int(input("Introduce precio sin IVA: "))
IVA = int(input("INtroduce el IVA: "))
total = (precio * IVA/100) + precio
print("El precio total es: ", total)