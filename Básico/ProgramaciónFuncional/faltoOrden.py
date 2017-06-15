########################
#Funciones de alto orden
########################


#####
# MAP
#####

items = list(range(1,11))
print(items)

cuadrados=[]

def cuadrado(x):
	return x**2

cuadrados= list(map(cuadrado, items))

print(cuadrados)

cubos= list(map(lambda x:x**3,items))

print(cubos)

########
# Filter
########

multiplos4= list(filter(lambda n:n%4==0,items))

print(multiplos4)

#######
#Reduce
#######
import functools
res=functools.reduce(lambda a,b:a+b,items)
print(res)



########
# Lambda
########


#lambda parametros:Funciones

#def f(a,b):
#	return a+b

f=lambda a,b:a+b

print("Resultado",f(1,1))