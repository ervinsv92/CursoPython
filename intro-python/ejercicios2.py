#1- multiplicar 2 numeros sin usar el simbolo de multiplicacion
a = 4
b = 8
res = 0

for num in range(b):
    res += a
print(res)

#2- ingresa nombre y apellido e imprimirlo al reves

nombreCompleto = "Ervin "
nombreCompleto += "Solano"

cantidad = len(nombreCompleto) -1
resAlreves = ""

while cantidad > -1:
    resAlreves += nombreCompleto[cantidad]
    cantidad -=1

print(resAlreves)
print(resAlreves[::-1])#le da vuelta al string con solo una instruccion

#3- encontrar el menor numero de una lista
lista = [1,2,5,3,55,-24,13]
lista.sort()
print("Numero menor de la lista:", lista[0])

#4- escribir una funcion que devuelva el volumen de una esfera por su radio
#formula 4/3 * pi * r ** 3
def calcularVolumenEsfera(r):
    return 4/3 * 3.14 * r **  3#** es elevacion 4 elevado a la 3

print("El volumen de la esfera es:",calcularVolumenEsfera(6))

#5- escribir una funcion que indique si el usuario es mayor de edad

def esMayorDeEdad(usuario):
    return usuario.edad > 17
    
class Usuario:
    def __init__(self,edad):
        self.edad = edad

usuario = Usuario(17)
usuario2 = Usuario(18)

print(esMayorDeEdad(usuario), esMayorDeEdad(usuario2))

#6- escribir una funcion que indique si un numero es par o impar
def esPar(numero):
    return numero % 2 == 0 #el operador de modulo es %

print(esPar(2), esPar(3))    

#7- escribir una funcion que indique cuantas vocales tiene una palabra
palabra = "chAnchito feliz"
vocales = 0
for y in palabra:
    x = y.lower() #cambia la letras a minuscula
    vocales += 1 if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" else 0 #if ternario
    #if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        #vocales += 1
print("La cantidad de vocales de la palabra", palabra, " es:", vocales)

#8- escribir una aplicacion que reciba una cantidad infinita de numeros hasta
#decir basta, luego que devuelva la suma de los numeros ingresados

lista = []
print("Ingrese numeros y para salir escriba 'basta'")
while True:
    dato = input("Numero: ")
    if dato == "basta":
        break
    else:
        try:
            dato = int(dato)
            lista.append(int(dato))
        except:
            print("Dato invalido")
            exit()

suma = 0
for numero in lista:
    suma += numero
print("La suma es:", suma)

#9- escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo
def agregarNombreCompleto(nombre, apellido):
    archivo = open("nombres.txt", "a")
    archivo.write(nombre + " " + apellido + "\n")

agregarNombreCompleto("Ervin", "Solano")
agregarNombreCompleto("Carmen", "Vargas")