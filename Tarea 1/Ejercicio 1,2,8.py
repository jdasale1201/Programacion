#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes. 
acumulador = 0
num1 = float(input("Pon el numero 1:"))
acumulador += num1
num1 = float(input("Pon el numero 2:"))
acumulador += num1
num1 = float(input("Pon el numero 3:"))
acumulador = acumulador + num1
print(f"El resultado es:{acumulador:.2f}")