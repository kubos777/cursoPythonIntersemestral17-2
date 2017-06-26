#########
# Linkbox
########


from tkinter import *
import webbrowser

ventana= Tk()
def linkCallback():
	#Aqui abrimos un navegador para acceder a la pag dicha
	#(r"blabla./n") es una cadena cruda y omite los caracteres especiales
	webbrowser.open_new(r"http://www.google.com")

#fg cambia el color del texto
link= Button(ventana,text="google",fg="red",cursor="hand2",command=linkCallback)
link.pack()
ventana.mainloop()
