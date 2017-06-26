##########
# ListBox
##########

from tkinter import *

ventana=Tk()

lab1=Listbox(ventana)
lab1.insert(1,"Python")
lab1.insert(2,"Java")
lab1.insert(3,"C++")
lab1.insert(4,"Haskell")
lab1.pack()

ventana.mainloop()
