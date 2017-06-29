from tkinter import *  

v=Tk()
v.configure(background="#a1dbcd")
v.title("Incicia Sesion")
v.wm_iconbitmap("db.ico")
v.geometry('300x650+20+10') 

v2=Toplevel(v)
v2.withdraw()
v2.title("Bienvenido")
msg = Message(v2, text="Haz iniciado sesion!")
msg.pack()

bt2 = Button(v2, text="Aceptar", command=v2.destroy)
bt2.pack()

foto=PhotoImage(file="python.png")
lb=Label(v,image=foto)
lb.pack()

lb2=Label(v,text="Loguearse para continuar:",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
lb2.pack()

lb3=Label(v,text="Usuario",fg="#383a39",bg="#a1dbcd",relief=RAISED)
en3=Entry(v)
lb3.pack()
en3.pack()

lb4=Label(v,text="Contraseña",fg="#383a39",bg="#a1dbcd",relief=RAISED)
en4=Entry(v,show="*")
lb4.pack()
en4.pack()

bt1=Button(v,text="Login",bg="#383a39",fg="#a1dbcd",command=  lambda: [f() for f in [v.withdraw,v2.deiconify]])
bt1.pack()

v.mainloop()