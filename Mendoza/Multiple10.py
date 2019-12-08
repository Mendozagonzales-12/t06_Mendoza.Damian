#Programa que
#Muestre la categoría a la que pertenece el signo del zodíaco seleccionado.
#Nota: Si el signo introducido por el usuario, no está asociado a ningún signo del zodíaco
#Declaracion
signo=""
import os

#Input
signo=str(os.sys.argv[1])

#Processing
#si el signo es ARIES, LEO O SANGITARIO pertenece a la categoria FUEGO
if (signo=="ARIES" or signo=="LEO" or signo=="SAGITARIO"):
    print(signo,"pertenece a la categoria FUEGO")
#si el signo es TAURO, VIRGO O CAPRICORNIO pertenece a la categoria TIERRA
if (signo=="TAURO" or signo=="VIRGO" or signo=="CAPRICORNIO"):
    print(signo,"pertenece a la categoria TIERRA")
#si el signo es GEMINIS, LIBRA O ACUARIO pertenece a la categoria AIRE
if (signo=="GEMINIS" or signo=="LIBRA" or signo=="ACUARIO"):
    print(signo,"pertenece a la categoria AIRE")
#si el signo es CANCER, ESCORPIO O PISCIS pertenece a la categoria AGUA
if (signo=="CANCER" or signo=="ESCORPIO" or signo=="PISCIS"):
    print(signo,"pertenece a la categoria AGUA")
