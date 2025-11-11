#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def Grupo(nombre, sexo):
    if not nombre:
        raise NameError("No has introducido un nombre válido.")

    inicial = nombre.lower()[0]
    sexo = sexo.lower()

    if sexo not in ["femenino", "mujer", "masculino", "hombre"]:
        raise ValueError("Sexo no reconocido. Usa 'femenino' o 'masculino'.")

    if (sexo in ["femenino", "mujer"] and inicial < "m") or (sexo in ["masculino", "hombre"] and inicial > "n"):
        print("Perteneces al grupo A.")
    else:
        print("Perteneces al grupo B.")

try:
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu sexo: ")

    Grupo(nombre, sexo)

except ValueError as e:
    print(f"Error: {e}")
except NameError as e:
    print(f"Error: {e}")
