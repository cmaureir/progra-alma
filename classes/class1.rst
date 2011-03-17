Class 1 
=======

Data types
----------

.. index:: Data types

(`Python standard data types official documentation`_)

.. _Python standard data types official documentation: http://docs.python.org/library/stdtypes.html

A **data type** is the property of a value
that determine their domain (possible values),
what operations can be applied
and how is represented inside the computer.

All the values inside a program have a type.

Following we will review the Python elemental data types.
Also, there are several another types,
and later we will learn to create out own data types.

Integers
~~~~~~~~

.. index:: integer number, int

The **int** type (from the word «integer»)
allow the representation of the integer numbers.

The values that can take an ``int`` are
all the integer numbers:
... ``-3``, ``-2``, ``-1``, ``0``, ``1``, ``2``, ``3``, ...

The literal integer numbers writes with an optional sign
following by a digits sequence::

   1570
   +4591
   -12

Reals
~~~~~

.. index:: real number, floating point number, float

The **float** type allow to represent real numbers.

The name ``float`` comes from the term `floating point`_,
that is the way of the computer to represent internally
the real numbers.

.. _floating point: http://en.wikipedia.org/wiki/Floating_point

We need to be carefully,
because the real numbers cannot be represented
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

The literal real numbers
writes splitting the decimal and integer part
with a point.
The integer and decimal parts can be omitted
if some of them is zero::

    >>> 881.9843000
    881.9843
    >>> -3.14159
    -3.14159
    >>> 1024.
    1024.0
    >>> .22
    0.22


.. index:: scientific notation

Others representations is the scientific notation,
in which is written a factor and a power of ten
separated by a letter  ``e``.  For example:

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
with text between simple and doubles quotes::

   "example 1"
   'example 2'

The advantage of having two kinds of quotes
is that we can use one of them when the other
appear like a text part::

    "Let's go!"
    'She says "hello"'

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

Is important to understand that the strings
are not the same that the values inside
the self representation::

   >>> 5 == '5'
   False
   >>> True == 'True'
   False

The strings with lower and upper case differences,
or with blank spaces are not the same::

   >>> 'table' == 'Table'
   False
   >>> ' table' == 'table '
   False


Boolean
~~~~~~~

.. index:: bool, logic value, boolean value

The logic values ``True`` and ``False``
are of **bool** type, that represent logic values.

The name ``bool`` comes from the mathematician `George Boole`_,
who create an algebraic system to the binary logic.
For this reason,
the ``True`` and ``False`` values also are called
**boolean values**.
The name is not very clear,
but is very used in different sciences,
so we need to know.

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
where no value is valid,
or to indicate that a variable has not a values
that makes sense.

The ``None`` value has its own type,
called ``NoneType``,
that is different to all others.

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
in which the user enter data.

.. index:: raw_input

The most simplest way to enter data
is doing it throught the keyboard.
The ``raw_input(message)`` function
ask to the user to enter a value
that can be assigned to a variable
to be used by the program.
The ``message`` is to be displayed to the user
before that he enter the value.

The entered value by the user
always is interpreted as text,
so is of ``str`` type.
If is necessary use like other type,
we need to explicit converting.

For example,
in the temperatures conversion program,
the input is do it by the sentence::

    f = float(raw_input('Enter temperature in Fahrenheit degrees: '))

When the program comes to this line,
the message ``Enter temperature in Fahrenheit degrees:``
is showed to the user,
that must enter a value,
being converted into a real number
and associated to the ``f`` name.

From that line onward,
the ``f`` variable can be used by the program
to refer to the enter value.

Output
~~~~~~

.. index:: output (program)

The **output** is the program part
in which the results are delivered to the user.

.. index:: print

The simplest way to delivered the output
is showing text on the screen.
In Python, the program output is performed by the
**print** sentence.

If is desired print a simple text,
the syntax is as follows::

    print value_to_print

If the values to print are many,
must be put separating it with commas.
For example,
the temperature conversion program
has the following output sentence::

    print 'The Celsius degrees equivalent is:', c

In this case,
is being printing the message ``The Celsius degrees equivalent is:``
and next, in the same line,
the value of the ``c`` variable. 

The quotes just allow to represent in the code a string,
and are not of string.
When printing the string using ``print``
the quotes do not appear::

    >>> 'Hello'
    'Hello'
    >>> print 'Hello'
    Hello

Comments
~~~~~~~~

.. index:: comments, #

A **comment** is a code section
that is ignored by the interpreter.
A comment can be used by the programmer
to place some messages inside the code
that can be useful to someone that need to read it
in the future.

In Python,
any text that appears to the right of a ``#`` sign
is a comment::

    >>> 2 + 3  # This is a sum
    5
    >>> # This is ignored
    >>>

The exception are the ``#`` signs that appear in a string::

    >>> "123 # 456" # 789
    '123 # 456'

Assignment 1
------------

PENDING
