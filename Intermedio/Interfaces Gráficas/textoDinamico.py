################
# Label dinamico
################

from tkinter import * 

contador=0
def incrementar(label):
	#Esta funcion manda a llamar contar y le pasa el label
	def contar():
		global contador
		contador+=1
		label.config(text=str(contador))
		#la funcion after llama a un callback despues de un tiempo determinado en milisegundos
		#after(delay_ms, callback=None, *args)
		#llama a contar cada segundo
		label.after(100,contar)
		if contador==100:
			#reiniciamos el contador 
			contador=0
	contar()


v=Tk()
v.title("Cuenta hasta 100")
lb1=Label(v,fg="green",width=40,height=2)
lb1.pack()
incrementar(lb1)
b1=Button(v,text="salir",width=25,command=v.destroy)
b1.pack()
v.mainloop()