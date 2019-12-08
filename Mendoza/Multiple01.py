#Programa que pregunte al usuario su renta anual
#muestre por pantalla el tipo impositivo que le corresponde
#Declaracion
renta=0.0
import os

#Input
renta=float(os.sys.argv[1])

#Processing
#si la rena<10000 entonces su tipo de impositivo es 5
if (renta<10000):
    tax=5
#si la renta>=10000 y renta<20000 entonces su tipo de impositivo es 15
if (renta>=10000 and renta<20000):
    tax=15
#si la renta>=20000 y renta<30000 entonces su tipo de impositivo es 20
if (renta>=20000 and renta<30000):
    tax=20
#si la renta>=30000 y renta<45000 entonces su tipo de impositivo es 30
if (renta>=30000 and renta<45000):
    tax=30
#si la renta>=45000 entonces su tipo de impositivo es 45
if (renta>=45000):
    tax=45
print("TU TIPO IMPOSITIVO ES"+str(tax)+"%")
