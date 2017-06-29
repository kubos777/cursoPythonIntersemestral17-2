palabra=input("Ingresa la palabra a buscar: ")
f=open("texto","r")

texto=f.read()
palabras=texto.split()
print(palabras)

if palabra in palabras:
	print("La palabra se encuentra ",palabras.count(palabra), " veces")
else:
	print("La palabra no se encuentra ")