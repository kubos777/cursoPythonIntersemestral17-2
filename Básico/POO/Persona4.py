class Persona4:
	def __init__(self,nombre2,apellido2,edad2,estatura2,dinero2):
		self.nombre=nombre2
		self.apellido=apellido2
		self.edad=edad2
		self.estatura=estatura2
		self.dinero=dinero2

	@classmethod
	def vivir(clase):
		print("Soy una ",clase,"y estoy vivo!")

	@staticmethod
	def respirar():
		print("respirar")

	def comer(self):
		print("comer")


alan=Persona4("alan","garrido",23,1.80,200)

#Metodo de clase
Persona4.vivir()


#Metodo estatico
Persona4.respirar()
alan.respirar()

#Metodo 
Persona4.comer(alan)
alan.comer()