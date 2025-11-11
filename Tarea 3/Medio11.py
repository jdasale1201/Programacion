#Realiza un subprograma que intercambie el valor de dos variables enteras.

def intercambio(a,b):
    c=0
    c = a
    a = b
    b = c
    return a,b

num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

print(intercambio(num1,num2))