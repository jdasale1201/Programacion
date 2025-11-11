#Calcular la serie de Fibonacci hasta un valor dado

num =int(input("Hasta qué número:"))

i = 0
j=1
punta=i+j

print(i)
print(j)
print(punta)
while(punta<=num):
    i=j
    j=punta
    punta=i+j
    if(punta<=num):
        print(punta)
