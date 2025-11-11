#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. 
celsius = float(input("Ingresa la temperatura en grados celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit.")