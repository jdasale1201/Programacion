#Convertir grados Celsius a Fahrenheit

def convertir(a):
    resultado = (a * (9/5)) + 32
    return resultado

num = float(input("Dime un numero: "))
print(convertir(num))