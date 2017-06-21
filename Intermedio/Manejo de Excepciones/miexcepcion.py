#Así declaramos una excepción propia
class Miexcepcion(Exception):
	pass

try:
	x=1.7172
	if isinstance(x,float):
		#raise va a obligar a que ocurra una excepció, en esta caso nuestra excepción
		raise Miexcepcion
##Levantamos nuestra propia excepción
except Miexcepcion:
	print("No es un entero")