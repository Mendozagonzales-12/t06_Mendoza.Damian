#calcular el area del triangulo
#Declaracion
base=0
altura=0
area=0
import os

#Input
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

#Processing
area=base*altura/2

if (area>0):
    print("el area del triangulo es:",base*altura/2)
