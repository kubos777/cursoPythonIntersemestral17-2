#*-* coding: utf-8 *-*
import sqlite3, datetime #importamos la libreria
#Conectamos a la base de datos
conexion = sqlite3.connect("chelas.sqlite") #nombre de la carpteta/nombre del scritp sqlite3

#Seleccionamos el cursor para realizar la consulta
consulta = conexion.cursor()

# Definimos nuestra consulta con la observacion de cuidar las "" en la query
sql = "UPDATE bebida SET nombre = 'Jack' WHERE id_bebida= %s" %2

#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Registro modificado con exito :D")
else:
	print("ERROR al hacer la modificacion :v")

#Definimos nuestra consulta de borrar un registro
sql = "DELETE FROM bebida WHERE id_bebida = %s" %3
#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Registro borrado con exito :D")
else:
	print("ERROR al hacer la eliminacion :v")


#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexion a la base de datos
conexion.close()
