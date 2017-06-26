############
# Combobox
############

from tkinter import *
#Extras para tkinter
from tkinter import ttk

ventana= Tk()

combo=ttk.Combobox(ventana)
combo.pack()
#Se agregan los valores que se desplegaran
combo["values"]=("Mexico","Venezuela","Nicaragua","Ecuador","Argentina")

ventana.mainloop()