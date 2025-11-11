#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio. 
h = int(input("Pon las horas que trabajas: "))
Cobro = int(input("Dime cuanto cobras por hora: "))

Importe = h * Cobro

print("El importe total es ", Importe, "euros")