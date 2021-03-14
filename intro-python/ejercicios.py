# dato = input("Ingrese dato: ")

# lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

# if lista.count(dato) > 0:
#     print("El dato existe", dato)
# else:
#     print("El dato no existe", dato)

primero = input("Ingrese primer numero: ")
try:
    primero=int(primero)
except:
    print("Debe ingresar valores numericos")
    exit()
segundo = input("Ingrese segundo numero: ")
try:
    segundo = int(segundo)
except:
    print("Debe ingresar valores numericos")
    exit()

simbolo = input("ingrese operacion: ")

if simbolo == "+":
    print("Suma:", int(primero) + int(segundo))
elif simbolo == "-":
    print("Resta:", int(primero) - int(segundo))
elif simbolo == "*":
    print("Multiplicacion:", int(primero) * int(segundo))
elif simbolo == "/":
    print("Division:", int(primero) / int(segundo))
else:
    print("El operador debe ser (+,-,*,/)")