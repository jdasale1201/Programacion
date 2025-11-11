#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 
capital = float(input("Introduce tus ahorros:"))
interes = 4 / 100
capital_primer_año = capital * (1 + interes)
capital_segundo_año = capital_primer_año * (1 + interes)
capital_tercer_año = capital_segundo_año * (1 + interes)
print(f"La rentabilidad obtenida de {capital} euros es de {capital_primer_año:.2f} euros el primer año, de {capital_segundo_año:.2f} euros el segundo año y de {capital_tercer_año:.2f} euros el tercer año.")