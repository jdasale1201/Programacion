#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def eco():
    salir = "salir"
    palabra = ""

    while palabra != salir:
        palabra = input("Dime una palabra: ")
        if palabra == salir:
            print("Saliendo del programa...")
        else:
            print(palabra)

print("Escribe 'salir' para finalizar.")
eco()