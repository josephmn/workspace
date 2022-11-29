################## CLASES ##################

################## EJEMPLO 1 ##################

# class Usuario:
#   # se ejecuta siempre al crear una instancia
#   def __init__(self, nombre, apellido):
#     self.nombre = nombre
#     self.apellido = apellido
  
#   # metodo
#   def saludo(self):
#     print('Hola!, mi nombre es', self.nombre, self.apellido)

# # usuario es una instancia
# usuario = Usuario('Felipe', 'Feliz')
# usuario2 = Usuario('Chanchito', 'Feliz')

# # imprimimos
# usuario.saludo()
# usuario2.saludo()


################## EJEMPLO 2 (SELF, ELIMINAR PROPIEDADES Y OBJETOS) ##################

class Usuario:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
  
  def saludo(self):
    print('Hola!, mi nombre es', self.nombre, self.apellido)

usuario = Usuario('Felipe', 'Feliz')

# imprimimos
usuario.saludo()
usuario.nombre = 'Chanchito'
usuario.saludo()
del usuario.nombre
# usuario.saludo()
del usuario
print(usuario)