#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = float(input("Introduce el precio con 2 decimales:"))

Euro = int(precio // 1)
Centimos = precio-(precio // 1)

print(f"Son {Euro}euros y {Centimos:.2f}céntimos")