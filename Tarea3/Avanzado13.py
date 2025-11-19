#Crea un subprogama que indique si un número es primo o no lo es.

def primo(num):
    if num < 2:
        print("No es primo")
        return
    i = 2
    encontrado = False
    while i * i <= num and not encontrado:
        if num % i == 0:
            encontrado = True
        i = i + 1

    if encontrado:
        return False
    else:
        return True

if __name__ == "__main__":

    num = int(input("Dime un número: "))
    n = primo(num)
    if n == False:
        print("No es primo.")
    else:
        print("Es primo.")