#PROGRAMA
#Programa que pregunte al usuario su edad
#Muestre por pantalla que es menor de edad
#Declaracion
edad=0
import os

#Input
edad=int(os.sys.argv[1])

#Processing
if (edad>0 and edad<18):
    print ("Eres menor de edad.")
#En caso no sea asi, mostrar que es mayor de edad
elif (edad>18):
    print ("Eres mayor de edad")
#En caso sea igual a 0 entonces mostrar que es recien nacido
elif (edad==0):
    print("Recien nacido")
