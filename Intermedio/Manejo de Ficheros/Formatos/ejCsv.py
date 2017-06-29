import csv

with open("ejemplo.csv","r") as f:
	reader = csv.reader(f)
	for linea in reader:
		print(linea)


infile=open("ejemplo.csv")
reader=csv.reader(infile)

filas=0
for linea in reader:
	if filas==0:
		header=linea
	else:
		columnas=0
		for columna in linea:
			print("Fila= %d , columna= %d, Contenido=%s"%(filas,columnas,columna))
			columnas+=1
	filas+=1
infile.close()


infile=open("ejemplo.csv")
outfile=open("copia.csv","w")

reader=csv.reader(infile)
writer=csv.writer(outfile,delimiter="|",quoting=csv.QUOTE_ALL)
#csv.QUOTE_MINIMAL a las que tiene caracteres especiales
#csv.QUOTE_NONNUMERIC solo a cadenas
#csv.QUOTE_NONE nada (default)


for linea in reader:
	writer.writerow(linea)

infile.close()
outfile.close()















