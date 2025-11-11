

a = int(input("Introduce lado a:"))
b = int(input("Introduce lado b:"))
c = int(input("Introduce lado c:"))

semiperimetro = (a+b+c)/2
area = (semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c))**0.5

print(f"El area del triangulo es: {area}")