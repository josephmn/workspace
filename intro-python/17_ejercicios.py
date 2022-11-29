#################### EJERCICIO 01 ####################
# multiplicar dos numeros sin usar el simbolo de multiplicar

# a = 4
# b = 8

# resultado = 0

# for x in range(a):
#     resultado += b

# print(resultado)

#################### EJERCICIO 02 ####################
# ingresar nombre y apellido e imprimirlo al reves

# nombre = 'joseph'
# apellido = 'magallanes'

# concatenacion = nombre + ' ' + apellido

# print(concatenacion[::-1])

#################### EJERCICIO 03 ####################
# escribir una funcion que encuentre el elemento menor de una lista

# lista = [1, 2, 3, 55, -24, -13]

# menor = 'init'

# for x in lista:
#     if menor == 'init':
#         menor = x
#     else:
#         menor = x if x < menor else menor

# print('menor', menor)

#################### EJERCICIO 04 ####################
# escribir una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

# def calcularVolumen(r):
#     return 4 / 3 * 3.14 * r ** 3

# resultado = calcularVolumen(6)
# print('El volumen de nuestra esfeta es:', resultado)

#################### EJERCICIO 05 ####################
# escribir una funcion que indique si el usuario es mayor de edad

# def esMayor(usuario):
#     return usuario.edad > 17

# class Usuario:
#     def __init__(self, edad):
#         self.edad = edad

# usuario = Usuario(15)
# usuario2 = Usuario(21)

# resultado1 = esMayor(usuario)
# resultado2 = esMayor(usuario2)

# print(resultado1, resultado2)

#################### EJERCICIO 06 ####################
# escribir una funcion que indique si un numero es par o impar

# def esPar(n):
#     return n % 2 == 0

# resultado = esPar(11)
# print(resultado)

#################### EJERCICIO 07 ####################
# escribir una funcion que indique cuantas vocales tiene una palabra

### primera solucion tradicional ###
# palabra = 'ChanchitoFeliz'
# vocales = 0
# for x in palabra:
#     vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

# print(vocales)

### segunda solucion si usan mayusculas o minusculas ###
# palabra = 'ChAnchitoFeliz'
# vocales = 0
# for x in palabra:
#     y = x.lower()
#     vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

# print(vocales)

### tercera solucion simplificada ###
# palabra = 'ChAnchitoFeliz'
# vocales = ['a', 'e', 'i', 'o', 'u']
# tvocales = 0
# for x in palabra:
#     y = x.lower()
#     if y in vocales:
#         tvocales += 1

# print(tvocales)

#################### EJERCICIO 08 ####################
# escribir una aplicacion que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de los numeros ingresados

# lista = []
# print('Ingrese numeros y para salir escriba "basta"')
# while True:
#     valor = input('Ingrese valor: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato inválido')
#             exit()

# resultado = 0
# for x in lista:
#     resultado += x

# print(resultado)

#################### EJERCICIO 09 ####################
# escribir una funcion que reciba nombre y apellido y los vaya agregando a
# un archivo

# def agregaNombreAArchivo(nombre, apellido):
#     c = open('nombrecompleto.txt','a')
#     c.write(nombre + ' ' + apellido + '\n')
#     c.close()

# agregaNombreAArchivo('Joseph', 'Magallanes')
# agregaNombreAArchivo('Chanchito', 'Feliz')
