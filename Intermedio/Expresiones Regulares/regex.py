#######################
# Expresiones Regulares
# Nos ayudan a identificar patrones
# E identificar grupos de cadenas
# Son conjuntos de metacaracteres
# Meta -> Mas allá de
#######################

import re

# Rangos, se usan entre corchetes
# [0-9] -> 0, 1, 2, 3. ..., 9
# [a-z] -> a, b, c, d, ..., z
# [A-Z] -> A, B, C, D, ..., Z
# [0-9a-zA-Z] -> Se pueden combinar
# [a-f5-8]-> de la a a la f o del 5 al 8
# [az-] -> a, z , -
# {n} n = numero de veces exactas
# {n,m} n=minimo de veces, m=maximo de veces

# Grupos, se usan entre paréntesis
# (...) Permiten englobar otros metacaracteres

#Metacaracter {}

def buscar(patrones, texto):
	for patron in patrones:
		print( re.findall(patron, texto) )


patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']
texto = "hla hola hoola hooola hooooola"

buscar(patrones, texto)

#Metacaracter []

def buscar(patrones, texto):
	for patron in patrones:
		print( re.findall(patron, texto) )

patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
texto = "hala hela hila hola hula"
buscar(patrones, texto)

#Metacaracteres combinados

def buscar(patrones, texto):
	for patron in patrones:
		print( re.findall(patron, texto) )

patrones = ['h[a‐z]la', 'h[0‐9]la', '[a‐z]{4}', '[A‐Z][A‐z0‐9]{3}']
texto = "h0la Hola aaaa bbbb hala hzla hbla hola"
buscar(patrones, texto)


# Metacaracter Negacion ^ ,
# para obtener el grupo contrario

if re.match("python[^0-9a-z]", "pythonZ", re.IGNORECASE): #ignora mayusculas o minusculas
	print("Hizo match")


# Escape
# Para que un metacaracter pierda su cualidad de metacaracter, se debe "escapar" con una "\"
# Así el metacaracterl "." al escaparse "\." simplemente es el caracter punto

# Alias
# \d -> equivale [0-9]
# \D -> equivale [^0-9]
# \A -> iniciar con el match
# \w -> equivale [a-zA-Z_]
# \W -> equivale [^a-zA-Z_]
# \s -> equivale a cualquier caracter en blanco [ \n\t]
# \S -> equivale a cualquier caracter no en blanco