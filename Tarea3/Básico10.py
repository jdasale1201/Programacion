#Evaluar si una edad permite votar

def votar(a):
    if a < 18:
        print("No puedes votar.")
    else:
        print("Puedes votar")

edad = int(input("Dime tu edad y te digo si puedes votar: "))

print(votar(edad))