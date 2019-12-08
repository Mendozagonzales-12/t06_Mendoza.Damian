#Programa que pida dos numeros
#Muestre en pantalla si el primero es mayor
#Declaracion
num1,num2=0,0
import os

#Input
num1=int(os.sys.argv[1])
num2=int(os.sys.argv[2])

#Processing
#si el numero 2>numero 1, indicarlo en pantalla
if(num1>num2):
    print("El primer numero",num1," es mayor que ",num2)
else:
    print("Numero ",num2," Es mayor que ",num1)
