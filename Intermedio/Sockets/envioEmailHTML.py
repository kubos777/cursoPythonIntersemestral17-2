import smtplib
sender = 'cursopython.proteco@gmail.com'
pwd = 'python.isCool'
receivers = 'jorgechavez.proteco@gmail.com'

message = """From: pyTeco <cursopython.proteco@gmail.com>
To:<jorgechavez.proteco@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Hola, amigos de intermedio

	<div style="font-family: 'Pacifico', cursive;background: #CBAEAE">
	<center>
	<h1>This is <span style="color: #61E58D">Python 3</span></h1>

	<p style="color:#1D0D0D">El correo ha sido enviado desde: Sala D</p>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	</center>
</div>

</body>
</html>
"""

try:
   smtpObj = smtplib.SMTP("smtp.gmail.com",587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo
   smtpObj.login(sender, pwd)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except Exception as e:
   print ("Error: unable to send email")
   print(e)