#Calcular la ganancia que tendra el vendedor
#Declaracion
precio_venta=0
precio_compra=0
ganancia=0
import os

#Input
precio_compra=int(os.sys.argv[1])
precio_venta=int(os.sys.argv[2])

#Processing
ganancia=precio_compra-precio_venta

if (ganancia>0):
    print("la ganancia es:",precio_compra-precio_venta)
if(ganancia>100):
    print("no hay ganancia")
if(ganancia>200):
    print("resultado no satisfactorio")
if(ganancia>300):
    print("Regular")
if(ganancia>400):
    print("Hay ganancia")
