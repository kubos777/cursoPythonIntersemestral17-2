#-*-coding:utf-8-*-
#Modulo que nos va a permitir enviar correos electronicos desde python 3
import smtplib
#To, es a quién será enviado el correo
to ='allanstone19@gmail.com'
#Datos de quien enviará el correo
gmail_User='cursopython.proteco@gmail.com'
gmail_Pass='python.isCool'
#El método SMTP recibe el nombre del servidor al que vamos a pedirle
#que nos permita enviar el correo y además su puerto.
smtpserver=smtplib.SMTP('smtp.gmail.com',587)
#Con el método ehlo, saludamos al servidor, y nos conectamos
smtpserver.ehlo()
#Aquí comenzamos la transferencia, si nos reconocio.
smtpserver.starttls()
smtpserver.ehlo
##########################Logueo en gmail
#El método login nos va a permitir loguearnos en gmail
smtpserver.login(gmail_User,gmail_Pass)

cabecera="To"+to+'\n'+'From: '+ gmail_User+'\n'+'Subject: Hola \n'

print(cabecera)

mensaje= cabecera + '\n Este es un mensaje, enviado desde la sala D del curso Intermedio de Python por PROTECO'

smtpserver.sendmail(gmail_User,to,mensaje)

print("Correo enviado!")
#Terminamos la conexión
smtpserver.close()