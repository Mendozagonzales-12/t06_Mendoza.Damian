#Dado los numeros mostrar el promedio
#Declaracion
exam1=0
exam2=0
promedio=0
import os

#Input
exam1=int(os.sys.argv[1])
exam2=int(os.sys.argv[2])

#Procesing
promedio=num1+num2/2

if (promedio>0):
    print("el promedio de los numeros es:",exam1+exam2/2)
if(promedio>10):
    print("mal alumno")
if(promedio>12):
    print("alumno regular")
if(promedio>15):
    print("buen alumno")
if(promedio>17):
    print("excelente alumno")
