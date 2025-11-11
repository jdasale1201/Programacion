#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación, se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2400€ multiplicada por la puntuación del nivel. 
#Nivel Puntuación
#Inaceptable 0.0
#Aceptable 0.4
#Meritorio 0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario. 

nivel = float(input("Indica tu nivel siendo los siguientes '0.0','0.4','0.6':"))
if(nivel != 0.0 and nivel != 0.4 and nivel != 0.6):
    print("Muestra un nivel valido.")
else:
    sueldo_inicial = 2400 * nivel
    sueldo_final = 2400 + sueldo_inicial
    print(f"Tu sueldo es {sueldo_final}.")