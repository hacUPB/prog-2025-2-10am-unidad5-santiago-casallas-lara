import csv
with open('C:\\Users\\B09S202est\\Desktop\\Archivos\\datos-numericos.csv','r') as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    #print(encabezado)
    #print(sum(fila[0]))
    presion = []
    print(encabezado[3])
    for fila in lector:
        fila[3] = fila[3].replace(',','.')
        dato = float(fila[3])
        presion.append(dato)

print(presion)