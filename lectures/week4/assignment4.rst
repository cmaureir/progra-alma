Assignment 4
============

#. To do this assignment,
   you must download `el módulo con los datos`_
   que vamos a utilizar.
   
   .. _el módulo con los datos: ../../_static/personas.py
   
   para usar el módulo
   hay que guardarlo en la misma carpeta
   que se usará desde pyscripter,
   e importar los datos de esta forma::
   
       from personas import *
   
   este módulo contiene una lista llamada ``personas``
   que contiene tuplas que representan los datos de una persona.
   cada tupla tiene tres valores: el nombre, el apellido y la fecha de nacimiento.
   
   el nombre y el apellido son strings,
   y la fecha de nacimiento es una tupla de tres valores: el día, el mes y el año.
   
   por ejemplo,
   podemos ver los datos de la primera persona::
   
       >>> personas[0]
       ('martín', 'soto', (24, 8, 1990))

   para realizar estos ejercicios ,
   usted debe descargar `el módulo con los datos`_
   que vamos a utilizar.
   
   .. _el módulo con los datos: ../../_static/personas.py
   
   para usar el módulo
   hay que guardarlo en la misma carpeta
   que se usará desde pyscripter,
   e importar los datos de esta forma::
   
       from personas import *
   
   este módulo contiene una lista llamada ``personas``
   que contiene tuplas que representan los datos de una persona.
   cada tupla tiene tres valores: el nombre, el apellido y la fecha de nacimiento.
   
   el nombre y el apellido son strings,
   y la fecha de nacimiento es una tupla de tres valores: el día, el mes y el año.
   
   por ejemplo,
   podemos ver los datos de la primera persona::
   
       >>> personas[0]
       ('martín', 'soto', (24, 8, 1990))
   
   #. escriba una función que imprima el nombre de todas las personas.
      para eso, recorra la lista con un ``for``,
      obtenga el nombre de la persona
      e imprímalo usando ``print``.
      la función no tiene que retornar nada::
      
          >>> nombres(personas)
          martín
          gabriel
          humberto
          sebastián
          víctor
          ...
          horacio
          ignacio
          nicolás
          pablo
          rolando
          ricardo
     
   #. escriba una función que imprima la fecha de nacimiento de todas las personas::
      
        >>> fechas(personas)
        24 de agosto de 1990
        2 de junio de 1974
        14 de noviembre de 1973
        18 de septiembre de 1973
        12 de agosto de 1992
        ...
        18 de agosto de 1981
        24 de abril de 1972
        17 de mayo de 1977
        4 de febrero de 1972
        29 de enero de 1976
   
      para hacerlo más fácil,
      construya un diccionario con los nombres de los meses::
    
        meses = {
            1: 'enero',
            2: 'febrero',
            # ...
            12: 'diciembre',
        }
   
   #. realice una función llamada *cuantas_personas(lista)*
      para determinar la cantidad de personas que hay
      en la lista de personas.
   
   #. escriba una función que retorne una lista de personas
      que tengan cumpleaños el mismo día que usted::
    
        >>> mi_cumple(personas)
        ['jonathan sepúlveda']
   
   #. realice una función *cumples_repetidos(lista)*
      que pueda determinar las personas en la lista que
      tienen su cumpleaños el mismo día.
   
   #. realice una función *nombre_mas_comun(lista)*
      que sea capaz de determinar el nombre que más
      se repite en la lista de personas.
   
   #. realice una función *menor_mayor(lista)*
      para poder determinar a la persona más vieja y más joven
      de la lista.
