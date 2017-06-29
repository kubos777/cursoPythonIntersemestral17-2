##############
# Archivos csv
##############

import csv

with open("archCSV.csv","r") as f:
	reader= csv.reader(f)
	for linea in reader:
		print(linea)


f=open("archCSV.csv","r")
reader= csv.reader(f)

filas=0
for linea in reader:
	if filas==0:
		header=linea
	else:
		columnas=0
		for dato in linea:
			print("Fila: %d, columna: %d, Contenido:%s"%(filas,columnas,dato))
	filas+=1

	

