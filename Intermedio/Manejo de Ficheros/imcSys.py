import sys
print(len(sys.argv))
if len(sys.argv)<=2:
	print("Te faltan parametros")
	exit(-1)

while True:
	peso=float(sys.argv[1])
	altura=float(sys.argv[2])
	IMC=peso/altura**2
	if IMC<18:
		print("Infrapeso")
	elif IMC<24.9:
		print("Chido!")
	else:
		print("Bajale a los tamales")
	res=input("Escribe 'salir' para terminar")
	if res=='salir':
		break