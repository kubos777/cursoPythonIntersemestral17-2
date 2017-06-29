#######
# Numpy
########

#Numpy es la biblioteca principal para la computación científica en Python. 
#Proporciona un objetos tipo matriz multidimensional de alto rendimiento y 
#herramientas para trabajar con estas matrices. 
#Si ya está familiarizado con MATLAB, puede que Numpy de le haga familiar.

import numpy as np

a = np.array([1, 2, 3])   # Crea un arreglo unidimensional
print(type(a))            # Imprime el tipo de dato
print(a.shape)            # Imprime las dimensiones "(3,)"
print(a[0], a[1], a[2])   # Indexazion "1 2 3"
a[0] = 5                  # Asignacion por elemento
print(a)                  # "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Arreglo de dos dimensiones
print(b.shape)                     # Imprime las dimensiones "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # "1 2 4"


#Funciones con rangos
a = np.arange(10) # 0 .. n-1  (!)
print(a) #imprime array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.arange(1, 9, 2) # inicio, fin (no inclusivo), salto
print(b) #imprime array([1, 3, 5, 7])

#Rangos con 
c = np.linspace(0, 1, 6)   # inicio, fin, numero de puntos
print(c) #imprime array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ])
d = np.linspace(0, 1, 5, endpoint=False) # para que no sea inclusivo
print(d) #imprime array([ 0. ,  0.2,  0.4,  0.6,  0.8])

#Funciones para crear matrices
a = np.zeros((2,2))   # Crea un array con ceros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Crea un array con unos
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Crea un array con una constante
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create matriz identidad 2x2
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Crea una matriz con random
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"

#Slicing: Similar a las listas de Python, matrices numpy se permiten el slicing.
#Dado que los arreglos pueden ser multidimensionales, 
#debe especificar una slice (:) para cada dimensión de la matriz

# Crear la siguiente matriz con shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Usar slicing para objtener el subarray de las primeras dos filas
# y las columnas 1 y 2; b seria el siguiente array de shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A un slice es una vista de los datos, modificar b... también modifica a!!!
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"

import numpy as np

a = np.arange(15).reshape(3,5)


print(a)
print("Forma: ",a.shape)
print("Dimension: ",a.ndim)
print("Tipo de dato: ",a.dtype.name)
print("# elementos",a.size)

print("Tipo de objeto", type(a))


b=np.array([2.1,3.2,4])
print(b)

print("Tipo de dato: ",b.dtype.name)


c=np.array([(1,3,4.3),(1,4.5,0)])
print(c.shape)

d=np.array([[1,2],[3,4]],dtype=complex)
print(d)

zeros=np.zeros((3,3))
print(zeros)

unos=np.ones((2,3,4),dtype=np.int16)
print(unos)


random=np.empty((2,3))
print(random)

print(np.pi)

e=np.linspace(0,2,19)
print(e)

a=np.array([20,30,40,50])
b=np.arange(4)
print(a+b)
print(a-b)
print(b**2)
print(10*np.sin(a))

A=np.array(
        [[5,4],
        [1,2]]
        )

B=np.array(
        [[1,2],
        [2,3]]
        )
        
print(A*B)
print(A.dot(B))
print(np.dot(A,B))

unos=np.ones(3,dtype=np.int32)
b=np.linspace(0,np.pi,3)
print(b.dtype.name)
c=unos+b
print(c)

r=np.random.random((2,3))
print(r)
print(unos.sum())
print(r.min())
print(r.max())
print(r[1][2])
