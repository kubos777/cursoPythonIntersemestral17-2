##Problema del diamante
###
class A:
	def a(self):
		print("A")

class B(A):
	def a(self):
		print("B")

class C(A):
	def a(self):
		print("C")

class D(C,B):
	def preguntaPorA(self):
		self.a()

objD=D()
objD.preguntaPorA()

print(D.__mro__)