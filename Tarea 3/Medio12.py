# Calcula la solución de una ecuación de segundo grado contemplando las
#diferentes condiciones de entrada que se puedan dar.

def ecuacion(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "La ecuación tiene infinitas soluciones."
            else:
                return "No tiene solución."
        else:
            solución = -c / b
            return solución
    else:
        paso1 = (b ** 2) - (4 * a * c)
        if paso1 < 0:
            return "No tiene número reales."
        else:
            paso2 = paso1 ** 0.5
            paso3 = -b + paso2
            paso4 = -b - paso2
            paso5 = 2 * a
            solución1 = paso3 / paso5
            solución2 = paso4 / paso5
    return solución1,solución2

num1 = int(input("Dime el primer número: "))
num2 = int(input("Introduce segundo número: "))
num3 = int(input("Intruduce tercer número: "))

print(ecuacion(num1,num2,num3))
