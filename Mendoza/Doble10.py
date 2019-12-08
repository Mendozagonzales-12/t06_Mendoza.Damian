#Programa que permita al usuario elegir un candidato por el cual votar.
#Las posibilidades son:
#candidato A por el partido rojo
#candidato B por el partido verde
#candidato C por el partido azul.
#Declaracion
candidato=""
import os

#Input
candidato=float(os.sys.argv[1])

#Processing
#Según el candidato elegido (A, B ó C)
#se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”.
if candidato.upper()=="A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper()=="B":
    print("Usted ha votado por el partido verde")
elif candidato.upper()=="C":
    print("Usted ha votado por el partido azul")
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
else:
    print("Opción errónea")

