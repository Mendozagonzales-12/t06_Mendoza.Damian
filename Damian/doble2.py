#Dado los numeros mostrar el promedio
#Declaracion
num1=0
num2=0
promedio=0
import os

#Input
num1=int(os.sys.argv[1])
num2=int(os.sys.argv[2])

#Procesing
promedio=num1+num2/2

if (promedio>0):
    print("el promedio de los numeros es:",num1+num2/2)
else:
    print("es negativo")
