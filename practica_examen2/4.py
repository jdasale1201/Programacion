#Pide un número N e
# imprime la suma de todos los números pares desde 1 hasta N.

def sumaPares(a):
    acumular = 0
    for i in range(1,a+1,1):
        if i % 2 == 0:
            acumular = i + acumular
    return acumular

try:
    n1 = int(input("Dime un numero entero: "))
    if n1 < 1:
        print("Debe ser un número entero positivo.")
    else:
        print("La suma de los números de", n1,"es", sumaPares(n1))
except ValueError:
    print("Valor inválido.")