###########
#Ciclo for (for in)
#########

lista=[1,2,3,4,5]

#for i in lista:
	#print(i)


#tup=("uno",1,1.0,1+1j,[1,1,1])
#for val in tup:
#	print(val)

#for j in range(5,0,-1):
#	print(j)

a=1
b=-5 
if a>5 or b>0:
	print(a,b)
else:
	if a>0 and b>(-10):
		print(a,b)
#Lo mismo pero mas resumido
if a!=5 or b>0:
	print(a,b)
elif a>0 and b>(-10):
	print("Los mucho menores ahora")




for i in range(1,10):
	if(i == 7):
		print(i)
		break
	else:
		print("Este no es el que buscas")
	print("Pero sigue intentando")
