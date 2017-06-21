#*-* coding: utf-8 *-*
import sqlite3, datetime #importamos la libreria

#Recibimos los valores que el usuario quiere almacenar
print("***********Bienvendio***********")
nombre = input("Introduzca el nombre de la bebida: ")
precio = input("Introduzca el precio de la bebida: ")

try:
	precio = float(precio) or int(precio)
except ValueError:
	print(precio, "no es un numero entero o flotante")
	exit()

#Conectamos a la base de datos
conexion = sqlite3.connect("chelas.sqlite") #nombre de la carpteta/nombre del scritp sqlite3
#Seleccionamos el cursor para realizar la consulta
consulta = conexion.cursor()
#Almacendo los datos en una tupla
argumentos = (nombre, precio, datetime.date.today()) #yyyy-mm-dd

#Creando String con la consulta SQL
sql="""
INSERT INTO bebida(nombre, precio, exportacion)
VALUES(?,?,?)
"""

if(consulta.execute(sql, argumentos)):
	print("Registro guardado exitosamente :D")
else:
	print("ERROR al guardad el registro :v")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexion a la base de datos
conexion.close()