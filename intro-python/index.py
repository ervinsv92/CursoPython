#esto es un comentario
if 5 > 3:
    #print("5 es mayor a 3")
    var = 1

x = 5
y = "chanchito feliz"

#print(x,y)

a, b, c = 'la', 'le', 'li'
#print(a,b,c)

val1 = val2 = val3 = "nada"
#print(val1, val2, val3)

inicio = "hola "
final = "mundo"

#print(inicio+final)

palabra = 'comilla simple' #string
palabra2= "comillas dobles" #string

entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j

#print(palabra, palabra2, entero, conDecimales, complejo)

lista = [1,2,3,3, "carro", "bici"]
lista2 = lista.copy()
lista.append(4)
#lista.clear()
#print(lista, lista2.count(3))
#print(len(lista))
#print(lista[0])

#lista.pop()#elimina el ultimo elemento de la lista
#print(lista)

#lista.remove("carro") #elimina elemento por su valor
#print(lista)

lista.reverse()
#lista.sort() #no deja ordenarla porque tiene tipos de datos diferentes
#print(lista)

#las tuplas no se pueden cambiar una vez creadas
tupla = ("hola", "mundo", "somos", "tupla")
#print(tupla.count("hola"))
#print(tupla.index("somos"))
#print(tupla[2])

listaDeTupla = list(tupla)
listaDeTupla.append("otra tupla")
#print(listaDeTupla)

rango = range(6)
#print(rango)

diccionario = {
    "nombre":"Chanchito feliz",
    "raza":"persa",
    "edad":5
}

#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario.get('raza'))
diccionario['nombre'] = "Fluffy"
#print(diccionario)
#print(len(diccionario))

diccionario['ronronea'] = "Si" #sino existe lo agrega al diccionario
#print(diccionario)
diccionario.pop('ronronea') #elimina el elemento del diccionario con el nombre espesificado
#print(diccionario)
diccionario.popitem() #elimina el ultimo elemento del diccionario
#print(diccionario)
del diccionario['raza'] #elimina el elemento del diccionario por llave
#print(diccionario)
copiaDiccionario = diccionario.copy()
copiaDiccionario2 = dict(diccionario) #otra manera de copiar los diccionarios
#print(copiaDiccionario)
diccionario.clear() #elimina todos los elementos del diccionario
#print(diccionario)

floffy = {
        "nombre":"Floffy",
        "edad":4
        }

gatos = {
    "Floffy":floffy,
    "Mamba":{
        "nombre":"Black Mamba",
        "edad":12
    }
}

#print(gatos)

perros = dict(nombre = "chanchito feliz", edad=6) #crea un diccionario
#print(perros)

verdadero = True
falso = False
print(verdadero, falso)