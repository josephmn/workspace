#/*************************************************************************/
# agregando texto
# instruccion salto de linea \n
# append (a)
###########################################################################
# c = open('chanchito.txt', 'a')
# c.write('\nagregamos una nueva linea a nuestro archivo')
# c.close()

# x = open('chanchito.txt')
# print(x.read())

#/*************************************************************************/
# escribir texto
# instruccion salto de linea \n
# write (a)
###########################################################################
c = open('chanchito.txt', 'w')
c.write('\nagregamos una nueva linea a nuestro archivo')
c.close()

x = open('chanchito.txt')
print(x.read())