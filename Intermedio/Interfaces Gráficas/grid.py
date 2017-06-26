######################
# Gesturas de posicion
######################

#GRID: Crea una malla en toda la ventana para acceder como una matriz
#Con numeros para columna y fila
from tkinter import *
v=Tk()

"""
#Con grid podemos crear una malla donde todos los elementos tendrán
#El tamaño del elemento más grande
i=0
for x in range (6):
	for y in range(6):
		i+=1
		Button(v,text=str(i),borderwidth=1).grid(row=x,column=y)"""
butonI=Button(v,text="ESTOY A LA IZQUIERDA").grid(row=0,column=0)
butonD=Button(v,text="ESTOY A LA DERECHA").grid(row=0,column=1)
v.mainloop()