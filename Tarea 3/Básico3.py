#Multiplicar sin usar el símbolo * (dos números)

def multiplicar(a, b):
    resultado = 0
    for i in range(b):
        resultado = resultado + a
    return resultado

a = int(input("Introduce primer numero: "))
b = int(input("Introduce segundo numero: "))

print(f"El resultado de {a} multiplicado por {b} es", multiplicar(a,b))

