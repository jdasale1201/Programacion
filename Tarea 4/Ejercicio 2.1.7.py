#Los tramos impositivos para la declaración de la renta en un determinado país son los
#siguientes:
#Renta Tipo impositivo
#Menos de 10000€ 5%
#Entre 10000€ y 20000€ 15%
#Renta Tipo impositivo
#Entre 20000€ y 35000€ 20%
#Entre 35000€ y 60000€ 30%
#Más de 60000€ 45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
#tipo impositivo que le corresponde.

def RentaImpositivo(a):
    if ingresos < 0:
        raise NameError ("No puede ser negativo.")
    else:
        if (a < 10000):
            tipo = 5
        elif (a >= 10000 and a < 20000):
            tipo = 15
        elif (a >= 20000 and a < 35000):
            tipo = 20
        elif (a >= 35000 and a < 60000):
            tipo = 30
        else:
            tipo = 45

        return tipo

try:
    ingresos = float(input("Pon tus ingresos anuales: "))
    valor = RentaImpositivo(ingresos)
    print(f"Tienes que pagar este porcentaje: {valor}" + "%")
except Exception as e:
    print(f"Algo salió mal: {e}")
except ValueError:
    print("Error: Debes introducir un número válido.")