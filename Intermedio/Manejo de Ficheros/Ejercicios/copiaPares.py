####
# copia pares
####

destino=open(input("Archivo destino: "),"r+")

i=0
with open(input("Archivo origen: ")) as f:
	for linea in f.readlines():
		if i%2==0:
			destino.write(linea)
		i+=1

destino.seek(0)
lista=destino.readlines()
ultima=lista[-1]
print(ultima)