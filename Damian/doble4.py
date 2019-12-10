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

if (ganancia>1000):
    print("la ganancia es:",precio_compra-precio_venta)
else
    print("no hay ganancia")
