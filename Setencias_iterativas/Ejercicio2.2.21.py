#Crear un programa que permita al usuario ingresar los montos de las compras de un
# cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada
# ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa
# un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al
# finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total
# de $1000, se le debe aplicar un 10% de descuento.

total = 0
importe = -1
while (importe !=0):
    importe=float(input("Introduce importe de compra (0.Finalizar): "))
    if importe>0:
        total=total+importe

if total>=1000:
    print("El total con descuento es: {}", total*0.9)
else:
    print("El total es: ",total)