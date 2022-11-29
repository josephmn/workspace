############################ CLASE 02 ############################

# Acá va un comentario
from asyncio.format_helpers import _format_callback_source
from tabnanny import verbose


if 3 > 5:  # Acá va otro comentario
    print('Estio no se va a imprimir')

# if 5 > 3: # Acá va otro comentario
#     print('5 es mayor que 3')

x = 5
y = 'chanchito feliz'

# print(x, y)

email = 'josephcarlos.jcmn@gmail.com'

# print(email)

mi_var = 'chanchito'

# camel case
miVar = 'chanchito'

# asignar constantes, variables que no cambiaran su valor (MAYUSCULAS)
MIVAR = 'chanchito'

a, b, c = 'Lala', 'Lele', 'Lili'

# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

# print(valor1, valor2, valor3)

inicio = 'Hola '
final = 'mundo'

# print(inicio + final)

############################ CLASE 02 ############################

palabra = 'hola mundo'  # string
oracion = "hola mundo comilla doble"  # string

entero = 20  # integer
conDecimales = 20.2  # float
complejo = 1j  # complejo

# print(palabra, oracion, entero, conDecimales, complejo)

############################ CLASE 03 ############################

lista = [1, 2, 3]
lista2 = lista.copy()
lista.append(4)
# lista.clear()
# print(lista, lista2)


############################ CLASE 04 ############################

# lista = [3, 2, 3]
# lista2 = lista.copy()
# lista.append(4)
# lista.clear()
# print(lista, lista2.count(3))
# print(len(lista), len(lista2))

# largoLista = len(lista)
# largoLista2 = len(lista2)

# print(largoLista, largoLista2)

############################ CLASE 05 ############################

lista = ['Hola', 'Mundo', 'Chanchito feliz']
# lista.append(4)
lista.append('Chanchito triste')

# print(lista[0])
# print(lista[1])
# print(lista[2])

############################ CLASE 06 ############################

# lista.pop() # elimina el ultimo elemento de una lista

# lista.remove('Hola') # este elimina un elemento por su valor


# lista.reverse() # listar la lista al reves

# lista.sort() # debe tener el mismo tipo de dato si queremos ordenar los datos
# print(lista)

############################ CLASE 07 (TUPLA) ############################

tupla = ('hola', 'mundo', 'somos', 'tupla')
# print(tupla)
# print(tupla.count('hola'))
# print(tupla.index('mundo'))
# print(tupla[0])

listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
# print(listaDeTupla)

# agregado rangos
rango = range(6)
# print(rango)

############################ CLASE 08 (DICCIONARIO) ############################

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))

diccionario['nombre'] = 'Fluffy'

# print(diccionario)
# print(len(diccionario))

############################ CLASE 09 (DICCIONARIO AGREGAR) ############################

# agregando una propiedad o valor
diccionario['ronronea'] = 'Si'

# print(diccionario)
# diccionario.pop('ronronea') # elimianr propiedad o valor
# diccionario.popitem() # elimina la ultima propiedad o valor

# copiGatito = diccionario.copy()
# del diccionario['ronronea']
copiGatito = dict(diccionario)
diccionario.clear()
# print(diccionario, copiGatito)

############################ CLASE 10 (DICCIONARIOS ANIDADO) ############################

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre": "Black Manba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)

print(perritos)

verdadero = True
falso = False

print(verdadero, falso)