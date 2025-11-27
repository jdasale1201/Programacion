#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def contraseña():
    PIN_correcto = "alberti"
    intento_usuario = ""

    while PIN_correcto != intento_usuario:  
        intento_usuario = input("Introduce la contraseña: ")
        intento_usuario = intento_usuario.lower()
        if intento_usuario == PIN_correcto:
            print("Bienvenido.")
            return True
        else:
            print("Contraseña incorrecta. Intenta de nuevo.")

print("El pin es 'alberti'")
contraseña()
