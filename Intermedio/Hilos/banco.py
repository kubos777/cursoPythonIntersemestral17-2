########################
####Exclusión Mutua#####
########################

import threading #Importamos el modulo threading
import time

class Cuenta: #Creamos la clase Cuenta
	def __init__(self, saldo):
		self.saldo=saldo
		self.candado=threading.Lock() #Definimos un candado, con ayuda del método Lock

	#Definimos el método retirar
	def retirar(self,cantidad):
		self.candado.acquire() #El método acquire nos permite bloquear al hilo
		if self.saldo>0:
			time.sleep(1)
			print("Se hizó un retiro! ")
			self.saldo=self.saldo-cantidad
			print("Su saldo actual es: ",self.saldo)
		self.candado.release() #El método release nos permite liberar al hilo
#Creamos un objeto de tipo cuenta
c=Cuenta(300)

h=[] #Creamos una lista para meter los hilos

for i in range(100):	
	h.append(threading.Thread(target=c.retirar,args=(20,)))
for hilito in h:
	hilito.start() #Inicializamos todos los hilos de la lista