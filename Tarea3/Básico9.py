#Calcular el área de un rectángulo

def área(a,b):
    resultado = a * b
    return resultado

print("Vamos a calcular el área de un rectangulo.")
num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame el segundo número: "))
print(área(num1,num2))