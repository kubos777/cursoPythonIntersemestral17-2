######
#Recursion
######
def factorial(num):
	if num<1:
		return 1
	else:
		return num*factorial(num-1)

#print(factorial(5))

#####
# Iteracion
#####
def factorial2(num):
	fack=1
	for i in range(2,num+1):
		fack*=i
	return fack

#print(factorial2(5))


######
#Map
#####

items = list(range(1,11))
print(items)

cuadrados=[]

cuadrados= list(map(lambda x: x ** 2, items))

print(cuadrados)