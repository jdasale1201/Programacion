#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter. 

Nacimiento = str(input("Introduce fecha de nacimiento dd/mm/aaaa: "))
Fecha = Nacimiento.split('/')
dia = int(Fecha[0])
mes = int(Fecha[1])
año = int(Fecha[2])
print(f"Naciste el día {dia} en el mes {mes} del año {año}")