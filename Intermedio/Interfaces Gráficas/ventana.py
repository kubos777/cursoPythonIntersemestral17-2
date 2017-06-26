from tkinter import * 

ventana=Tk()
ventana.title("Mi primer ventana")
etiqueta=Label(ventana,text="Hola a todos :D")
etiqueta.pack()
boton=Button(ventana,text="Minimizar",command=ventana.iconify)
boton.pack()
boton1=Button(ventana,text="Salir",command=quit)
boton1.pack()
ventana.mainloop()