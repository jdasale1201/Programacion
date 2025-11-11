#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def edadTributar(e):
    if e < 0 or e >150:
        raise NameError("La edad no es válido.")
    elif e<16:
        return False
    else:
        return True

def ingresosTributar(i):
    if i<0:
        raise NameError("INGRESOS NEGATIVOs.")
    elif i<1000:
        return False
    else:
        return True

try:
    edad = int(input("Dime la edad: "))
    ingresos = float(input("Dime tus ingresos: "))

    if edadTributar(edad) and ingresosTributar(ingresos):
        print("Tienes que pagar.")
    else:
        print("No tienes que pagar.")
except ValueError:
    print("Valores no válidos.")
except Exception as e:
    print(f"Algo no ha salido bien: {e}")