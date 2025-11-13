#Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. 
# Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. 
# Si el usuario introduce cualquier otra cosa que no sea un número, (mas adelante veremos como detectar los fallos usando try y except)
def pedirNumero(a):
    num = (input("Dame un número entero (fin para acabar): "))
    if num.lower() == 'fin':
        return False
    numeros.append(int(num))
    return True

def numerosEnLista(a):
    total = 0
    cuenta_num = 0
    for i in a:
        cuenta_num = cuenta_num + 1
    for n in a:
        total = total + n
        media = total / cuenta_num
    return media

try:
    numeros = []
    seguir = True
    while seguir:
        seguir = pedirNumero(numeros)
    print(f"Los números son: {numeros}.")
    print(f"La media es:{numerosEnLista(numeros):.2f}")
except ValueError:
    print("Valor no válido.")