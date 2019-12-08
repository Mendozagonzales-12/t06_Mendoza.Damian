#Programa para indicar si un caracter es vocal
#Declaracion
letra=""
import os

#Input
letra=str(os.sys.argv[1])

#Processing
#si no es vocal indicarlo como mensaje
if (letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u'):
    print ("Es una vocal")
else:
    print("no es vocal")
