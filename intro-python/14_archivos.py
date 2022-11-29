# open, por defecto ya viene con su argumento read (r)

# Argumentos
# read (r) - leer un archivo
# append (a) - agregar mas texto al archivo
# write (w) - escribir en el archivo
# en caso que el archivo no exista, python crea el archivo
# agregar (x) - crea el archivo

# ejemplo: c = open('chanchito.txt','x')

c = open('chanchito.txt')

# print(c.read()) # .read -> devuelve la lectura de todo el archivo
# print(c.readline()) # .readline -> muestra lineas por lineas el txt

for x in c:
    print(x)

c.close() # buena practica cerrar el archivo