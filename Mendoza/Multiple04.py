#Programa que pida al usuario un numero entero
#Declaracion
numer=0
import os

#Input
numer=int(os.sys.argv[1])

#Processing
#si el numero>0 entonces Muestre por pantalla es positivo
if (numer>0):
    print("El número " + str(numer) + " es positivo")
#si el numero<0 entonces Muestre por pantalla es negativo
if(numer<0):
    print("El número " + str(numer) + " es negativo")
#si el numero==0 entonces Muestre por pantalla es neutro
if (numer==0):
    print("El número " + str(numer) + " es neutro")
