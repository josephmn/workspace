################## HERENCIA ##################

################## EJEMPLO 1 ##################
# clase padre
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)

# clase hijo


class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo', self.nombre, 'y soy administrador')

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

# extendiendo metodo padre(1): nombramos la clase padre
class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

# extendiendo metodo padre(2): sin referencia de instancia (self)
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

# instancias
gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

perro = Canario('Piolin', 'silvido')
perro.saludo()
