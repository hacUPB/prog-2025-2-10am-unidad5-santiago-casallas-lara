ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
# el \ se utiliza para comandos de texto
nombre_archivo = "frutas.txt"
modo = "a" # solo escritura - sobre escribe 
fp = open(ubicacion+"\\"+nombre_archivo,modo,encoding="utf-8")
frase = input("por favor ingrese una frase: ")
fp.write(frase)
#solicitar una variable entera y una flotante al usuario y la escriben en el archivo
peso = float(input("ingrese un numero por favor: "))
numero = int(input("ingrese su peso por favor: "))

fp.write(frase + "\n")
fp.write(str(peso))
fp.write(frase+"\n")
fp.write(str(numero))

fp.close()