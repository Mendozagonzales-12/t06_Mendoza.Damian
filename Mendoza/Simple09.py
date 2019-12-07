#Programa Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
#Si se compran tres camisas o más se aplica un descuento del 20%
#sobre el total de la compra
#Declaracion
nc=0
costo,des,pt,pc=0.0,0.0,0.0,0.0
import os

#Input
nc=int(os.sys.argv[1])
pc=float(os.sys.argv[2])

#Processing
costo=nc*pc
des=costo*0.20
pt=costo-des

if (nc>=3):
    print("El costo de las camisas es:",costo)
    print("El descuento es:",des)
    print("El costo total a pagar es",pt)

