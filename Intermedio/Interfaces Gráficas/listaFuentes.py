####################
# Fuentes en Tkinter
####################

# Este programa les muestra una tabla con las fuentes que se pueden usar en tkinter para un text
# programa tomado de from https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
# Recordar que se pueden configurar así: text.tag_config("azul",background="blue",font=('Helvetica', 12))

from tkinter import *
from tkinter import font

ventana = Tk()
ventana.title("Fuentes Disponibles")
ventana.geometry("300x200")
#Obtenemos una lista de fuentes
fonts=list(font.families())
fonts.sort()
#Y las desplegamos en un listbox
display = Listbox(ventana)
display.pack(fill=BOTH, expand=YES, side=LEFT)
#Agregamos un scroll a la ventana
scroll = Scrollbar(ventana)
scroll.pack(side=RIGHT, fill=Y, expand=NO)
#Y lo configuramos
scroll.configure(command=display.yview)
display.configure(yscrollcommand=scroll.set)
#Agregamos cada una de las fuentes al listbox
for item in fonts:
    display.insert(END, item)

ventana.mainloop()