################## CLASES ##################

################## EJEMPLO 1 ##################
# class Usuario:
#     nombre = "Felipe"
#     apellido = "Feliz"

# # usuario es una instancia
# usuario = Usuario()
# usuario2 = Usuario()

# # devuelve un objeto
# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

################## EJEMPLO 2 ##################
# creando clase (plano de lo que creamos)
class Usuario:
  # se ejecuta siempre al crear una instancia
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

# usuario es una instancia
# ingresamos parametros para que la clase tome los argumentos
usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')

# imprimimos
print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
