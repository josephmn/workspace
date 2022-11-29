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

usuario = Usuario('Felipe', 'Feliz')

# imprimimos
usuario.saludo()
usuario.nombre = 'Chanchito'
usuario.saludo()

admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()

# usuario.superSaludo()
# las instancias de la clase padres no se puede llamar a los metodos y propiedades
# de las clases hijo