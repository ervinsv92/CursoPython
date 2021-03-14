class Usuario: #init es el constructor
    def __init__(self, nombre, apellido): #self (this) es la referencia al usuario, no se usa como paremetro cuando se instancia la clase
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self): #se le puede cambiar el nombre de self a cualquier otro, siempre el primer parametro es la referencia, pero por convencion mejor dejar self siempre
        print("Hola, mi nombre es", self.nombre, self.apellido)

class Admin(Usuario): #lo que va dentro de () es la clase de la que hereda
    def superSaludo(self):
        print("Hola, me llamo,", self.nombre, " y soy administrador")
# usuario = Usuario("Ervin", "Solano")
#usuario2 = Usuario("Carmen", "Vargas")

#print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
# usuario.saludo()
#usuario2.saludo()

# usuario.apellido = "Solano Vargas"

# usuario.saludo()

#del usuario.nombre #elimina el atributo de la clase en tiempo de ejecucion

#del usuario #se elimina toda la instancia del usuario
#print(usuario)

# admin = Admin("Pablo", "Marmol")
# admin.saludo()
# admin.superSaludo()

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy el", self.tipo ," y mi sonido es el", self.onomatopeya)

class Gato(Animal):
    tipo="gato"
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)#extender el metodo del padre
        print("Hola, soy un gato extendido")
class Perro(Animal):
    tipo="perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)#hace referencia a la clase padre, no es necesario pasar el self cuando se usa super
        print("Instanciando un perro")

class Canario(Animal):
    tipo="canario"

gato = Gato("Pecas", "Maullido")
gato.saludo()

perro = Perro("Firulais", "Ladrido")
perro.saludo()

canario = Canario("Piolin", "Silvido")
canario.saludo()