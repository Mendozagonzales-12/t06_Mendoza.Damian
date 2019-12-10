#calcular la deuda promedio del cliente
#Declaracion
deuda_bcp=0
deuda_bvva=0
deuda_promedio=0
import os

#Input
deuda_bcp=int(os.sys.argv[1])
deuda_bvva=int(os.sys.argv[2])

#Procesing
deuda_promedio=deuda_bcp+deuda_bvva/2

if (deuda_promedio>0):
    print("la deuda promedio del cliente es:",deuda_bcp+deuda_bvva/2)
if(deuda_promedio>600):
    print("cliente normal")
if(deuda_promedio>900):
    print("cliente regular")
if(deuda_promedio>10000):
    print("cliente en riesgo")
if(deuda_promedio>12000):
    print("clinte en rojo")
