#####################
# Formatos en tkinter
#####################


from tkinter import *

ventana=Tk()
ventana.title("Tamaños, colores y fuentes")


Label(ventana, text="Rojo en fuente Times",
			   fg="red",
			   font="Times"
	).pack()

Label(ventana, text="Verde en fuente Helvetica en negritas",
			   fg="light green",
			   bg="dark green",
			   font="Helvetica 16 bold"
	).pack()

Label(ventana, text="Azul en fuente Verdana en cursiva",
			   fg="blue",
			   bg="yellow",
			   font="Verdana 10 italic"
	).pack()

#ventana.geometry("200x200")
ventana.mainloop()