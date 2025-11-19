#Crea un subprograma que reciba una nota decimal y devuelva si está suspenso, aprobado, notable o sobresaliente.

def nota(a):
    if a < 0 or a >10:
        print("La nota debe estar entre 0 y 10")
    elif a < 5:
        print("Suspenso")
    elif a >= 5 and a <= 6:
        print("Aprobado")
    elif a >= 7 and a <= 8:
        print("Notable")
    else:
        print("Sobresaliente")

num = float(input("Dime tu nota: "))
print(nota(num))