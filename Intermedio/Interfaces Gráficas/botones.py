##########
#Botones
##########

from tkinter import *
from tkinter import messagebox

v=Tk()
def alertaCallback():
	msg=messagebox.showinfo("Alerta","Este es un mensaje de alerta")

def textCallback():
	v=Toplevel()
	text=Text(v)
	#Insercion de datos
	text.insert(INSERT,"Hola desde ...")
	text.insert(END,"Aqui :v")
	text.pack()

	text.tag_add("amarillo","1.0","1.4")
	text.tag_add("azul","1.8","1.13")

	text.tag_config("amarillo",background="yellow",foreground="red")
	text.tag_config("azul",background="blue",foreground="red")

def msgCallback():
	v=Toplevel()
	#IntVar(), diferentes a String y a Int respectivamente
	var=StringVar()
	label=Message(v,textvariable=var,relief=RAISED)
	#modifica a la variable var
	var.set("Hola, como estan?")
	label.pack()


b1=Button(v,text="Alerta",command=alertaCallback)
b1.place(x=50,y=50)

b2=Button(v,text="Texto",command=textCallback)
b2.place(x=50,y=100)

b3=Button(v,text="Mensaje",command=msgCallback)
b3.place(x=50,y=150)

v.mainloop()