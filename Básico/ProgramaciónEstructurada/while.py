a=0
b=int(input("Ingresa el numero que deseas saber su tabla de multiplicar"))

while a<=10:
	print(("%d * %d = %d")%(a,b,a*b))
	a=a+1 #a+=1
print("Se termino el ciclo :(")

###While con break y continue


a=0

while a<10:
	a=a+1
	if a==2:  #Se salta la iteración del numero 2
		continue
	elif a==5:  #Ya no llegó al 5, se quedó en el 4
		break
	print(a)
print("Se termino el segundo ciclo :c")


#######Do while :
a=0

while True:
	print("Esto se imprime una vez") #Parte del DO
	a=int(input("Escribe un cero para salir del ciclo: "))
	if a==0:  #PARTE DEL WHILE
		break

print("Se terminó")
	