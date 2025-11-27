#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la
# frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el
# carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la
# posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se
# encontró y finalizar la ejecución.

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

encontrado = False
i=0
while i<len(frase) and (not encontrado):
    if frase[i]==letra:
        print(f"En la posición {i} la letra es {letra}.")
        encontrado = True
    i+=1

if not encontrado:
    print("Letra no encontrada...")