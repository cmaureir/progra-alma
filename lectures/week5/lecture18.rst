Lecture 18 - Higher-order functions
-----------------------------------

	     map, reduce, filter,
               * funciones como parametros (ver diapo 11)
               * decorators
                  * memoize
                  * metodo statico
.. Archivos de valores con separadores
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Una manera usual de almacenar datos con estructura de tabla
.. en un archivo es la siguiente:
.. cada línea del archivo representa una fila de la tabla,
.. y los datos de una fila se ponen separados
.. por algún símbolo especial.
.. 
.. Por ejemplo,
.. supongamos que queremos guardar en un archivo
.. los datos de esta tabla:
.. 
.. =========== =========== ======= ======= ======= =======
.. Nombre      Apellido    Nota 1  Nota 2  Nota 3  Nota 4
.. =========== =========== ======= ======= ======= =======
.. Perico      Los Palotes 90      75      38      65
.. Yayita      Vinagre     39      49      58      55
.. Fulana      De Tal      96      100     36      71
.. =========== =========== ======= ======= ======= =======
.. 
.. Si usamos el símbolo ``:`` como separador,
.. el archivo, que llamaremos ``alumnos.txt``, debería quedar así::
.. 
..     Perico:Los Palotes:90:75:38:65
..     Yayita:Vinagre:39:49:58:55
..     Fulanita:De Tal:96:100:36:71
.. 
.. El formato de estos archivos se suele llamar CSV_,
.. que en inglés son las siglas de *comma-separated values*
.. (significa «valores separados por comas»,
.. aunque técnicamente el separador puede ser cualquier símbolo).
.. A pesar del nombre especial que reciben,
.. los archivos CSV son archivos de texto como cualquier otro,
.. y se pueden tratar como tales.
.. 
.. .. _CSV: http://en.wikipedia.org/wiki/CSV_(file_format)
.. 
.. Los archivos de valores con separadores
.. son muy fáciles de leer y escribir, y por esto son muy usados.
.. Como ejemplo práctico,
.. si usted desea hacer un programa que analice los datos
.. de una hoja de cálculo Excel,
.. puede guardar el archivo con el formato CSV directamente en el Excel,
.. y luego abrirlo desde su programa escrito en Python.
.. 
.. Para leer los datos de un archivo de valores con separadores,
.. debe hacerlo línea por línea,
.. eliminar el salto de línea usando el método ``strip``
.. y luego extraer los valores de la línea usando el método ``split``.
.. Por ejemplo,
.. al leer la primera línea del archivo de más arriba
.. obtendremos el siguiente string::
.. 
.. 
..     'Perico:Los Palotes:90:75:38:65\n'
.. 
.. Para separar los seis valores,
.. lo podemos hacer así::
.. 
..     >>> linea.strip().split(':')
..     ['Perico', 'Los Palotes', '90', '75', '38', '65']
.. 
.. Como se trata de un archivo de texto,
.. todos los valores son strings.
.. Una manera de convertir los valores a sus tipos apropiados
.. es hacerlo uno por uno::
.. 
..     valores = linea.strip().split(':')
..     nombre   = valores[0]
..     apellido = valores[1]
..     nota1 = int(valores[2])
..     nota2 = int(valores[3])
..     nota3 = int(valores[4])
..     nota4 = int(valores[5])
.. 
.. Una manera más breve
.. es usar las rebanadas y la función ``map``::
.. 
..     valores = linea.strip().split(':')
..     nombre, apellido = valores[0:2]
..     nota1, nota2, nota3, nota4 = map(int, valores[2:6])
.. 
.. O podríamos dejar las notas en una lista,
.. en vez de usar cuatro variables diferentes::
.. 
..     notas = map(int, valores[2:6])
.. 
.. Por ejemplo,
.. un programa para imprimir el promedio de todos los alumnos
.. se puede escribir así::
.. 
..     archivo_alumnos = open('alumnos.txt')
..     for linea in archivo_alumnos:
..         valores = linea.strip().split(':')
..         nombre, apellido = valores[0:2]
..         notas = map(int, valores[2:6])
..         promedio = sum(notas) / 4.0
..         print '{0} obtuvo promedio {1}'.format(nombre, promedio)
..     archivo_alumnos.close()
.. 
.. Para escribir los datos en un archivo,
.. hay que hacer el proceso inverso:
.. convertir todos los datos al tipo string,
.. pegarlos en un único string,
.. agregar el salto de línea al final
.. y escribir la línea en el archivo.
.. 
.. Si los datos de la línea ya están en una lista o una tupla,
.. podemos convertirlos a string usando la función ``map``
.. y pegarlos usando el método ``join``::
.. 
..     alumno = ('Perico', 'Los Palotes', 90, 75, 38, 65)
..     linea = ':'.join(map(str, alumno)) + '\n'
..     archivo.write(linea)
.. 
.. Otra manera es armar el string parte por parte::
.. 
..     linea = '{0}:{1}:{2}:{3}:{4}:{5}\n'.format(nombre, apellido,
..                                                nota1, nota2, nota3, nota4)
..     archivo.write(linea)
.. 
.. Como siempre, usted debe preferir la manera
.. que le parezca más simple de entender.
