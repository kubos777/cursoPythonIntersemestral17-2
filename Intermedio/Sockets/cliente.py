# Cliente

import socket

s=socket.socket()
s.connect(("localhost",9000))

while True:
	mensaje=input("Ingresa tu mensaje: ")
	s.send(mensaje.encode())
	if mensaje=="adios":
		break
	respuesta=s.recv(1024).decode()
	print("Respuesta del servidor: ",respuesta)

print("Finaliza la conexion")
s.close()