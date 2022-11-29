import modulos as xs
from camelcase import CamelCase # forma de usar modulo camelcase

print(xs.mascotas)
xs.saludo('Nicolas')

# para instalar camelcase: py -m pip install camelcase

# instanciamos
c = CamelCase()
s = 'esta oracion necesita CamelCase'

camelcase = c.hump(s)
print(camelcase)