Lecture 3 - Data types
----------------------

.. index:: Data types

(`Python standard data types official documentation`_)

.. _Python standard data types official documentation: http://docs.python.org/library/stdtypes.html

A **data type** is the property of a value
that defines its domain (possible values),
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

Exercises
~~~~~~~~~

1. Write a program that takes as input the radius of a circle
   and outputs its perimeter and its area::

    Enter radius: `5`
    Perimeter: 31.4
    Area: 78.5

2. Write a program that calculates the average of four grades
   input by the user::

    First grade: `55`
    Second grade: `71`
    Third grade: `46`
    Fourth grade: `87`
    Average: 64.75

3. Write a program that converts centimeters to inches.
   An inch is equal to 2.54 centimeters::

    Enter length: `45`
    45 cm = 17.7165 in
    Enter length: `13`
    13 cm = 5.1181 in

4. Write a program that receives as input
   the legs `a` and `b` of a right triangle,
   and outputs the length `c` of the hypotenuse,,
   given by the `Pythagorean theorem`_ `c^2=a^2+b^2`::

    Enter leg a: `7`
    Enter leg b: `5`
    Hypotenuse: 8.6023252670426267

.. _`Pythagorean theorem`: http://en.wikipedia.org/wiki/Pythagorean_theorem

5. Write a program that asks the user the current time `t` on the clock
   and an integer number of hours `h`,
   and outputs which time will the clock show
   in `h` hours from now::

    Current time: `3`
    Hour quantity: `5`
    In 5 hours, the clock will show 8 o'clock

    Current time: `11`
    Hour quantity: `43`
    In 43 hours, the clock will show 6 o'clock

6. A student wants to know the grade of a final test in a course
   to pass it.

   The average of the course is calculated as follows.

   .. math::

       G_C = \frac{(T1+T2+T3)}{3}

       G_F = G_C\cdot 0.7 + G_L\cdot 0.3


   Where `G_C` is the average of all tests,
   `G_L` is the laboratory average
   and `G_F` is the final grade.

   Write a program that asks the user the grades of the first two tests,
   and the laboratory grade,
   and shows the grade he needs in the final test
   to pass the course with a final grade of 60.

   .. testcase::

       Grade in test 1: `45`
       Grade in test 2: `55`
       Laboratory grade: `65`
       You need a 72 in the final test.

