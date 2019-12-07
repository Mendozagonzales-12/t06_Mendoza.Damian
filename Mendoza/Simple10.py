#Crear un programa que resuelva la ecuación cuadrática tipo ax2 + bx + c
#Declaracion
a,b,c,d=0.0,0.0,0.0,0.0
import os

#Input
a=float(os.sys.argv[1])
b=float(os.sys.argv[2])
c=float(os.sys.argv[3])

#Processing
d=((b*b)-4)*a*c

if (d<0):
    print ("No existe soluciones reales!!")
