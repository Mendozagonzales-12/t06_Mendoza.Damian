#PROGRAMA
#Dado un numero, mostrar su mitad
#siempre y cuando el numero sea negativo
#Declaracion
numero=0
import os

#Input
numero=int(os.sys.argv[1])

#Processing
if (numero>0):
    print("La mitad es:",numero/2)
