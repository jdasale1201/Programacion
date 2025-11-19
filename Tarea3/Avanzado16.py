#Realiza un subalgoritmo que permita a un usuario intentar 3 veces acertar el PIN de acceso a un dispositivo.

def contraseña():
    PIN_correcto = "1234" 
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        intento_usuario = input("Introduce PIN: ")
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

contraseña()
print("El pin es '1234")
