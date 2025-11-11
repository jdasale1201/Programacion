#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. 

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))


if(num2 == 0):
    print("No se puede dividir entre 0")
else:
    division = num1 / num2
    print(f"El resultado de la division es {division}")