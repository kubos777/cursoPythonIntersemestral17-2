#######
#tuplas
#######

tupla=("hola",1,10,True)
tupla2=("a",10,[1,2,3])
tuplaVacia=()
singleton=(1,)

print("Tipo de dato: ",type(tupla))
print("Indexación: ",tupla[0])
print("Longitud: ",len(tupla))
print("Concatenación: ",tupla+tupla2)


#No permite porque la tupla es inmutable
#tupla[0]="Hola"

tupla2[2]=0
print(tupla2)