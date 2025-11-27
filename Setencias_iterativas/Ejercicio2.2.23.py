#Crear un programa que permita al usuario ingresar títulos de libros por teclado,
# finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese
# un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una
# línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9)
# aparecieron en total (en todos los títulos de libros que componen en esa línea).
# Finalmente, informar cuántas líneas completas se ingresaron. 

print("Ingresa títulos de libros. Usa '/' para terminar una línea y '*' para finalizar el programa.")

línea_actual = ""
líneas_completas = 0
entrada = ""

while entrada!='*':
    entrada=input("Título: ")
    if entrada == "/":
        #contar dígitos sin isdigito
        total_dígitos = 0
        for titulo in línea_actual:
            for caracter in titulo:
                if caracter in "0123456789":
                    total_dígitos = total_dígitos + 1
        print("Dígitos numéricos en esta línea:",total_dígitos)
        líneas_completas = líneas_completas + 1
        línea_actual = "" #Reiniciar la línea
    else:
        línea_actual = línea_actual + entrada

print("\n Total de líneas completas ingresadas:",líneas_completas)