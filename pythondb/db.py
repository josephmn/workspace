import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sgr9cl4v3s',
    database='prueba'
)

cursor =  midb.cursor()

# --------------------------------------------------------------------------
##### PARA CONSULTA A MYSQL #####
cursor.execute('select * from Usuario')
resultado = cursor.fetchall() # muestra todos los datos de la consulta
# resultado = cursor.fetchone() # muestra solo el primer dato de la consulta
print(resultado)

# --------------------------------------------------------------------------
##### PARA CONSULTA A MYSQL LIMITAR VALORES #####
# cursor.execute('select * from Usuario limit 2')
# resultado = cursor.fetchall() # muestra todos los datos de la consulta
# # resultado = cursor.fetchone() # muestra solo el primer dato de la consulta
# print(resultado)

# --------------------------------------------------------------------------
##### DML (INSERT) - MYSQL #####
# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@correo.co.nz', 'nombreusuario', 45)
# cursor.execute(sql, values)

# midb.commit()
# print(cursor.rowcount)

# --------------------------------------------------------------------------
##### DML (UPDATE) - MYSQL #####
# sql = 'update Usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 4)
# cursor.execute(sql, values)

# midb.commit()
# print(cursor.rowcount)

# --------------------------------------------------------------------------
##### DML (DELETE) - MYSQL #####
# sql = 'delete from Usuario where id = %s'
# values = (4, ) # recordar colocar (4, ) <-- un espacio despues del primer param
# cursor.execute(sql, values)

# midb.commit()
# print(cursor.rowcount)
