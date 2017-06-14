#######
#Listas
#######


lista=["hola",4,10.4,True]
lista2=["a",10,[1,2,3]]
listaVacia=[]

print("Tipo de dato: ",type(lista))
print("Indexación: ",lista[0])
print("Longitud: ",len(lista))
print("Concatenación: ",lista+lista2)

lista[0]="Hola"
print(lista[0])
print("Búsqueda: ", 3 in lista2)
#sublista
print("Elemento en sublista: ",lista2[2][1])

for elemento in lista:
	print("Elemento: ",elemento)

print("Slicing: ",lista[1:3])
print("Slicing: ",lista[ 1: :2])
print("Slicing: ",lista[ : :-1])

#Operaciones
lista=["A","B","C","D"]
lista.append("E")
print(lista)
lista.insert(0,"Z")
print(lista)
uiltimoElemento=lista.pop()
print(uiltimoElemento)
print(lista)
#Eliminacion del elemento
del lista[0]
print(lista)
lista2=[3,4,1,5,8,2]
print("Máximo: ",max(lista2))
print("Mínimo: ",min(lista2))
#Ordenamiento
lista2.sort()
print("Lista ordenada: ",lista2)
lista2.reverse()
print("Lista en orden inverso: ",lista2)
#indice de un elemento
print("Indice de B: ",lista.index("B"))

