def miFuncion():
    print("soy una funcion")

#miFuncion()

def imprimeDatoVariable(*nombre):
    #print("El nombre completo es", nombre)#imprime una tupla
    print("El nombre completo es", nombre[0])#imprime un elemento de la tupla

def imprimeDato(nombre, apellido):
    print("El nombre completo es", nombre, apellido)

#imprimeDato("ervin", "solano")
#imprimeDatoVariable("chanchito", "feliz", "yo")

def nombreComleto(apellido, nombre):
    print(nombre, apellido)

#nombreComleto(nombre="Chancho", apellido="Feliz")
def nombreComleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

#nombreComleto2(nombre="Chancho", apellido="Feliz")

def miFuncion2(argumento = "chancho"):
    print(argumento)

# miFuncion2("bartman")
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['perro', 'gato', 'elefante'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i += el + " "
    return i

#print(concatenaNombres(['perro', 'gato', 'elefante']))

def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i - 1)

recursion(6)
