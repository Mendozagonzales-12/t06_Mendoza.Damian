#Para tributar un determinado impuesto se debe ser mayor a 18 años
#tener unos ingresos superiores a 1000 soles mensuales
#Programa que pregunte al usuario su edad y sus ingresos mensuales
#Muestre en pantalla si el usuario tiene que tributar
#Declaracion
edad_usua=0
ingresos=0.0
import os

#Input
edad_usua=int(os.sys.argv[1])
ingresos=float(os.sys.argv[2])

#Processing
#sino es mayor de edad y su sueldo es menor de 1000
#entonces no tiene que tributar
if (edad_usua>18 and ingresos>=1000):
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")
