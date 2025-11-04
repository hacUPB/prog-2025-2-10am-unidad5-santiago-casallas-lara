'''
#abrir el archivo y definir el modo
archivo = open("texto.txt","r")
#leer el archivo
datos = archivo.read(10)
print (datos)
#cerrar el archivo 
archivo.close()
'''
'''
#abrir el archivo y definir el modo
archivo = open("texto.txt","r")
#leer el archivo
for i in range(5):
    datos = archivo.readline()
for datos in archivo:
    print (datos[0])
#cerrar el archivo 
archivo.close()
'''
'''
#abrir el archivo y definir el modo
archivo = open("texto.txt","r")
#leer el archivo
datos = archivo.readlines()
print (datos)
#cerrar el archivo 
archivo.close()
'''