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
ventana.mainloop()