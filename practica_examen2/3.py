#Pide un número positivo e imprime un contador hacia atrás hasta llegar a 0.

def cuentaAtras(a):
    for i in range(a,0-1,-1):
        print(i)

try:
    num1 = int(input("Dame un número entero: "))
except ValueError:
    print("Valor inválido.")

cuentaAtras(num1)