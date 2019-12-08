#Programa que pida al usuario una cantidad de euros, una tasa de interés, y unos años.
#Capital obtenido
#Declaracion
cantidad=0.0
interes=0.0
tiempo=0.0
import os

#Input
cantidad=float(os.sys.argv[1])
interes=float(os.sys.argv[2])
tiempo=float(os.sys.argv[3])

#Processing
cantidad_final=int(cantidad*(1+interes/100)**tiempo)
beneficio= int(cantidad_final-cantidad)
#Si la cantidad<2500 y tiempo<5 Muestra en pantalla el resultado del capital transcurrido
if(cantidad<2500 and tiempo<5):
    print ("El capital al final del transcurso es ",cantidad_final)
    print ("habiendo incrementado el patrimonio en ",beneficio)
#Si la cantidad>=2500 hasta <5000 y tiempo>=5 hasta <10 Muestra en pantalla el resultado del capital transcurrido
if((cantidad>=2500 and cantidad<5000) and (tiempo>=5 and tiempo<10)):
    print ("El capital al final del transcurso es ",cantidad_final)
    print ("habiendo incrementado el patrimonio en ",beneficio)
#Si la cantidad>=5000 y tiempo>=10 Muestra en pantalla el resultado del capital transcurrido
if(cantidad>=5000 and tiempo>=10):
    print ("El capital al final del transcurso es ",cantidad_final)
    print ("habiendo incrementado el patrimonio en ",beneficio)
