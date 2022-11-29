# i = 0

# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

################## EJEMPLO 01 ##################

# usuarios = ['chanchito feliz','felipe','roberto','nicolas']

# for usuarios in usuarios:
#     print(usuarios)

################## EJEMPLO 02 ##################

# usuarios = 'Chanchito feliz'

# for c in usuarios:
#     print(c)

################## EJEMPLO 03 ##################

# usuarios = ['chanchito feliz','felipe','roberto','nicolas']

# for usuarios in usuarios:
#     if usuarios == 'roberto':
#         break
#     print(usuarios)

################## EJEMPLO 04 ##################

# usuarios = ['chanchito feliz','felipe','roberto','nicolas']

# for usuarios in usuarios:
#     if usuarios == 'roberto':
#         continue
#     print(usuarios)

################## EJEMPLO 05 ##################

# for x in range(3,30,5):
#     print(x)
# else:
#     print('Hemos terminado!')

################## EJEMPLO 05 ##################

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)