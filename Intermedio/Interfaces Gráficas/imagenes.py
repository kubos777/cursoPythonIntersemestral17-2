##################
# Imagenes tkinter
##################

from tkinter import *
ventana=Tk()
logo=PhotoImage(file="python.png")
lbl1=Label(ventana,image=logo).pack(side="right")
texto="""Para utilizar imagenes con python, se deben
utilizar los formatos PNG o GIF, o utilizar el modulo
PIL para otros formatos.
"""
lbl2=Label(ventana,justify=LEFT,padx=10,text=texto).pack(side="left")
#Para que el texto y la imagen se cargen en el mismo lugar
#Descomentar lb3 y comentar lb1 y lb2
#lb3=Label(ventana,text=texto,compound=CENTER,padx=10,image=logo).pack(side="left")
ventana.mainloop()