# os es un  del SO para eliminar archivos y carpetas
import os

# eliminando un archivo (file)
if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

# eliminando una carpeta (dir)
os.rmdir('micarpeta')