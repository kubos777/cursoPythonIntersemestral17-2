import random
##Creamos dos excepciones
class ValorMuyBajo(Exception):
	pass
class ValorMuyAlto(Exception):
	pass
y=0
x=random.randint(1,30)
#print(x)
while True:
	try:
		a=int(input("Ingresa un entero: "))
		y+=1
		if y==5:
			print("Perdiste :c")
			break
		elif a>x:
			raise ValorMuyAlto
		elif a<x:
			raise ValorMuyBajo
		if a==x:
			print("Ganaste! ")
			break
	except ValorMuyBajo:
		print("Valor muy bajo!")
	except ValorMuyAlto:
		print("ValorMuyAlto")
	except:
		print("Fue otro error!")