####Excepciones##
#Una excepción es un tipo de error que ocurre durante la ejecución
#Estructura try-except
#try: ->Aquí dentro va el código que nos puede ocasionar una excepción
#except ->Aquí va la excepción, nos puede enviar un mensaje
#else: ->Si no ocurre ninguna excepción, entramos al else
#finally: ->Se va a ejecutar siempre, haya o no haya excepción
#################
try:
	numero=int(input("Ingresa un numero, te lo voy a dividir:  "))
	print(10/numero)
except ZeroDivisionError:
	print("Error, no puedes dividir entre cero. Esta indefinido.")
except ValueError:
	print("Estamos solicitando un entero, ingresa un entero.")
else:
	print("Todo esta bien, no se levantó ninguna excepción.")
finally:
	print("Finally se ejecuta siempre, haya o no haya alguna excepción.")