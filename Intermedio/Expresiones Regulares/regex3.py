################
# Ejemplos regex
################

import re

celular=input("Dame tu numero celular: ")

patron="55[0-9]{8}"

valido=re.match(patron,celular)
if valido:
	print("Celular válido para CDMX")
else:
	print("Favor de verificar")

entero=input("Dame un entero: ")
patron="\d+" #Mejorar para no aceptar valores booleanos o usar ^

valido=re.match(patron,entero)
if valido:
	print("Ok si es un entero")
	entero=int(entero)
else: 
	print("No te creo ")






