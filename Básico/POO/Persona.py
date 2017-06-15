#####Primer ejemplo de POO

class Persona:
	#Atributos
	edad=21
	saludo="Hola amigos"
	#Este es un método de la clase Persona
	def saludar(self):
		print("%s soy una Persona"%self.saludo)

	def unaFuncion():
		print("Esto es una función de clase")

#Instancia o creación de un objeto a partir de una clase
jorge=Persona()

print(jorge.edad)
print(jorge.saludo)

jorge.saludar()

Persona.unaFuncion()

print(Persona.edad)

