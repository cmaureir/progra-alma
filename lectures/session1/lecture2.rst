Lecture 2 - Data types
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

Integers
~~~~~~~~

.. index:: integer, int

The **int** type (from the word «integer»)
allows the representation of integer numbers.

The values an ``int`` can take are
all the integer numbers:
... ``-3``, ``-2``, ``-1``, ``0``, ``1``, ``2``, ``3``, ...

Literal integer numbers are written with an optional sign
followed by a sequence of digits::

   1570
   +4591
   -12

Reals
~~~~~

.. index:: real number, floating point number, float

The **float** type allows the representation of real numbers.

The name ``float`` comes from the term `floating point`_,
which is the internal representation of real numbers in a
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
are approximations.
This can produce surprising results::

    >>> 1/7 + 1/7 + 1/7 + 1/7 + 1/7 + 1/7 + 1/7
    0.9999999999999998

Literal real numbers are written by separating the decimal
and integer part with a point.
Both the integer and the decimal part can be omitted
when one of them is zero::

    >>> 881.9843000
    881.9843
    >>> -3.14159
    -3.14159
    >>> 1024.
    1024.0
    >>> .22
    0.22


.. index:: scientific notation

Another representation for real numbers is scientific notation,
in which the number is written as a factor and the exponent of a power 
of ten separated by the letter  ``e``.  For example::

    >>> -2.45E4
    -24500.0
    >>> 7e-2
    0.07
    >>> 6.02e23
    6.02e+23
    >>> 9.1094E-31
    9.1094e-31

The last two values of the previous example
are equal, respectively, to
:math:`6.02\times 10^{23}` (the `Avogadro constant`_) y
:math:`9.1094\times 10^{-31}` (the `electron mass`_).

.. _Avogadro constant: http://en.wikipedia.org/wiki/Avogadro_constant
.. _electron mass: http://en.wikipedia.org/wiki/Electron

