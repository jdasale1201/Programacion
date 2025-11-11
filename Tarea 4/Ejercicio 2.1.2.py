#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def contraseña():
    PIN_correcto = "alberti" 
    intentos = 0
    max_intentos = 1

    while intentos < max_intentos:
        intento_usuario = input("Introduce contraseña: ")
        intento_usuario = intento_usuario.lower()
        if intento_usuario == PIN_correcto:
            print("Bienvenido.")
            return True  
        else:
            intentos += 1
            intentos_restantes = max_intentos - intentos
            if intentos_restantes > 0:
                print(f"PIN incorrecto, te quedan {intentos_restantes} intentos.")
            else:
                print("Superaste límite de intentos, usuario bloqueado.")
                return False 

print("El pin es 'alberti'")
contraseña()
