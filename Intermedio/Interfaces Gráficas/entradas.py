###################
# Entradas de datos
###################

from tkinter import *

#Con esta funcion obtendremos los datos de los campos y los impriremos en la terminal
def mostrarCampos():
   print("Nombre: %s\nApellido: %s" % (e1.get(), e2.get()))
   #Si quieren borrar los campos después de imprimir basta con usar la funcion delete
   e1.delete(0,END)
   e2.delete(0,END)
#Creamos la ventana
ventana = Tk()
#Colocamos dos etiquetas con el método grid
Label(ventana, text="Nombre").grid(row=0)
Label(ventana, text="Apellido").grid(row=1)
#Y colocamos dos entradas de datos
e1 = Entry(ventana)
e2 = Entry(ventana)
#Podemos colocar estos valores por default
e1.insert(10,"Alan")
e2.insert(10,"Garrido")
#Y ahora las ponemos en la ventana con el metodo grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#También colocaremos dos botones, uno para salir y el otro para mostrar los valores de los campos
Button(ventana, text='Quit', command=ventana.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(ventana, text='Show', command=mostrarCampos).grid(row=3, column=1, sticky=W, pady=4)
#Recordar siempre colocar esta funcion para generar el loop de la interfaz
mainloop( )