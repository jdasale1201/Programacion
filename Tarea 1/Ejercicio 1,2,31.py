#Mostrar descomposición factorial (antes los divisores de un número)

from sympy import isprime

num = int(input("Dame un numero:"))

#Comprueba que no es un numero primo

if isprime(num):
    print(f"Es primo no tiene divisores, solo el mismo:{num}")
else:
    if(num<4):
        print("Demasiado pequeño para descomponer")
    else:
        i=2
        while(i<=num):
            if(num%i==0):
                print("{:3d} es un divisor" .format(i))
                num=num//i
            else:
                i=i+1