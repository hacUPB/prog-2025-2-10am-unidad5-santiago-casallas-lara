lista = ["Ducati","RHLM","Los Cacorros usan clemont","TBT","Robert de niro"]
ubicacion ="C:\\Users\\B09S202est\\Desktop\\Archivos"
modo = "w"

nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding ="utf-8")

for cancion in lista:
    fp.write(cancion + "\n")
fp.close()