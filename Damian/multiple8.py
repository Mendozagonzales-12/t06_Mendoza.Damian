#calcular la cuota del cliente
#Declaracion
saldo_capital=0.0
suma_factores=0.0
cuota=0.0
import os

#Input
saldo_capital=float(os.sys.argv[1])
suma_factores=float(os.sys.argv[2])

#Processing
cuota=saldo_capital/suma_factores

if (cuota>0.0):
    print("la cuota del cliente es:",saldo_capital/suma_factores)
if (cuota<0.5):
    print("el monto de prestamo es recomendando")
if (cuota<0.10):
    print("el monto de prestamo es bueno")
if (cuota<0.15):
    print("el monto de prestamo no es recomendado puesto a sus condiciones de pago")
if (cuota<0.20):
   print("cliente en riesgo de deuda ")

