#calcular el mantenimiento de valor cuenta de ahorro
#Declaracion
monto_principal=0.0
tipo_cambio_dia_anterior=0.0
cambio_dia_hoy=0.0
mantenimiento_valor_cuenta_de_ahorro=0.0
import os

#input
monto_principal=float(os.sys.argv[1])
tipo_cambio_dia_anterior=float(os.sys.argv[2])
cambio_dia_hoy=float(os.sys.argv[3])

#Processing
mantenimiento_valor_cuenta_de_ahorro=(monto_principal/tipo_cambio_dia_anterior*cambio_dia_hoy-monto_principal)

if (mantenimiento_valor_cuenta_de_ahorro>0.0):
    print("el valor de la cuenta de ahorro es:",monto_principal/tipo_cambio_dia_anterior*cambio_dia_hoy-monto_principal)
