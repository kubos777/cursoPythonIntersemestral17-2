class Terrestre:
	def moverse(self):
		return("Soy un "+self.__class__.__name__+" y camino en la tierra")
class Animal:
	def __init__(self,patas,nombre, peso):
		self.patas=patas
		self.nombre=nombre
		self.energia=0
		self.peso=peso
	
	def comer(self):
		self.energia +=1
		print(self.energia)
	def hablar(self):
		print("Grrrrrrr!")

#Un perro es un animal y es terrestre

class Perro(Animal,Terrestre): #Dentro de la clase, va de dónde vamos a heredar
	def __init__(self,nombre,peso):
		#Super nos regresa la clase animal, llamamos al constructor de Animal
		super().__init__(4,nombre,peso)
		#Se manda a llamar cuando se mande a imprimir el objeto por medio de print
	def __str__(self):
		return str("Soy un objeto perro :3")
	def hablar(self):
		print("Guuuuau! Guuuuau!")


Lucho=Perro("Lucho",30)
Firulais=Perro("Firulais",40)


Lucho.hablar()
Lucho.comer()

print(Lucho)
print(Lucho.moverse())

