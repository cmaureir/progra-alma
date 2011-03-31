Lecture13 - Modules
-------------------

.. index:: module, library

A **module** (or **library**) is a collection of variable definition, 
functions and types (among other things) that can be imported 
to be used from any program. 

We have seen some examples of how to use modules,
particularly the mathematics module,
from which we can import functions
as the exponential, cosine,
and the constants π and *e*::

 >>> from math import exp, cos
 >>> from math import pi, e
 >>> print cos(pi / 3)
 0.5

The advantages of using modules are:

* The functions and variables must be defined only once,
  and then can be used in many programs, 
  without the need to rewrite the code;
* allows a program can be organized in several logic sections,
  each placed in separate file,
* make it easier to share components with other developers.

Python comes with many modules ready to be used.
Besides, it is possible download from Internet and install modules
practically to do anything.
Finally, we will learn to create ours own modules.


Modules from Python
~~~~~~~~~~~~~~~~~~~

These are some of the standard modules of Python,
can be used from any program.

The math_ module contains mathematical functions and constants::

 >>> from math import floor, radians
 >>> floor(-5.9)
 -6.0
 >>> radians(180)
 3.1415926535897931

The random_ module contains functions to produce random numbers::

 >>> from random import choice, randrange,
 >>> choice(['heads', 'tails'])
 'heads'
 >>> choice(['heads', 'tails'])
 'tails'
 >>> choice(['heads', 'tails'])
 'tails'
 >>> randrange(10)
 7
 >>> randrange(10)
 2
 >>> randrange(10)
 5
 >>> r = range(5)
 >>> r
 [0, 1, 2, 3, 4]
 >>> shuffle(r)
 >>> r
 [4, 2, 0, 3, 1]

The datetime_ module provides data types to
manipulate dates and times::

 >>> from datetime import date
 >>> today = date(2011, 5, 31)
 >>> end_of_the_world = date(2012, 12, 21)
 >>> (end_of_the_world - today).days
 570

The fractions_ module provides one data type to 
represent rationals numbers::

 >>> from fractions import Fraction
 >>> a = Fraction(5, 12)
 >>> b = Fraction(9, 7)
 >>> a + b
 Fraction(143, 84)

The turtle_ module allows to handle a turtle
(¡Try it!)::

 >>> from turtle import Turtle
 >>> t = Turtle()
 >>> t.forward(10)
 >>> t.left(45)
 >>> t.forward(20)
 >>> t.left(45)
 >>> t.forward(30)
 >>> for i in range(10):
 ... t.right(30)
 ... t.forward(10 * i)
 ...
 >>>

.. _math: http://docs.python.org/library/math.html
.. _random: http://docs.python.org/library/random.html
.. _datetime: http://docs.python.org/library/datetime.html
.. _fractions: http://docs.python.org/library/fractions.html
.. _turtle: http://docs.python.org/library/turtle.html

The complete list of Python modules can be found in the `standard library documentation`_.

.. _standard library documentation: http://docs.python.org/library/index.html

Name import
~~~~~~~~~~~
.. index:: import, module (use)

The ``import`` sentence import objects from a module
to be used in the current program.

One way to use ``import`` is importing only specific names
that you want to use in the program.::

 >>> from math import sin, cos
 >>> print sin(10)
 >>> print cos(20)


In these case, the ``sin`` and ``cos`` functions were not created by us,
but imported from math modules, which are defined.

The other way to use ``import`` is importing the entire module,
and accessing their objects by a point::

 >>> import math
 >>> print math.sin(10)
 >>> print math.cos(10)

The two cases are equivalent.
As always, we must choose the one that makes the program 
easier to understand.
