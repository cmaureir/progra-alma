Lecture 14 - Modules creation
-----------------------------
.. index:: module (creation)

A simple module is simply a file with Python code.
The name of the file indicates which is the module name.

For example, we can create a file called ``parity.py``
which have functions related to the parity numbers.::

 def is_even(n):
    return n % 2 == 0

 def is_odd(n):
    return not es_par(n)

 def to_even(n):
    return range(0, n, 2)

In this case, the name of the module is ``parity``.
To use the functions in another program, the file ``parity.py`` must be
in the same folder that the program.

For example,
the ``show_even.py`` program can be 
written as follows::

 from parity import to_even

 n = int(raw_input('Enter an integer: '))
 print 'The even number to', n, 'are:'
 for i in to_even(n):
    print i

And the ``check_even.py`` program
can be written as follows::

 import parity

 n = int(raw_input('Enter an integer: '))
 if parity.is_even(n):
    print n, 'is even'
 else:
    print n, 'is odd'

As seen, both programs can use objects defined in the module 
simply by importing it.

Use modules as programs
~~~~~~~~~~~~~~~~~~~~~~~

A file with ``.py`` extension can be either a module or a program.
If is a module, it contains definitions that can be imported from a program or other module.
If is a program, it contains code to be executed.

Sometimes, a program also contains definitions
(for example, functions and variables)
which also may be useful from another program.
However, cannot be imported,
because by using the ``import`` statement
the full program will be executed.
What would happen in this case,
to run the second program,
also will run the first.

There is a trick to avoid this problem:
whenever there is code  being executed,
exist a variable called ``__name__``.
When is a program,
the value of this variable is ``__main__``,
while in the module,
is the module name.

Therefore, 
you can use the value of this variable to mark
the program part to be executed to run the file, 
but not to import it.

For example,
the following program converts 
measurement units of length:

.. literalinclude:: ../../_static/programs/unit_conversion.py

This program is useful by itself,
but also their four functions and 
constants ``km_per_mile`` and ``cm_per_inch``
might be useful for use in another program.

To put the body of the program inside 
of the ``if __name__ == '__main__'``,
the file can be use like a module.
If we did not do this,
whenever the other program import a function
will be executed the whole program.

Try it: `download the program`_ and run it.
Then, write another program to import some of the functions.
Next, do the same,
but removing the ``if`` statement.


.. _download the program: ../_static/programs/unit_conversion.py

Exercises
---------

#. Desarrolle un módulo llamado ``listas.py``
   que contenga las siguientes funciones.
   
   * Una función ``promedio(l)``,
     cuyo parámetro ``l`` sea una lista de números reales,
     y que entregue el promedio de los números::
   
       >>> promedio([7.0, 3.1, 1.7])
       3.933333333333333
       >>> promedio([1, 4, 9, 16])
       7.5
   
   * Una función ``cuadrados(l)``,
     que entregue una lista con los cuadrados
     de los valores de ``l``::
   
       >>> cuadrados([1, 2, 3, 4, 5])
       [1, 4, 9, 16, 25]
       >>> cuadrados([3.4, 1.2])
       [11.559999999999999, 1.44]
   
   * Una función ``mas_largo(palabras)``,
     cuyo parámetro ``palabras`` es una lista de strings,
     que entregue cuál es el string más largo::
   
       >>> mas_largo(['raton', 'hipopotamo', 'buey', 'jirafa'])
       'hipopotamo'
       >>> mas_largo(['****', '**', '********', '**'])
       '********'
   
     Si las palabras más largas son varias,
     basta que entregue una de ellas.

#. Para realizar estos ejercicios ,
   usted debe descargar `el módulo con los datos`_
   que vamos a utilizar.
   
   .. _el módulo con los datos: ../../_static/personas.py
   
   Para usar el módulo
   hay que guardarlo en la misma carpeta
   que se usará desde PyScripter,
   e importar los datos de esta forma::
   
       from personas import *
   
   Este módulo contiene una lista llamada ``personas``
   que contiene tuplas que representan los datos de una persona.
   Cada tupla tiene tres valores: el nombre, el apellido y la fecha de nacimiento.
   
   El nombre y el apellido son strings,
   y la fecha de nacimiento es una tupla de tres valores: el día, el mes y el año.
   
   Por ejemplo,
   podemos ver los datos de la primera persona::
   
       >>> personas[0]
       ('Martín', 'Soto', (24, 8, 1990))

   Para realizar estos ejercicios ,
   usted debe descargar `el módulo con los datos`_
   que vamos a utilizar.
   
   .. _el módulo con los datos: ../../_static/personas.py
   
   Para usar el módulo
   hay que guardarlo en la misma carpeta
   que se usará desde PyScripter,
   e importar los datos de esta forma::
   
       from personas import *
   
   Este módulo contiene una lista llamada ``personas``
   que contiene tuplas que representan los datos de una persona.
   Cada tupla tiene tres valores: el nombre, el apellido y la fecha de nacimiento.
   
   El nombre y el apellido son strings,
   y la fecha de nacimiento es una tupla de tres valores: el día, el mes y el año.
   
   Por ejemplo,
   podemos ver los datos de la primera persona::
   
       >>> personas[0]
       ('Martín', 'Soto', (24, 8, 1990))
   
   #. Escriba una función que imprima el nombre de todas las personas.
      Para eso, recorra la lista con un ``for``,
      obtenga el nombre de la persona
      e imprímalo usando ``print``.
      La función no tiene que retornar nada::
      
          >>> nombres(personas)
          Martín
          Gabriel
          Humberto
          Sebastián
          Víctor
          ...
          Horacio
          Ignacio
          Nicolás
          Pablo
          Rolando
          Ricardo
     
   #. Escriba una función que imprima la fecha de nacimiento de todas las personas::
      
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
   
      Para hacerlo más fácil,
      construya un diccionario con los nombres de los meses::
    
        meses = {
            1: 'enero',
            2: 'febrero',
            # ...
            12: 'diciembre',
        }
   
   #. Realice una función llamada *cuantas_personas(lista)*
      para determinar la cantidad de personas que hay
      en la lista de personas.
   
   #. Escriba una función que retorne una lista de personas
      que tengan cumpleaños el mismo día que usted::
    
        >>> mi_cumple(personas)
        ['Jonathan Sepúlveda']
   
   #. Realice una función *cumples_repetidos(lista)*
      que pueda determinar las personas en la lista que
      tienen su cumpleaños el mismo día.
   
   #. Realice una función *nombre_mas_comun(lista)*
      que sea capaz de determinar el nombre que más
      se repite en la lista de personas.
   
   #. Realice una función *menor_mayor(lista)*
      para poder determinar a la persona más vieja y más joven
      de la lista.
