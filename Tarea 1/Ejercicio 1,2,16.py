#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.  
pan_duro = int(input("Barras de pan vendidas que no son del dia:"))
pan_del_dia = 3.49
rebaja = 0.6
descuento = pan_del_dia * rebaja
precio_final = pan_del_dia - descuento
coste_total = pan_duro * precio_final
print(f"Las barras de pan que son del dia cuestan:{pan_del_dia} euros")
print(f"Si la barra no es del dia:{descuento:.2f} euros de descuento")
print(f"Comprando {pan_duro} barras que no son del dia te saldria a:{coste_total:.2f}")