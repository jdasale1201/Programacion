#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. 
peso = float(input("Introduce tu peso en kilogramos:"))
altura = float(input("Introduce tu altura en metros:"))
indice_de_masa_corporal = peso / (altura**2)
print(f"Tu indice de masa corporal es {indice_de_masa_corporal:.2f}")