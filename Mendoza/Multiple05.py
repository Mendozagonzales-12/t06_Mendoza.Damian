#Para tributar un determinado impuesto se debe ser mayor a 18 años
#tener unos ingresos superiores a 1000 soles mensuales
#Programa que pregunte al usuario su edad y sus ingresos mensuales
#Declaracion
edad_usua=0
ingresos=0.0
import os

#Input
edad_usua=int(os.sys.argv[1])
ingresos=float(os.sys.argv[2])

#Processing
#si su edad>=18 y sus ingresos>=1000 entonces
#Muestre en pantalla el descuento de sus ingresos
if ((edad_usua>=18 and edad_usua<30)and (ingresos>=1000 and ingresos<2500)):
    des=ingresos*0.2
    print("Tienes que cotizar descontarle a sus ingresos")
#si su edad>=30 y sus ingresos>=2500 entonces
#Muestre en pantalla el descuento de sus ingresos
elif (edad_usua>=30 and ingresos>=2500):
    des=ingresos*0.4
    print("Tienes que cotizar descontarle a sus ingresos")
#sino es mayor de edad y su sueldo es menor de 1000
#entonces no tiene que tributar
else:
    print("No tienes que cotizar")
