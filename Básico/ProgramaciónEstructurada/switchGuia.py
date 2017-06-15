#-*-coding:utf-8-*-
import os
#Con esto limpiamos la pantalla
#cls es para windows y clear es para linux o mac
os.system("cls")
#Declaramos un diccionario vacío para guardar los contactos
contactos={}
print("\n\n\t\t\t\t\t\t\t\t\tBienvenido a la Super Agenda")

while True:
	print("Selecciona la opción que deseas realizar: ")
	print("\n\t1.-Agregar un contacto.")
	print("\n\t2.-Buscar un número.")
	print("\n\t3.-Ver todos los contactos.")
	print("\n\t4.-Eliminar contacto.")
	print("\n\t5.-Salir.")

	opcionMenu=int(input("Opción: "))
	if opcionMenu==1:
		#Agregar contacto
		nombre=input("\n\n\t Ingresa el nombre del contacto: ")
		numero=int(input("Ingresa el número de teléfono: "))
		contactos[nombre]=numero
		os.system("cls")
	elif opcionMenu==2:
		#Buscar un numero
		nombre=input("¿Qué contacto deseas buscar?: ")
		os.system("cls")
		if nombre in contactos:
			print("\n Nombre: ",nombre)
			print("\nTeléfono: ",contactos[nombre])
		else:
			print("\nError 404, contacto no encontrado")
	elif opcionMenu ==3:
		#Mostrar todos los contactos
		os.system("cls")
		if len(contactos.items())==0:
			print("\n\n\t No hay contactos para mostrar!")
		else:
			for persona in contactos.keys():
				print("\n\n\tEl numero de ",persona," es: ",contactos[persona])
	elif opcionMenu==4:
		#Eliminar contacto
		nombre=input("¿Qué contacto deseas borrar?: ")
		os.system("cls")
		if nombre in contactos:
			del contactos[nombre]
		else:
			print("\nError 404, contacto no encontrado")
	elif opcionMenu==5:
		#Para salir
		os.system("cls")
		print("\n\n\tHasta luego!")
		break
	else:
		os.system("cls")
		print("\n\n\tOpción no válida, intenta otra vez!")



	