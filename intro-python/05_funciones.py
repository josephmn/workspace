################## CREAR FUNCIONES ##################

# def mifuncion():
#     print('Mi primera funcion')

# mifuncion()

# def imprimeDato(argumentoUno):
#     print('Mi argumento es', argumentoUno)

# imprimeDato('parametro 1')

################## EJEMPLO 1 ##################

# def imprimeDato(nombre, apellido):
#     print('El nombre completo es:', nombre, apellido)

# imprimeDato('Chanchito', 'Feliz')

################## EJEMPLO 2 ##################
# al ingresar un arterisco (*) en los argumentos de la funcion este asume que
# enviaras multiples parametros

# def imprimeDato(*nombre):
#     print('El nombre completo es:', nombre[1])

# imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')

################## EJEMPLO 3 ##################
# tambien se puede enviar parametros identificado con el mismo nombre del
# argumento en la funcion, ver ejemplo:

# def nombrecompleto(apellido, nombre):
#     print(nombre, apellido)

# nombrecompleto(nombre='Chanchito', apellido='Feliz')

################## EJEMPLO 4 ##################
# **kwarg sirve para mandar varios parametros, pero este cumple la condicion
# que al enviar los parametros este se escriban asi: nombre='Chanchito' por que
# se declaro kwarg['nombre']

# def nombrecompleto2(**kwarg):
#     print(kwarg['nombre'], kwarg['apellido'])

# nombrecompleto2(nombre='Chanchito', apellido='Feliz')

################## EJEMPLO 5 ##################
# valor por default argumento dentro de una funcion, este si no 
# mandas un parametro, toma el argumento por default

# def mifuncion2(argumento = 'Chanchito'):
#     print(argumento)

# mifuncion2('Batman')
# mifuncion2()

################## EJEMPLO 6 ##################
# podemos mandar una lista como parametro e iterar dentro de la funcion
# dicho argumento

# def miFuncionLista(lista):
#     for el in lista:
#         print(el)

# miFuncionLista(['Chanchito','Feliz'])

################## EJEMPLO 7 ##################
# podemos tambien contanar nombres

def concatenarNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

nombre = concatenarNombres(['Chanchito', 'Feliz'])
print(nombre)