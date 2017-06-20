##########
# Archivos
##########

#open(rutaDelArchivo,modo) #modo por default en solo lectura

archivo=open("archivo.txt",'a+')
#Con la ruta completa
#archivo=open(r"D:\Users\cur02alu12\Desktop\Clase1Inter\archivo.txt",'r')
print("Nombre del archivo: ",archivo.name)
print("Modo de apertura: ",archivo.mode)

#Siempre recordar cerrar los archivos o flujos de datos
#archivo.close()

if archivo.closed:
	print("El archivo esta cerrado")
else:
	print("El archivo esta abierto")

#texto=archivo.read()
#print(texto)
#print(type(texto))

texto=input("Ingrese texto para escribir en el archivo: ")
archivo.write("\n"+texto)

#Mover el apuntador
archivo.seek(0) #bytes
print("Contendido del archivo:",archivo.read())

archivo.close()


#Manejador de contexto
with open(input("Ingrese el nombre del archivo: ")) as f:
	lineas=f.readlines()

print(lineas)

for linea in lineas:
	print(linea,end="")



