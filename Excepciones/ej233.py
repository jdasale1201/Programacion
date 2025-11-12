#Escribir un programa que pida al usuario un numero entero positivo y haga su cuenta atrás hasta 0 separado por comas.

num = -1
while num != 0:
    try:
        num=int(input("Dime un número entero: "))

        if num > 0:
            salida = ""
            for i in range(num,-1,-1):
                salida = salida + str(i) + ", "
            print(salida[:-2]+".")
    except ValueError:
        print("Valor no válido.")
    except TypeError:
        print("Error en conversión de tipos.")
    else:
        num = 0