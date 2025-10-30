nombre_archivo = "texto.txt"
ubicacion ="C:\\Users\\B09S202est\\Desktop\\Archivos"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    #leer todas las lineas dentro de una lista 
    lista = archivo.readlines()

#se imprime la lista elemento por elemento
for c in lista:
    print(c)