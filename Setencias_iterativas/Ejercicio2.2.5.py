#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

def formulaInversion(a,b,c):
    return a * (1 + b/100) ** c


try:
    inversion = float(input("Dime la cantidad invertida:  "))
    interes = float(input("El interes anual tambien tienes que decirlo: "))
    años = int(input("Durante cuantos años: "))
    for i in range(1,años + 1):
        capital = formulaInversion(inversion,interes,i)
        print(f"En el año {i} hubo una ganancia de {capital:.2f} ")
except ValueError:
    print("Algún valor no era válido")