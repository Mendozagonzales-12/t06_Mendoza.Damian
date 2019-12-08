##Programa para que calcule el total a pagar por la compra de camisas.
#Declaracion
nc=0
pc=0.0
import os

#Input
nc=int(os.sys.argv[1])
pc=float(os.sys.argv[2])

#Processing
#Si se compran tres camisas o más se aplica un descuento del 20%
if (nc>=3 and nc<12):
    costo = nc*pc
    print("El costo de las camisas es ",costo)
    des = costo*0.20
    print("El descuento es ",des)
    pt = costo-des
    print("El costo total a pagar es ",pt)
#si son menos de tres camisas un descuento del 10%
if (nc<3):
    costo = nc*pc
    print("El costo de las camisas es ",costo)
    des = costo*0.10
    print("El descuento es ",des)
    pt = costo-des
    print("El costo total a pagar es ",pt)
#si son mas de 12 camisas un descuento del 50%
if (nc>=12):
    costo = nc*pc
    print("El costo de las camisas es ",costo)
    des = costo*0.50
    print("El descuento es ",des)
    pt = costo-des
    print("El costo total a pagar es ",pt)
