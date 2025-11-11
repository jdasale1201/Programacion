#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta. 
Cesta = str(input("Escribe una cesta de la compra(separando con ','):"))
producto = Cesta.split(',')
print("\nLa lista de la compra son:")
for producto in producto:
    print(producto)