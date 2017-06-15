###########
# Funciones
###########

def suma(a,b):
	"""Docstring"""
	return a+b

a , b = 2 , 4
print(suma(a,b))
print(suma(3.4,6))
#Keyword argument
print(suma(10,b=20))

def suma2(a=0,b=0):
	return a+b

print("Parametros por default")
print(suma2())
print(suma2(a,b))

def suma3(*variables):
	acum=0
	for numero in variables:
		acum+=numero
	return acum

print("Parametros variables")
print(suma3())
print(suma3(1,2))
print(suma3(1,2,3))
print(suma3(1,2,3,4,5,6))


def suma4(a=0,b=0,**llaveValor):
	if llaveValor is not None:
		for llave,valor in llaveValor.items():
			print("Llave: ",llave,"Valor: ",valor)
	else:
		return a+b

print(suma4())
print(suma4(1))
print(suma4(1,3))
print(suma4(nombre="alan"))
print(suma4(nombre="alan",apellido="garrido",semestre=10))











