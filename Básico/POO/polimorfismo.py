class Animal:

	def __init__(self,nombre):
		self.nombre=nombre

	#metodo abstracto
	def hablar(self):
		raise NotImplementedError("Debes implementar antes!!")


class Perro(Animal):
	def hablar(self):
		return "Guauuu!!!"


class Gato(Animal):
	def hablar(self):
		return "Miaaauu!!!"


animales=[Gato("Gatosan"),
		  Perro("Max"),
		  Gato("Bigotes")]

for animal in animales:
	print(animal.nombre+" dice "+animal.hablar())


a=Animal("fantasma")
a.hablar()