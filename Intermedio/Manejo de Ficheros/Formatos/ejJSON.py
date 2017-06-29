import json

print(json.dumps(["e1",{"sub1":(0,None,1.0)}]))

nombres='{"primerNombre":"Alan","apellido":"Garrido"}'

obj=json.loads(nombres)
print(obj['primerNombre'])

infile=open("marks.json")
archivo=infile.read()

print(archivo)
objson=json.loads(archivo)

print(objson['markers'][0]["information"])