Lecture 4 - Data types
----------------------

.. index:: Data types

(`Python standard data types official documentation`_)

.. _Python standard data types official documentation: http://docs.python.org/library/stdtypes.html

A **data type** is the property of a value
that define its domain (possible values),
what operations can be applied to it
and how it is represented by the computer.

All the values in a program have a type.

Below we will review the Python elemental data types.
Later in this course, we will learn several other types available in Python
and, finally, we will learn how to create our own data types.

Strings
~~~~~~~

.. index:: string, text data types, str

A **strings** is a value that
represents text, and whose type is **str**.

The literal strings
are represented in a program
by enclosing it in single or double quotes::

   "example 1"
   'example 2'

The advantage of having two kinds of quotes
is that we can use one of them when the other
appears in the text::

    "Let's go!"
    'She said "hello"'

.. Los operadores aritméticos no pueden ser aplicadas sobre strings,
.. salvo dos excepciones:
.. 
.. 1. El operador ``+`` aplicado a dos strings
..    no representa la suma,
..    sino la **concatenación**,
..    que significa pegar los strings
..    uno después del otro::
.. 
..        >>> "hola " + 'mundo'
..        'hola mundo'
.. 
.. 2. El operador ``*`` aplicado a un string y a un número entero
..    no representa la multiplicación,
..    sino la **repetición**,
..    es decir, el string es repetido tantas veces como indica el número::
.. 
..        >>> "lo" * 5
..        'lololololo'
.. 
.. Las operaciones relacionales permiten comparar strings alfabéticamente::
.. 
..     >>> "ala" < "alamo" < "bote" < "botero" < "boteros" < "zapato"
..     True
.. 
.. Para conocer el largo de un string,
.. se utiliza la función ``len()``::
.. 
..     >>> len('universidad')
..     11
.. 
.. La función ``input()``,
.. que usamos para leer la entrada del usuario,
.. siempre entrega como resultado un string.
.. Hay que tener la precaución
.. de convertir los valores que entrega
.. al tipo adecuado.
.. Por ejemplo,
.. el siguiente programa tiene
.. un error de incompatibilidad de tipos::
.. 
..     n = input('Escriba un número:')
..     cuadrado = n * n
..     print('El cuadrado de n es', cuadrado)

It is important to understand that strings
are not the same as the values that can be represented 
inside them::

   >>> 5 == '5'
   False
   >>> True == 'True'
   False

The strings with lower and upper case differences 
(case sensitive), or with blank spaces are not the same::

   >>> 'table' == 'Table'
   False
   >>> ' table' == 'table '
   False


Boolean
~~~~~~~

.. index:: bool, logic value, boolean value

The logic values ``True`` and ``False``
have type **bool**, which represents logic values.

The type ``bool`` is named after the mathematician `George Boole`_,
who created an algebraic system for binary logic.
For this reason,
the ``True`` and ``False`` values are also called
**boolean values**.
The name is not very intuitive, but we need to know it because
it is very used in computer programming.

.. _George Boole: http://en.wikipedia.org/wiki/George_Boole

.. Las operaciones lógicas ``and``, ``or`` y ``not``
.. pueden ser aplicadas sobre valores booleanos,
.. y entregan como resultado un valor booleano::
.. 
..     >>> not True or (True and False)
..     False
.. 
.. Las operaciones relacionales
.. ``<``, ``>``, ``==``, etc.,
.. pueden ser aplicadas sobre valores de tipos comparables,
.. pero siempre entregan como resultado un valor booleano::
.. 
..     >>> 2 + 2 == 5
..     False
..     >>> x = 95.4
..     >>> 50 < x < 100
..     True


None
~~~~

.. index:: null type, None

There is a value called  **None**
which is used to represent cases
where no value is valid
or to indicate that the current value of a
variable does not make sense.

The ``None`` value has its own type,
called ``NoneType``,
which is different to all other values.

.. Conversión de tipos
.. -------------------
.. .. index:: conversión de tipos
.. 
.. Los tipos de los valores
.. indican qué operaciones pueden ser aplicadas sobre ellos.
.. 
.. A veces es necesario convertir valores de un tipo a otro
.. para poder operar sobre ellos.
.. Existen dos tipos de conversiones:
.. implícitas y explícitas.
.. 
.. Las conversiones implícitas
.. son las que se hacen automáticamente
.. según el contexto.
.. Las más importantes son las siguientes:
.. 
.. * cuando se utiliza un entero
..   en un contexto real,
..   el entero es convertido al real correspondiente::
.. 
..       >>> 56 * 8.0
..       448.0
.. 
.. * cuando se utiliza cualquier valor
..   en un contexto booleano,
..   es convertido al valor ``True``,
..   excepto por los siguientes casos,
..   en que es convertido al valor ``False``:
.. 
..   * el valor ``0``,
..   * el string vacío ``''``,
..   * ``None``.
.. 
..   Por ejemplo::
.. 
..       >>> not 0
..       True
..       >>> not 10
..       False

..       >>> not 'hola'
..       False
..       >>> bool(3.14)
..       True
.. 
..   Con los operadores ``and`` y ``or``
..   ocurre algo más extraño::
.. 
..       >>> 4 and 7
..       7
..       >>> 0 and 7
..       0
..       >>> 5 or 6
..       5
..       >>> 0 or 6 or 7
..       6


Exercises
~~~~~~~~~

PENDING
