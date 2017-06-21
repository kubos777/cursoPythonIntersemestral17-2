#*-* coding: utf-8 *-*
import sqlite3 #importamos la libreria

#Conectamos a la base de datos
conexion = sqlite3.connect("chelas.sqlite") #nombre de la carpteta/nombre del scritp sqlite3

#El acceso a base de datos se define de modo estandar en las especificaciones DB-API (PEP 249)

#Seleccionamos el cursor para realizar la consulta
consulta = conexion.cursor()

#Creando un String con la consulta SQL
sql = """
CREATE TABLE IF NOT EXISTS bebida(
id_bebida INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre VARCHAR(50) NOT NULL,
precio FLOAT NOT NULL,
exportacion DATE NOT NULL
)"""

#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Tabla creada con exito :D")
else:
	print("ERROR al crear la tabla :v")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexion a la base de datos
conexion.close()