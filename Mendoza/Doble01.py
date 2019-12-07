#PROGRAMA
#Dado un numero, mostrar su mitad
#si el numero es positivo
#Declaracion
numero=0
import os

#Input
numero=int(os.sys.argv[1])

#Processing
#en caso sea negativo, mostrar que es un negativo
if (numero>0):
    print("La mitad es:",numero/2)
else:
    print ("Es un negativo")
