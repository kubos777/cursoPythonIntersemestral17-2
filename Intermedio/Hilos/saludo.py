import threading
#Definimos la función que realizará el hilo
def saluda(nombre):
	print("Hola",nombre)
#Creamos dos objetos de tipo Thread
hilo= threading.Thread(target=saluda,args=("Jorge",))
hilo2=threading.Thread(target=saluda,args=("Alan",))
hilo3=threading.Thread(target=saluda,args=("Ala",))
hilo4=threading.Thread(target=saluda,args=("Aln",))
hilo5=threading.Thread(target=saluda,args=("Aan",))
hilo6=threading.Thread(target=saluda,args=("lan",))
hilo7=threading.Thread(target=saluda,args=("AlanA",))

#Iniciacilazamos los hilos

hilo.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()
hilo7.start()