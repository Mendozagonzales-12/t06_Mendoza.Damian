#PROGRAMA
#Programa que pregunte al usuario su edad
#Muestre por pantalla que es menor de edad
#Declaracion
edad=0
import os

#Input
edad=int(os.sys.argv[1])

#Processing
#En caso no sea asi, mostrar que es mayor de edad
if (edad<18):
    print ("Eres menor de edad.")
else:
    print ("Eres mayor de edad")
