Lecture 25 - NumPy arrays (part I)
----------------------------------
 
Arrays
~~~~~~
lists, tuples, dictionary and sets
allow to manipulate data in a flexible way.
Combining and nesting,
is it possible to organize the information of structured way
to represent real world systems.

In many engineering applications, on the other hand,
most important than the data organization
is the capacity of perform many operations at once
over large sets of numerical data,
efficiently.
Some problems examples which require handling large sequences
of numbers are the following:
weather forecast,
building construction,
and the analysis of financial indicators,
among many others.

.. index:: array

The data structure used to store this large sequences
of numbers (usually ``float`` type) is the **array**.

The arrays have some similarities with the list:

* the elements (items) have an order and can be accessed by its position.
* the elements (items) can be traveled by a ``for`` cycle.

However,
they also have some restrictions:

* all the elements (items) of the array must have the same type,
* in general, the size of the array is fixed
  (they don’t grow dynamically as the lists),
* are primarily used to store numerical data.

At the same time,
arrays have many advantages over the lists,
which we will discover as we proceed in the course content. 

.. index:: matrix, vector

The arrays are equivalent in programming
to mathematics **matrix** and **vectors**.
Precisely,
a huge motivation to use arrays
is because there are many theories behind them
which can be used in the algorithm design
to solve really interesting problems.

Array Creation
~~~~~~~~~~~~~~
.. index:: NumPy

The module which provides data structures
and functions to work with arrays is called **NumPy**,
and is not included with Python,
so you have to install it separately.

.. index:: NumPy (download page)

Download the appropriate installer for your
Python version from the `NumPy download page`.
To see what version of Python you have installed,
see the first line that appears when you open a console,
for example:

