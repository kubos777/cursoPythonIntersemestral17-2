###########
# Modulo os
###########

import os
#Conocer el nombre del sistema o entorno en el que corre python
print("Nombre del sistema operativo: ",os.name)
#Invocar un comando externo
#os.system("dir")
#Saber el directorio acutual
print("directorio acutual:",os.getcwd()) # en linux seria como pwd
#caracteristicas del sistema
#print(os.uname())
#Listar un directorio
print(os.listdir("."))
#Borrar un directorio
os.rmdir("Nueva Carpeta") #Causa un error si no hay un carpeta llamada asi

# Crear una directorio
os.mkdir("Nueva Carpeta") #Causa un error si existe una llamada asi

# Cambiarnos de directorio
os.chdir("Nueva Carpeta")
print("directorio acutual:",os.getcwd()) # en linux seria como pwd

os.chdir("..")
#os.rename(src,dst)
os.rename("Nueva Carpeta","Carpeta Renombrada") 
print(os.listdir("."))
#os.rmdir("Carpeta Renombrada") #Causa un error si no hay un carpeta llamada asi



