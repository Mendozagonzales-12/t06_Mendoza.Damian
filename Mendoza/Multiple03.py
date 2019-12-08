#Programa para que calcule el IMC
#Declaracion
peso=0.0
altura=0.0
import os

#Input
peso=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#Processing
imc=peso/altura**2
#si el imc<=18.0 su peso es bajo
if (imc<=18.09):
    print ("Peso demasiado bajo")
#si el imc<=24.9 su peso es normal felicidades
elif (imc<=24.9):
    print ("Su peso es normal felicidades")
#si el imc<=29.9 su peso es sobrepeso,vigile su dieta
elif (imc<=29.9):
    print ("Tiene sobrepeso, vigile su dieta")
#si el imc>29.9 su peso es obesidad grave
elif (imc>29.9):
    print ("Obesidad grave, consulte su médico")
