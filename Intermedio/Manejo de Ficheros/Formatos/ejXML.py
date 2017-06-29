import xml.etree.ElementTree as etree

tree=etree.parse("libros.xml")
print(tree)

raiz=tree.getroot()

print(raiz)

print(dir(raiz))

print(raiz.tag)
print(raiz.attrib)

for rama in raiz:
	print(rama.tag,rama.attrib)
	for subrama in rama:
		print(subrama.tag,subrama.text)
