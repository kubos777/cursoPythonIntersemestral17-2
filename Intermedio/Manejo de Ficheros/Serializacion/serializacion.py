###############
# Serialización
###############

#La serialización es el método por el cual convertimos un objeto de python en un stream de datos
#El cual podemos dejar en un archivo y cada que ejecutemos un programa consultar el estado de ese
#objeto y sus datos internos
import time #para trabajar con fechas y horas
#Vamos a crear un diccionario y luego a serializarlo
libros = {}  
libros['titulo'] = 'Dive into Python'
libros['autor'] = 'Mark Pilgrim'
libros['link'] = 'https://cloud.github.com/downloads/diveintomark/diveintopython3/dive-into-python3.pdf'
libros['tags'] = ('diveintopython', 'programacion', 'python3')
libros['published'] = True
libros['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')                     

import pickle
with open('libros.pickle', 'wb') as f:
	pickle.dump(libros, f) 