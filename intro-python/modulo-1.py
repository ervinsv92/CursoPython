#import modulos #asi se usa sino se le pone alias
#import modulos as xs
from modulos import saludo, mascotas #tambien se pueden importar varias cosas, las que necesitemos
from camelcase import CamelCase 

#print(xs.mascotas) #sirve si se importa el modulo completo
#modulos.saludo("Elian") #si se importa sin alias
#xs.saludo("Elian") #si se importa con alias
saludo("Ervin")
print(mascotas)

c = CamelCase()
s = "esta oracion necesita camelcase"

camelcased = c.hump(s)

print(camelcased)