# Contar vocales, en una palabra

def contador_letras(palabra):
    vocales = 'aeiouáéíóúü'
    contador = 0
    for i in palabra.lower():
        if i in vocales:
            contador = contador + 1
    return contador

otra_palabra = input("Dime una palabra: ")
print("Tu palabra tiene", contador_letras(otra_palabra))