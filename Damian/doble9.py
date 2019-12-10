#calcular el producto bruto interno
#Declaracion
consumo=0
inversion_efectuada=0
gasto_publico=0
producto_bruto_interno=0
import os

#Input
consumo=int(os.sys.argv[1])
inversion_efectuada=int(os.sys.argv[2])
gasto_publico=int(os.sys.argv[3])

#Processing
producto_bruto_interno=consumo+inversion_efectuada+gasto_publico

if (producto_bruto_interno>100):
    print("el producto bruto interno es:",consumo+inversion_efectuada+gasto_publico)
else:
    print("ineficiencia")
