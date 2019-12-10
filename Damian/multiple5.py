#Calcular el costo de venta
#Declaracion
existencia_inicial=0
costo_produccion=0
existencia_final=0
costo_venta=0
import os

#Input
existencia_inicial=int(os.sys.argv[1])
costo_produccion=int(os.sys.argv[2])
existencia_final=int(os.sys.argv[3])

#Processing
costo_venta=existencia_inicial+costo_produccion-existencia_final

if (costo_venta>0):
    print("el costo de venta es:", existencia_inicial+costo_produccion-existencia_final)
if(costo_venta>40):
    print("ineficiente")
if(costo_venta>60):
    print("regular")
if(costo_venta>90):
    print("eficiente")
