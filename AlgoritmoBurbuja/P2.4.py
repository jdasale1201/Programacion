def burbuja(n):
    for i in range(len(n) - 1):
        for j in range(0, len(n) - 1 - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

numero = [22,0,90,56,60,37,78,50]
print(numero)
burbuja(numero)
print(numero)  