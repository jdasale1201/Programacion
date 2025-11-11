# Indicar si un número es par

def EsPar(a):
    if(a % 2 == 0):
        print(f"{a} es par")
    else:
        print(f"{a} es impar")

num = int(input("Dime un numero: "))
print(EsPar(num))