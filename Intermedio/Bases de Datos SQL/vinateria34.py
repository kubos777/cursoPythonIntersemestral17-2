#*-* coding: utf-8 *-*
import sqlite3, datetime #importamos la libreria
#Conectamos a la base de datos
conexion = sqlite3.connect("chelas.sqlite") #nombre de la carpteta/nombre del scritp sqlite3

#Seleccionamos el cursor para realizar la consulta
consulta = conexion.cursor()

#
sql = "SELECT * FROM bebida"

#Ejecutamos la consulta
if(consulta.execute(sql)):
	filas = consulta.fetchall()
	for fila in filas:
		print (fila[0], fila[1], fila[2], fila[3])

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexion a la base de datos
conexion.close()
