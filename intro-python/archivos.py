#el segundo parametro de open tiene los siguientes argumentos
#r = read, es el paremtro por defecto, no hace falta indicarlo
#a = append, sirve para agregar texto al final del archivo
#w = write, permite modificar todo el archivo, en caso de que el archivo no exista se crea
#x = crear, sirve para crear un archivo, si ya esta creado da error
#c = open("chanchito.txt")
#c = open("chanchito.txt", 'a')
#c = open("chanchito.txt", 'w')

#print(c.read()) #read() lee todo el archivo

#print(c.readline())#lee solo una linea del archivo
#print(c.readline())

#for x in c:
#    print(x)

#c.write("\nse agrega una nueva linea al archivo") #se agrega una linea al final del archivo
# c.write("hola, soy el nuevo texto")

# c.close() #cierra el archivo para que no hayan problemas

# c = open("chanchito.txt")
# for x in c:
#     print(x)
# c.close()

import os 
if os.path.exists("chanchito.txt"):
    os.remove("chanchito.txt")
else:
    print("El archivo no existe")


os.rmdir("micarpeta")

