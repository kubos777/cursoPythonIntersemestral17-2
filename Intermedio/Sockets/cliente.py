# Cliente

import socket

s=socket.socket()
#Para poder hacer la conexion entre dos equipos cambiar la ip
#de "localhost" al formato "192.168.1.x", recuerden que pueden
#saber su ip con el comando "ipconfig" en Windows e "ifconfig"
#en linux o Mac, también deben cambiarla en el otro programa
s.connect(("localhost",9000))

while True:
	mensaje=input("Ingresa tu mensaje: ")
	s.send(mensaje.encode())
	if mensaje=="adios":
		break
	respuesta=s.recv(1024).decode()
	print("Respuesta del servidor: ",respuesta)

print("Finaliza la conexion")
#Recordar que es muy importante cerrar explicitamente la conexion
s.close()