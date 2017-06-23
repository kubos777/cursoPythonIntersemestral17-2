import threading
import time
x=0
#
class Resta(threading.Thread):
	#Sobreescribir el método run:
	def run(self):
		#Variable local,solamente vive dentro de la función o método
		#Variable global, vive en todo el código
		global x 
		while x>0:
			x=x-1 #x-=1
			print("-: ",x)
			time.sleep(.5)
class Suma(threading.Thread):
	def run(self):
		global x
		while x<50:
			x=x+3 #x+=3
			print("+: ",x)
			time.sleep(.5)

s= Suma()
r= Resta()

s.start()
r.start()
#El método join nos ayuda a hacer que un hilo espere a que otro termine
s.join()
r.join()


