Lecture 1 
=========

Data types
----------

.. index:: Data types

(`Python standard data types official documentation`_)

.. _Python standard data types official documentation: http://docs.python.org/library/stdtypes.html

A **data type** is the property of a value
that determine its domain (possible values),
what operations can be applied to it
and how it is represented inside the computer.

All the values inside a program have a type.

Following we will review the Python elemental data types.
Also, we will learn several other types available in Python
and, later, we will learn to create our own data types.

Integers
~~~~~~~~

.. index:: integer number, int

The **int** type (from the word «integer»)
allows the representation of integer numbers.

The values that an ``int`` can take are
all the integer numbers:
... ``-3``, ``-2``, ``-1``, ``0``, ``1``, ``2``, ``3``, ...

The literal integer numbers are written with an optional sign
following by a sequence of digits::

   1570
   +4591
   -12

Reals
~~~~~

.. index:: real number, floating point number, float

The **float** type allow to represent real numbers.

The name ``float`` comes from the term `floating point`_,
which is an internal representation of real numbers in a
computer.

.. _floating point: http://en.wikipedia.org/wiki/Floating_point

We need to be careful,
because real numbers cannot be represented
exactly by a computer.
For example,
the decimal number 0.7
is represented internally by the computer
through the approximation 0.69999999999999996.
All the operations between  ``float`` values
are approaches.
This can produce surprising results::

    >>> 1/7 + 1/7 + 1/7 + 1/7 + 1/7 + 1/7 + 1/7
    0.9999999999999998

Literal real numbers are written splitting the decimal
and integer part with a point.
Either the integer or decimal part can be omitted
if one of them is zero::

    >>> 881.9843000
    881.9843
    >>> -3.14159
    -3.14159
    >>> 1024.
    1024.0
    >>> .22
    0.22


.. index:: scientific notation

Other representation is the scientific notation,
in which the number is written with a factor and a power 
of ten separated by the letter  ``e``.  For example:

    >>> -2.45E4
    -24500.0
    >>> 7e-2
    0.07
    >>> 6.02e23
    6.02e+23
    >>> 9.1094E-31
    9.1094e-31

The last two values of the previous example
are the same, respectively, to
:math:`6.02\times 10^{23}` (la `Avogadro constant`_) y
:math:`9.1094\times 10^{-31}` (la `Electron mass`_).

.. _Avogadro constant: http://en.wikipedia.org/wiki/Avogadro_constant
.. _Electron mass: http://en.wikipedia.org/wiki/Electron

Strings
~~~~~~~

.. index:: string, text data types, str

**Strings** is the name of the values that
represent text and have the **str** type.

The literal strings
can be represented
with text between simple or double quotes::

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
are of **bool** type, which represents logic values.

The name ``bool`` comes from the mathematician `George Boole`_,
who created an algebraic system for binary logic.
For this reason,
the ``True`` and ``False`` values are also called
**boolean values**.
The name is not very intuitive, but we need to know it because
it is widely used in different areas of science.

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

Input and output
----------------

(`Python input and output official documentation`_)

.. _Python input and output official documentation: http://docs.python.org/tutorial/inputoutput.html

Input
~~~~~

.. index:: input (program)

The **input** is the program part
in which the user enters data.

.. index:: raw_input

The simplest way to enter data
is doing it through the keyboard.
The ``raw_input(message)`` function
asks the user to enter a value
that can be assigned to a variable
to be used by the program.
The ``message`` is to be displayed to the user
before that he enters a value.

The input value provided by the user
is always interpreted as text
as a value of type ``str``.
If a different type is required,
we need to convert it explicitly.

For example,
in the temperature conversion program,
the input is converted with the sentence::

    f = float(raw_input('Enter temperature in Fahrenheit degrees: '))

When the program gets to this line,
the message ``Enter temperature in Fahrenheit degrees:``
is shown to the user that must enter a value,
which is converted into a real number
and associated to the name ``f``.

From that line onward,
the ``f`` variable can be used by the program
to refer to the entered value.

Output
~~~~~~

.. index:: output (program)

The **output** is the program part
in which the results are delivered to the user.

.. index:: print

The simplest way to deliver the output
is showing text on the screen.
In Python, the program output is performed by the
**print** sentence.

If printing simple text is desired,
the syntax is as follows::

    print value_to_print

If there are several values to print,
they should be separated with commas.
For example the temperature conversion program
has the following output sentence::

    print 'The Celsius degrees equivalent is:', c

In this case, the message ``The Celsius degrees equivalent is:``
is being printed and, after that, in the same line,
the value of the variable ``c``.

The quotation marks allow to represent a string but are not part of it.
When printing the string using ``print`` the quotation marks do not appear::

    >>> 'Hello'
    'Hello'
    >>> print 'Hello'
    Hello

Comments
~~~~~~~~

.. index:: comments, #

A **comment** is a section of code
that is ignored by the interpreter.
A comment can be used by the programmer
to place messages in the code that can be useful
to someone that needs to read the code
in the future.

In Python,
any text that appears to the right of a ``#`` sign
is a comment::

    >>> 2 + 3  # This is a sum
    5
    >>> # This is ignored
    >>>

The only exception are the ``#`` signs that appear in a string::

    >>> "123 # 456" # 789
    '123 # 456'

Assignment 1
------------

PENDING
