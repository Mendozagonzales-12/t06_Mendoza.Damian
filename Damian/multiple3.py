#Calcular el precio de venta del producto
#Declaracion
precio_venta=0
ganancia=0
precio_compra=0
import os

#Input
precio_compra=int(os.sys.argv[1])
ganancia=int(os.sys.argv[2])

#Processing
precio_venta=precio_compra+ganancia

if (precio_venta>0):
    print("el precio de venta es:",precio_compra+ganancia)
if(precio_venta>800):
    print("venta regular")
if(precio_venta>900):
    print("Muy buena venta")
if(precio_venta>1000):
    print("Excelente venta")

