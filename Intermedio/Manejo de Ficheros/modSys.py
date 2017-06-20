############
# Modulo sys
############


import sys
print(sys.platform)
""">>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps1="$ "
$ print("Hola")
Hola
$ sys.ps1="-> "
-> sys.getrecursionlimit()
1000
-> sys.setrecursionlimit(1002)
-> sys.getrecursionlimit()
1002
-> sys.version
'3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)]'
"""
print("Parametros de la linea de comandos ",sys.argv)