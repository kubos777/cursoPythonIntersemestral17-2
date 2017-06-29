import csv

with open('datos.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
       # print(row[0])
       # print(row[0],row[1],row[2],)

with open('datos.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    fechas = []
    colores = []
    for row in readCSV:
        color = row[3]
        fecha = row[0]

        fechas.append(fecha)
        colores.append(color)

print(fechas)
print(colores)

import csv
with open('directorio.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row['Nombre'],"->",row['Correo'])  # Accesar por el nombre de la columna en vez de un numero
