diccionario={1:"Opcion 1",2:"Opcion 2", 3:"Opcion 3"}

lista=list(diccionario.keys())
lista.sort()
print(lista)

while True:
	for llave in lista:
		print("\t%s. %s"%(llave,diccionario[llave]))
	seleccion=int(input("Selecciona una opcion: "))
	if seleccion in lista:
		print("Seleccionaste la: ",diccionario[seleccion])
	elif seleccion == 0:
		print("Adios!")
		break
	else:
		print("Opción inválida")
		
