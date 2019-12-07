#Programa que pida al usuario dos números y devuelva su división.
#Si el usuario no introduce números debe devolver un aviso de error.
#Declaracion
n,m=0.0,0.0
import os

#Input
n= float(os.sys.argv[1])
m = float(os.sys.argv[2])

#Processing
#En caso contrario debe mostrar el resultado
if (m==0):
    print("¡ERROR!,No se puede dividir por 0.")
else:
    print("El resultado es:",n/m)