::

    localhost~> python
    Python 2.7.2 (default, Jun 12 2011, 03:16:36) 
    [GCC 4.6.0 20110603 (prerelease)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

In this case, I have installed the 2.7 Python version.

.. _NumPy download Page: http://sourceforge.net/projects/numpy/files/NumPy/1.6.0/

To use the functions provided by NumPy,
we need to import at the beginning of the program
as a simple module::

    from numpy import array

Because we will use frequently a lot of this module functions,
is convenient to import all using the following statement::

    from numpy import *

.. index:: array

The data type of arrays is called ``array``.
To create a new array
we can use the ``array`` function
passing as parameter the list of values
which we want to add to the array::

    >>> a = array([6, 1, 3, 9, 8])
    >>> a
    array([6, 1, 3, 9, 8])

All the array elements
have exactly the same type.
To create a real number array,
is enough if only one of the values be a real number::

    >>> b = array([6.0, 1, 3, 9, 8])
    >>> b
    array([ 6.,  1.,  3.,  9.,  8.])

.. index:: astype

Another option is to convert the array to another type
using the ``astype`` method::

    >>> a
    array([6, 1, 3, 9, 8])
    >>> a.astype(float)
    array([ 6.,  1.,  3.,  9.,  8.])
    >>> a.astype(complex)
    array([ 6.+0.j,  1.+0.j,  3.+0.j,  9.+0.j,  8.+0.j])

.. index:: zeros, ones, arange, linspace

There are many array forms
which often appear in practice,
so there are special functions to create them:

* ``zeros(n)`` creates an array of ``n`` zeros;
* ``ones(n)`` creates an array of ``n`` ones;
* ``arange(a, b, c)`` creates an array is a similar way to the
  ``range`` function, with the difference that ``a``, ``b`` and ``c``
  can be real numbers, and that the result is an array and not a list;
* ``linspace(a, b, n)`` creates an array of ``n`` equally spaced
  between ``a`` and ``b``.

::

    >>> zeros(6)
    array([ 0.,  0.,  0.,  0.,  0.,  0.])

    >>> ones(5)
    array([ 1.,  1.,  1.,  1.,  1.])

    >>> arange(1.0, 9.0, 2)
    array([1., 3., 5., 7.])

    >>> arange(3.0, 9.0)
    array([ 3.,  4.,  5.,  6.,  7.,  8.])

    >>> linspace(1, 2, 5)
    array([ 1.  ,  1.25,  1.5 ,  1.75,  2.  ])
 

Arrays operations
~~~~~~~~~~~~~~~~~~

The limitations of the arrays
respect the lists are balanced by the amount of operations
which allow to realize over them.

.. index:: arrays (operations)

Arithmetic operations between arrays
are applied element by element::

    >>> a = array([55, 21, 19, 11,  9])
    >>> b = array([12, -9,  0, 22, -9])

    # add to arrays element-by-element
    >>> a + b
    array([67, 12, 19, 33,  0])

    # multiply element-by-element
    >>> a * b
    array([ 660, -189,    0,  242,  -81])

    # subtraction element-by-element
    >>> a - b
    array([ 43,  30,  19, -11,  18])

Operations between an array and a single value
works applying the operation
to all the array elements,
using simple value as operating every time::

    >>> a
    array([55, 21, 19, 11,  9])

    # multiply by 0.1 all the elements
    >>> 0.1 * a
    array([ 5.5,  2.1,  1.9,  1.1,  0.9])

    # subtract 9.0 to all the elements
    >>> a - 9.0
    array([ 46.,  12.,  10.,   2.,   0.])

If we want to do these operations using lists,
we need to use a cycle
to do the element by element operations.

The relational operations
are also applied element by element,
and return an array of boolean values::

    >>> a = array([5.1, 2.4, 3.8, 3.9])
    >>> b = array([4.2, 8.7, 3.9, 0.3])
    >>> c = array([5, 2, 4, 4]) + array([1, 4, -2, -1]) / 10.0

    >>> a < b
    array([False,  True,  True, False], dtype=bool)

    >>> a == c
    array([ True,  True,  True,  True], dtype=bool)

.. index:: any, all

To reduce the boolean array to a single value,
you can use ``any`` and ``all`` functions.
``any`` returns ``True`` if at least one element is true,
while ``all`` returns ``True`` only if all are true::

    >>> any(a < b)
    True
    >>> any(a == b)
    False
    >>> all(a == c)
    True

Functions over Arrays
~~~~~~~~~~~~~~~~~~~~~

NumPy provides many mathematical functions
which also operate element by element.
For example,
we can get *sine* of 9 values equally spaced
between 0 and *π*/2
with a single ``sin`` function call::

    >>> from numpy import linspace, pi, sin

    >>> x = linspace(0, pi/2, 9)
    >>> x
    array([ 0.        ,  0.19634954,  0.39269908,
            0.58904862,  0.78539816,  0.9817477 ,
            1.17809725,  1.37444679,  1.57079633])

    >>> sin(x)
    array([ 0.        ,  0.19509032,  0.38268343,
            0.55557023,  0.70710678,  0.83146961,
            0.92387953,  0.98078528,  1.        ])

As you can see,
the obtained values grow from 0 to 1,
which is exactly how it behaves the sine function
in the interval [0, *π*/2].

This is also evident another advantage of the arrays:
displaying or printing on the console,
the values are perfectly aligned.
With lists, this does not happen::

    >>> list(sin(x))
    [0.0, 0.19509032201612825, 0.38268343236508978, 0.5555702330
    1960218, 0.70710678118654746, 0.83146961230254524, 0.9238795
    3251128674, 0.98078528040323043, 1.0]


Random Arrays
~~~~~~~~~~~~~

The NumPy module contains other modules
which provide array additional functionality
and basic functions.

The ``numpy.random`` module provide
functions to create **random numbers**
(i.e. randomly generated),
of which the most used is the ``random`` function,
which provides a randomly generated array
uniformly distributed between 0 and 1::

    >>> from numpy.random import random

    >>> random(3)
    array([ 0.53077263,  0.22039319,  0.81268786])
    >>> random(3)
    array([ 0.07405763,  0.04083838,  0.72962968])
    >>> random(3)
    array([ 0.51886706,  0.46220545,  0.95818726])


Obtain Array Elements
~~~~~~~~~~~~~~~~~~~~~

Each array element has an index,
as well as the lists.
The first element has index 0.
Items can also be numbered
from end to beginning
using negative indexes.
The last element has index -1::

    >>> a = array([6.2, -2.3, 3.4, 4.7, 9.8])

    >>> a[0]
    6.2
    >>> a[1]
    -2.3
    >>> a[-2]
    4.7
    >>> a[3]
    4.7

An array section can be obtained
using the slice operator ``a[i:j]``.
The ``i`` and ``j`` indexes
indicate the range of values to be returned::

    >>> a
    array([ 6.2, -2.3,  3.4,  4.7,  9.8])
    >>> a[1:4]
    array([-2.3,  3.4,  4.7])
    >>> a[2:-2]
    array([ 3.4])

If the first index is omitted,
the slice starts from the beginning of the array.
If the second index is omitted,
the slice ends at the end of the array::

    >>> a[:2]
    array([ 6.2, -2.3])
    >>> a[2:]
    array([ 3.4,  4.7,  9.8])

A third index can indicate
how many items will be included in the result::

    >>> a = linspace(0, 1, 9)
    >>> a
    array([ 0.   ,  0.125,  0.25 ,  0.375,  0.5  ,  0.625,  0.75 ,  0.875,  1.   ])
    >>> a[1:7:2]
    array([ 0.125,  0.375,  0.625])
    >>> a[::3]
    array([ 0.   ,  0.375,  0.75 ])
    >>> a[-2::-2]
    array([ 0.875,  0.625,  0.375,  0.125])
    >>> a[::-1]
    array([ 1.   ,  0.875,  0.75 ,  0.625,  0.5  ,  0.375,  0.25 ,  0.125,  0.   ])

A simple way to remember how the slicing work
is to consider that the indexes do not refer to the elements,
but the spaces between the elements:

.. image:: ../../diagrams/indexes.png
   :align: center

::

    >>> b = array([17.41, 2.19, 10.99, -2.29, 3.86, 11.10])
    >>> b[2:5]
    array([ 10.99,  -2.29,   3.86])
    >>> b[:5]
    array([ 17.41,   2.19,  10.99,  -2.29,   3.86])
    >>> b[1:1]
    array([], dtype=float64)
    >>> b[1:5:2]
    array([ 2.19, -2.29])

Convenient Methods
~~~~~~~~~~~~~~~~~~

The array provides some useful methods that should know.

Methods ``min`` and ``max``,
returns the minimum and maximum array element
respectively::

    >>> a = array([4.1, 2.7, 8.4, pi, -2.5, 3, 5.2])
    >>> a.min()
    -2.5
    >>> a.max()
    8.4000000000000004

The ``argmin`` and ``argmax`` methods
return the position of the minimum and maximum value respectively::

    >>> a.argmin()
    4
    >>> a.argmax()
    2

The ``sum`` and ``prod`` methods returns
the sum and the product of the elements respectively::

    >>> a.sum()
    24.041592653589795
    >>> a.prod()
    -11393.086289208301



Exercises
~~~~~~~~~~

 * **Data transmission**

   In several digital communication systems, the data travel in a **serial** way,
   (i.e. one by one), and in fixed size bits blocks (values 0 or 1).
   The physical data transmission does not know of this blocks separation,
   and furthermore is necessary to use programs to separate and organize the receive data.
   
   The transmitted data is represented as arrays,
   which values are zeros and ones.
   
   #. A bits sequence can be interpreted as a decimal number.
      Each bit is associated to a power of two, starting from the last bit.
      For example, the 01001 sequence represent the decimal number 9, because:
   
      .. math::
   
        0\cdot2^4 +
        1\cdot2^3 +
        0\cdot2^2 +
        0\cdot2^1 +
        1\cdot2^0 = 9
   
      Write a function called ``decimal_number(data)`` which returns the
      decimal representation of a data array::
   
         >>> a = array([0, 1, 0, 0, 1])
         >>> decimal_number(a)
         9
   
   #. Suppose a block size of four bits.
      Write a function called ``valid_block(data)``
      which verify the data flow has a whole block size::
   
         >>> valid_block(array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]))
         True
         >>> valid_block(array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]))
         False
   
   #. Write a function called ``block_decode(data)``
      which return an array with the integer representation of each block.
      If a block is incomplete, this must be identified with the ``-1`` value::
   
         >>> a = array([0, 1, 0, 1])
         >>> b = array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0])
         >>> c = array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1])
         >>> block_decode(a)
         array([5])
         >>> block_decode(b)
         array([5, 7, 2])
         >>> block_decode(c)
         array([5, 7, 2, -1])
