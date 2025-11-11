#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre. 
nombre = input("Introduce tu nombre:")
nombre_mayus = nombre.upper()
contador_letras = len (nombre)
print(f"Buenas {nombre_mayus} tu nombre tiene {contador_letras} letras")