###############
# Serialización
###############

#En este script vamos a deserializar el objeto

import pickle
with open('libros.pickle', 'rb') as f:
	libros = pickle.load(f)

print(libros)  