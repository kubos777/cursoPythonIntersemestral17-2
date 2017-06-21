################
# Expresiones 2
################

import re

#SEARCH
texto="En este texto se encuentra la palabra mágica"

#re.search(regex,texto) regresa las posiciones

encontrado=re.search("mágica",texto)


print("Posición inicial: ",encontrado.start())
print("Posición final: ",encontrado.end())
print("En conjunto: ",encontrado.span())
print(texto[38:44])

#MATCH
texto="Hoola mundo"

#re.match(regex,texto) si hace match regresa un objeto de tipo match y si no regresa None

encontrado=re.match("Ho{0,1}la",texto)
if encontrado:
	print("Hizo coincidencia")
else:
	print("No  hay coincidencia")


#SPLIT

texto="vamos a dividir esta cadena"

#re.match(regex,texto) regresa una lista sin el caracter (patron)

encontrado=re.split(" ",texto)
#encontrado=re.split("a",texto)
print(encontrado)
print("".join(encontrado))

#Metacaracteres (Cuantificadores)
# . cualquier caracter
# + una o más veces
# * cero o más veces 
# ? puede o no estar 0 o 1 vez
# {n} n = numero de veces exactas
# {n,m} n=minimo de veces, m=maximo de veces

#Metacaracter .

texto="ola ala ula pla alo ilo"
patrones=[".la",".lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

#Metacaracter *

texto="hla hola hoola hoola hooooooooooola hulo huuuulo"
patrones=["ho*la","hu*lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

#Metacaracter +

texto="hla hola hoola hoola hooooooooooola hulo huuuulo"
patrones=["ho+la","ho+lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

#Metacaracter ?

texto="hla hola hoola hoola hooooooooooola hlo holo"
patrones=["ho?la","ho?lo"]

def buscar(patrones,texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)






