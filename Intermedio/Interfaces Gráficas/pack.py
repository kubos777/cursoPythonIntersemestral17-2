#############
# Gesturas de posicion
###########

#PACK: Permite ir colocando objetos en la ventana en orden descendente,
#el ancho se ajustará al mayor de estos o si se usa expand
from tkinter import *
v=Tk()
Button(v,text="Top").pack(side=TOP,fill=X,expand=YES)
Button(v,text="Centro").pack(side=TOP,fill=X,expand=NO)
Button(v,text="Final").pack(side=TOP,fill=X,expand=NO)
Button(v,text="izquierda").pack(side=LEFT)
Button(v,text="centrado").pack(side=LEFT)
Button(v,text="derecha").pack(side=LEFT)
v.mainloop()
