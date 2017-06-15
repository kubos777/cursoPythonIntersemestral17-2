class Persona3:
	#Definir los atributos
	def __init__(self,nombre,apellido,edad,estatura,dinero):
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.estatura=estatura
		self.dinero=dinero
		#Presentación de ambos objetos
		print("Hola soy",self.nombre," ",self.apellido,"y tengo ",self.edad,"años, y mido ",self.estatura)
		print("Tengo $ ",self.dinero,"pesos en mi cuenta")
	def comer(self,comida):
		print("Soy ",self.nombre," y estoy comiendo",comida, "qué rico!")
	def informarSaldo(self):
		print("Soy ",self.nombre,"y actualmente tengo $ ",self.dinero,"en mi cuenta")
##Vamos a hacer que dos objetos interactuen entre ellos
#monto: cuánto vamos a prestar
#destinatario: a quién le vamos a prestar
	def prestarDinero(self,monto,destinatario):
		self.informarSaldo()
		destinatario.informarSaldo()

		self.dinero=self.dinero-monto #Aquí le restamos la cantidad que va a prestar
		destinatario.dinero=destinatario.dinero+monto #Aquí le sumamos la cantidad a quien le prestaremos

		self.informarSaldo()
		destinatario.informarSaldo()
	#método de la clase		
	def regalarDinero(donacion,donador,beneficiado):

		donador.informarSaldo()
		beneficiado.informarSaldo()

		donador.dinero=donador.dinero-donacion
		beneficiado.dinero=beneficiado.dinero+donacion
		donador.informarSaldo()
		beneficiado.informarSaldo()


paco=Persona3("Paco","Nomeacuerdo",20,1.70,1000)
alan=Persona3("Alan","Garrido",23,1.80,200)

paco.comer("Pizza")
alan.informarSaldo()

paco.prestarDinero(500,alan)

print("*************************************")
Persona3.regalarDinero(200,alan,paco)