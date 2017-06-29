# -*- coding: utf-8 -*-
from fbchat import Client
from fbchat.models import *
from getpass import getpass

usuario = input("Dame tu correo: ")
cliente = Client(usuario,getpass())

amigos = cliente.fetchThreadList()
nAmigo=0
for amigo in amigos:
	print(nAmigo+1,". "+amigo.name)
	nAmigo+=1

idAmigo=int(input("Ingresa el id del amigo o grupo: "))
mensaje=input("Ingresa tu mensaje:")
cliente.sendMessage(mensaje, thread_id=amigos[idAmigo].uid, thread_type=ThreadType.USER)


thread_type=ThreadType.GROUP
thread_id='1473908892667021'
# mandar un emoji '👍'
cliente.sendEmoji(emoji='👍', size=EmojiSize.LARGE, thread_id=thread_id, thread_type=thread_type)

# Will send the default 'like' emoji
cliente.sendEmoji(emoji=None, size=EmojiSize.LARGE, thread_id=thread_id, thread_type=thread_type)

# Will send the emoji '😏'
cliente.sendEmoji(emoji='😏 ', size=EmojiSize.LARGE, thread_id=thread_id, thread_type=thread_type)
cliente.sendEmoji(emoji='😏 ', size=EmojiSize.MEDIUM, thread_id=thread_id, thread_type=thread_type)
cliente.sendEmoji(emoji='😏 ', size=EmojiSize.SMALL, thread_id=thread_id, thread_type=thread_type)

# Will send the image located at '<image path>'
cliente.sendLocalImage('logo.png', message='This is a local image', thread_id=thread_id, thread_type=thread_type)

# Will download the image at the url '<image url>', and then send it
cliente.sendRemoteImage('https://s-media-cache-ak0.pinimg.com/236x/b9/cb/47/b9cb4790046aed53c60629fd11c6ba12.jpg', message='This is a remote image', thread_id=thread_id, thread_type=thread_type)


cliente.logout()