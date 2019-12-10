#Calcular el costo de venta
#Declaracion
existencia_inicial=0
costo_produccion=0
existencia_final=0
costo_venta=0
import os

#Input
costo_venta=int(os.sys.argv[1])

#Processing
costo_venta=existencia_inicial+costo_produccion-existencia_final

if (costo_venta>670)
    print("el costo de venta es:", existencia_inicial+costo_produccion-existencia_final)
else:
    print("Hay perdida")
