#################
# Cuenta palabras
#################
import sys

nombreArch=sys.argv[1]

f=open(nombreArch,"r")

totalP=0
totalC=0

for linea in f.readlines():
	totalP+=len(linea.split())
	#totalP=totalP+len(linea.split())
	for palabra in linea:
		totalC+=len(palabra.strip())

print("La cantidad de palabras es: ",totalP)	
print("La cantidad de caracteres es: ",totalC)	


f.seek(0)
totalS=0

cadenas=f.read()
print(str(cadenas).split())
lista=cadenas.split()

for palabra in lista:
	totalS += len(palabra)

print("La cantidad de palabras es: ",len(lista))
print("La cantidad de caracteres es: ",totalS)




