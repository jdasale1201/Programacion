#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el
# usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares
# tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

digitosPares = 0
digitosImpares = 0

valor=input("Dame un valor: ")
for i in valor:
    aux=int(i)
    if aux%2==0:
        digitosPares+=1
    else:
        digitosImpares+=1

print(f"Has metido {digitosImpares} digitos impares y {digitosPares} digitos pares.")