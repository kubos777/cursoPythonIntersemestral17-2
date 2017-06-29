import pickle
import json
import time

def to_json(objetoPython):
    if isinstance(objetoPython, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(objetoPython)}
    if isinstance(objetoPython, bytes):
        return {'__class__': 'bytes',
                '__value__': list(objetoPython)}
    raise TypeError(repr(objetoPython) + ' no es un JSON serializable')

def from_json(objetoJSON):
    if '__class__' in objetoJSON:
        if objetoJSON['__class__'] == 'time.asctime':
            return time.strptime(objetoJSON['__value__'])
        if objetoJSON['__class__'] == 'bytes':
            return bytes(objetoJSON['__value__'])
    return objetoJSON

if __name__ == '__main__':
    libros = {}  
    libros['titulo'] = 'Dive into Python'
    libros['autor'] = 'Mark Pilgrim'
    libros['link'] = 'https://cloud.github.com/downloads/diveintomark/diveintopython3/dive-into-python3.pdf'
    libros['tags'] = ('diveintopython', 'programacion', 'python3')
    libros['published'] = True
    libros['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')                     

    with open('libros.pickle', 'wb') as f:
        pickle.dump(libros, f)

    with open('libros.pickle', 'rb') as f:
        libros2 = pickle.load(f)

    print(libros == libros2)
    print(type(libros['tags']))
    print(type(libros2['tags']))

    with open('libros.json', 'w', encoding='utf-8') as f:
        json.dump(libros, f, default=to_json)

    with open('libros.json', 'r', encoding='utf-8') as f:
        libros2 = json.load(f, object_hook=from_json)

    print(libros == libros2)
    print(type(libros['tags']))
    print(type(libros2['tags']))
