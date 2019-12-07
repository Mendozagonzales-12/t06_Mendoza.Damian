#Programa que pida al usuario un numero entero
#Muestre por pantalla si es par
#Declaracion
numer=0
import os

#Input
numer=int(os.sys.argv[1])

#Processing
if (numer%2==0):
    print("El número " + str(numer) + " es par")
