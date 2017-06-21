import re
correo='allanstone19@gmail.com'
 
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,3}$',correo):
	print ("Correo correcto")
else:
	print ("Correo incorrecto")