####
# copiar un archivo a otro
###

origen=open(input("Archivo origen: "),"r+")
destino=open(input("Archivo destino: "),"w")

#con ciclo for 
for linea in origen:
	destino.write(linea)

origen.seek(0)#bytes

#while 
linea=origen.readline()
while linea!="":
	destino.write(linea)
	linea=origen.readline()

origen.seek(0)#bytes

#primeros 4 caracteres
print(origen.read(4))
#primera linea
print(origen.readline())


destino.write(origen.read())


origen.close()
destino.close()


