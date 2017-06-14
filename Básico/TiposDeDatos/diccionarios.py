#############
#Diccionarios
#############

diccionario={"a":0,"b":1,"c":2,"d":True,"e":[1,2,3]}
print(diccionario["a"])
print(diccionario["b"])
print(diccionario["d"])
print(diccionario["e"])

#Se pueden usar como llave de un diccionario int,str y tuple
diccionario2={(1,2,3):"a"}

calificaciones={"alan":10,"coral":6,"jorge":5,"francisco":7}
print("Calificacion de Alan: ",calificaciones["alan"])
print("Calificacion de Alan: ",calificaciones.get("alan"))
#print("Calificacion de Luis: ",calificaciones["luis"])
print("Calificacion de Luis: ",calificaciones.get("luis"))
#Valor por default
print("Calificacion de Luis: ",calificaciones.get("luis",0))
#Modificar un valor
calificaciones["coral"]=8
print(calificaciones["coral"])
#Crear un valor
calificaciones["luis"]=8
print(calificaciones["luis"])

print(calificaciones)

for persona in calificaciones.keys():
	print("Calificacion de ",persona,"es",calificaciones[persona])

print(calificaciones.values())
print(calificaciones.items())
