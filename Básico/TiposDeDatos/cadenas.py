#########
# Cadenas
#########


cadena="hola"
cadena2=' mundo'
cadenaLarga="""Esta es una
cadena
con 
saltos de 
linea"""
cadenaVacia=""
cadenaCruda=r"hola\n\r\t"

#print(cadena)
#print(cadenaCruda)
print("Tipo de dato: ",type(cadena))
print("Indexación: ",cadena[0])
#Se pueden usar indices negativos
print("Indexación: ",cadena[-2])
print("Tamaño: ",len(cadena))
print("Concatenacion: ",cadena+cadena2)
print("Repetición: ",cadena*3)
#Asignacion no esta permitida porque son inmutables
#cadena[0]="H"
#Pueden ser opcionales
print("Slicing: ",cadena[1:3])
