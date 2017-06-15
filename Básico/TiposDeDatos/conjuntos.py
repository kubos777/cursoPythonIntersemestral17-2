###########
#Conjuntos
###########

conjunto={1,2,3,4,5,10}

print("Tipo de dato",type(conjunto))
print(conjunto)

conjunto2= set([1,2,2,3,3,4,5,6,9])
print(conjunto2)
#Todos los tipos inmutables
conjunto3= {True,3,40.2,"hola"}
print(conjunto3)
conjunto3.add(False)
print(conjunto3)

#No soporta indexacion
#print("Indexación: ",conjunto[0])
print("Tamaño: ",len(conjunto))
#No esta definida
#print("Concatenacion: ",conjunto+conjunto2)
#Tampoco soporta esta operacion
#print("Repetición: ",conjunto*3)

#Operaciones
print("Diferencia: ",conjunto-conjunto2)
print("Diferencia simetrica",conjunto^conjunto2)
print("Union: ",conjunto|conjunto2)
print("Intersección: ",conjunto&conjunto2)


############
# Frozensets
############

conjuntoF= frozenset([True,3,40.2,"hola"])
print(conjuntoF)
#No permitido
conjuntoF.add(False)
print(conjuntoF)