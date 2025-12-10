#Pide un número entero positivo y 
# di cuántos dígitos tiene usando un bucle, no usando len().

try:
    numero = int(input("Introduce un número entero positivo: "))
except ValueError:
    print("Debe ser un número entero.")

if numero < 0:
    print("El número debe ser positivo.")
else:
    cadena = str(numero)
    contador = 0
    for i in cadena:
        digito = int(i)
        contador= contador + 1

print(f"El número tiene {contador} digitos.")