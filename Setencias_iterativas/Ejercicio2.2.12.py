#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Dime una frase: ")
palabra_encontrar = input("Qué palabra buscas?: ").lower()
frase_contar = frase.lower().split()
palabras = frase_contar.count(palabra_encontrar)

print(f"La palabra '{palabra_encontrar}' aparece {palabras} veces en la frase: '{frase}'")
