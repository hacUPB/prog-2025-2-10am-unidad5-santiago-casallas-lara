#abrir el archivo y definir el modo
archivo = open("ejercicio_1","r")
archivo.readline()
archivo.readline()
archivo.read(11)
datos = archivo.readline()
archivo.close()
print(datos)