#Escribe un programa que  pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separado por comas.

try:
    numero = int(input("Introduce un número entero: "))
except ValueError:
    print("NO ES UN VALOR VÁLIDO.")
except TypeError:
    print("FALLO EN LA CONVERSIÓN DE TIPOS.")
else:
    cadena = ""
    for i in range(1,numero+1):
        if i%2 !=0:
            cadena = cadena + str(i) + ", "
    print(cadena[:-2])
finally:
    print("HASTA LUEGO.")