########
#Botones
########

from tkinter import *
from tkinter import messagebox

#Son objetos de una interfaz gráfica que nos pueden ayudar a realizar acciones las cuales corresponden
#a una función de python, llamadas callbacks de ese boton

v=Tk()

def alertaCallback():
	#hay diferentes tipos de messagebox
	msg=messagebox.showinfo("Alerta","Este es un mensaje de alerta")

def textCallback():
	#Aquí se debe de declarar otra ventana (toplevel)
	v=Toplevel()
	#Y hacerla hija de la ventana original
	text=Text(v)
	#Insercion de datos
	text.insert(INSERT,"Hola desde ...")
	text.insert(END,"Aqui :v")
	text.pack()

	text.tag_add("amarillo","1.0","1.4")
	text.tag_add("azul","1.8","1.13")

	text.tag_config("amarillo",background="yellow",foreground="red")
	text.tag_config("azul",background="blue",font=('Helvetica', 12),foreground="red")

def msgCallback():
	v=Toplevel()
	#En las interfaces gráficas no se pueden usar los tipos int y str
	#que usamos normalmente en los strings, debemos usar las clases
	#IntVar() o StringVar, para poder actualizar los valores
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