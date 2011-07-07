Lecture 25 - NumPy arrays (part I)
----------------------------------
 
Arrays
~~~~~~
(lists, tuples, dictionary, sets)
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

.. index:: arreglos (operaciones)

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

    # substraction element-by-element
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

    # substract 9.0 to all the elements
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

.. **********************************************

Random Arrays
~~~~~~~~~~~~~

The NumPy module contains other modules
which provide array additional functionalities
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


Bidimensional Arrays
~~~~~~~~~~~~~~~~~~~~

.. index:: bidimensional array

The **bidimensional arrays**
are tables of values.
Each bidimensional array element
is simultaneously in a row and a column.

.. index:: matrix

In mathematics,
the bidimensional arrays are called matrices_,
and are widely used in engineering problems.

In a bidimensional array,
each element has a position
which is identified by two index:
its row and its column.

Creating Bidimensional Arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bidimensional arrays are also provided by NumPy,
so we should start importing the functions
of this module::

    from numpy import *

In the same way of one dimension array,
the bidimensional arrays can also be created
using the ``array`` function,
but passing as arguments
a list with the rows of the matrix::

    a = array([[5.1, 7.4, 3.2, 9.9],
               [1.9, 6.8, 4.1, 2.3],
               [2.9, 6.4, 4.3, 1.4]])

All the rows must be of the same length,
or a value error will occurs::

    >>> array([[1], [2, 3]])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: setting an array element with a sequence.

.. index:: shape

The arrays have an attribute called ``shape``,
which is a tuple with the sizes of each dimension.
In the example,
``a`` is a bidimensional array
which has three rows and four columns::

    >>> a.shape
    (3, 4)

.. index:: size

The arrays also have another attribute called ``size``
which indicates how many items have the array::

    >>> a.size
    12

Of course, the value of ``a.size`` is always the product
of the ``a.shape`` elements.

Be careful with the ``len`` function,
because that does not return the array size,
but its number of rows::

    >>> len(a)
    3

.. index:: zeros (bidimensional), ones (bidimensional)

The ``zeros`` and ``ones`` functions
are also used to create bidimensional arrays.
Rather than pass an integer as an argument,
you have to give them a tuple
with the numbers of rows and columns
that will have the matrix::
    
    >>> zeros((3, 2))
    array([[ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.]])

    >>> ones((2, 5))
    array([[ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.]])

The same is true for many other functions
which create arrays,
for example the ``random`` function::

    >>> from numpy.random import random
    >>> random((5, 2))
    array([[ 0.80177393,  0.46951148],
           [ 0.37728842,  0.72704627],
           [ 0.56237317,  0.3491332 ],
           [ 0.35710483,  0.44033758],
           [ 0.04107107,  0.47408363]])


Bidimensional Arrays Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Like a one dimenson arrays,
operations on matrices
are applied term by term::

    >>> a = array([[5, 1, 4],
    ...            [0, 3, 2]])
    >>> b = array([[2, 3, -1],
    ...            [1, 0, 1]])

    >>> a + 2
    array([[7, 3, 6],
           [2, 5, 4]])

    >>> a ** b
    array([[25,  1,  0],
          [ 0,  1,  2]])

When two matrices are in operation,
both must have exactly the same form::

    >>> a = array([[5, 1, 4],
    ...            [0, 3, 2]])
    >>> b = array([[ 2,  3],
    ...            [-1,  1],
    ...            [ 0,  1]])
    >>> a + b
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: shape mismatch: objects cannot be broadcast to a single shape


Obtaining Bidimensional Arrays Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To obtain an element of an array,
must be indicated in its index of their ``i-th`` row and its ``j-th`` column
using the syntax  ``a[i,j]``::

    >>> a = array([[ 3.21,  5.33,  4.67,  6.41],
                   [ 9.54,  0.30,  2.14,  6.57],
                   [ 5.62,  0.54,  0.71,  2.56],
                   [ 8.19,  2.12,  6.28,  8.76],
                   [ 8.72,  1.47,  0.77,  8.78]])
    >>> a[1, 2]
    2.14

    >>> a[4, 3]
    8.78

    >>> a[-1, -1]
    8.78

    >>> a[0, -1]
    6.41

You can also get rectangular sections of the array
using slicing operator with index::

    >>> a[2:3, 1:4]
    array([[ 0.54,  0.71,  2.56]])

    >>> a[1:4, 0:4]
    array([[ 9.54,  0.3 ,  2.14,  6.57],
           [ 5.62,  0.54,  0.71,  2.56],
           [ 8.19,  2.12,  6.28,  8.76]])

    >>> a[1:3, 2]
    array([ 2.14,  0.71])

    >>> a[0:4:2, 3:0:-1]
    array([[ 6.41,  4.67,  5.33],
           [ 2.56,  0.71,  0.54]])

    >>> a[::4, ::3]
    array([[ 3.21,  6.41],
           [ 8.72,  8.78]])

To obtain an entire row,
you must indicate the row index,
and put a ``:`` in the column place
(meaning "from the beginning to the end").
Same for the columns::

    >>> a[2, :]
    array([ 5.62,  0.54,  0.71,  2.56])

    >>> a[:, 3]
    array([ 6.41,  6.57,  2.56,  8.76,  8.78])


The number of dimensions
is equals to the number of slices
which are in the index::

    >>> a[2, 3]      # scalar value (zero dimension array)
    2.56

    >>> a[2:3, 3]    # one dimension array of one element
    array([ 2.56])

    >>> a[2:3, 3:4]  # two dimension array of 1 x 1
    array([[ 2.56]])


Other Operations
~~~~~~~~~~~~~~~~
.. index:: trasposition, transpose

The **transposition** is changing rows by columns and vice versa.
To transpose an array,
is used the ``transpose`` method::

    >>> a
    array([[ 3.21,  5.33,  4.67,  6.41],
           [ 9.54,  0.3 ,  2.14,  6.57],
           [ 5.62,  0.54,  0.71,  2.56]])

    >>> a.transpose()
    array([[ 3.21,  9.54,  5.62],
           [ 5.33,  0.3 ,  0.54],
           [ 4.67,  2.14,  0.71],
           [ 6.41,  6.57,  2.56]])

.. index:: reshape

The ``reshape`` method
returns an array which has the same elements but in a different way.
The ``reshape`` parameter is a tuple
indicating the new way of arrangement:

    >>> a = arange(12)
    >>> a
    array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    >>> a.reshape((4, 3))
    array([[ 0, 1, 2],
           [ 3, 4, 5],
           [ 6, 7, 8],
           [ 9, 10, 11]])

    >>> a.reshape((2, 6))
    array([[ 0, 1, 2, 3, 4, 5],
           [ 6, 7, 8, 9, 10, 11]])

.. index:: diag

The ``diag`` function applied to a bidimensional array
provide the main diagonal of the matrix
(i.e. all elements of the form ``a[i, i]``)::

    >>> a
    array([[ 3.21,  5.33,  4.67,  6.41],
           [ 9.54,  0.3 ,  2.14,  6.57],
           [ 5.62,  0.54,  0.71,  2.56]])

    >>> diag(a)
    array([ 3.21,  0.3 ,  0.71])

In addition, ``diag`` receives an optional second parameter
to indicate another diagonal which is desired.
The diagonal over the main are positive,
and those under are negative::

    >>> diag(a, 2)
    array([ 4.67,  6.57])
    >>> diag(a, -1)
    array([ 9.54,  0.54])

The same ``diag`` function also fulfills the reverse role:
to receive an array of one dimension,
it returns a bidimensional array
which has elements of the parameter on the diagonal::

    >>> diag(arange(5))
    array([[0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 2, 0, 0],
           [0, 0, 0, 3, 0],
           [0, 0, 0, 0, 4]])

Excercises
~~~~~~~~~~
.. 
.. 
.. Transmisión de datos
.. ====================
.. 
.. .. Ejercicio propuesto por Claudio Price
.. 
.. En varios sistemas de comunicaciones digitales
.. los datos viajan de manera serial
.. (es decir, uno tras otro),
.. y en bloques de una cantidad fija de bits (valores 0 o 1).
.. La transmisión física de los datos
.. no conoce de esta separación por bloques,
.. y por lo tanto es necesario que haya programas
.. que separen y organicen los datos recibidos.
.. 
.. Los datos transmitidos los representaremos
.. como arreglos cuyos valores son ceros y unos.
.. 
.. #. Una secuencia de bits puede interpretarse
..    como un número decimal.
..    Cada bit está asociado a una potencia de dos,
..    partiendo desde el último bit.
..    Por ejemplo, la secuencia 01001 representa
..    al número decimal 9, ya que:
.. 
..    .. math::
.. 
..      0\cdot2^4 +
..      1\cdot2^3 +
..      0\cdot2^2 +
..      0\cdot2^1 +
..      1\cdot2^0 = 9
.. 
..    Escriba la función ``numero_decimal(datos)``
..    que entregue la representación decimal
..    de un arreglo de datos::
.. 
..       >>> a = array([0, 1, 0, 0, 1])
..       >>> numero_decimal(a)
..       9
.. 
.. #. Suponga que el tamaño de los bloques
..    es de cuatro bits.
..    Escriba la función ``bloque_valido(datos)``
..    que verifique que la corriente de datos
..    tiene una cantidad entera de bloques::
.. 
..       >>> bloque_valido(array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]))
..       True
..       >>> bloque_valido(array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]))
..       False
.. 
.. #. Escriba la función ``decodificar_bloques(datos)``
..    que entregue un arreglo
..    con la representación entera de cada bloque.
..    Si un bloque está incompleto,
..    esto debe ser indicado con el valor ``-1``::
.. 
..       >>> a = array([0, 1, 0, 1])
..       >>> b = array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0])
..       >>> c = array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1])
..       >>> decodificar_bloques(a)
..       array([5])
..       >>> decodificar_bloques(b)
..       array([5, 7, 2])
..       >>> decodificar_bloques(c)
..       array([5, 7, 2, -1])
.. Creación de arreglos bidimensionales
.. ====================================
.. 
.. La función ``arange`` retorna un arreglo
.. con números en el rango indicado::
.. 
..     >>> from numpy import arange
..     >>> a = arange(12)
..     >>> a
..     array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
.. 
.. A partir del arreglo ``a`` definido arriba,
.. indique cómo obtener los siguientes arreglos
.. de la manera más simple que pueda::
.. 
..     >>> # ???
..     array([[ 0,  1,  2,  3],
..            [ 4,  5,  6,  7],
..            [ 8,  9, 10, 11]])
..     >>> # ???
..     array([[  0,   1,   4,   9],
..            [ 16,  25,  36,  49],
..            [ 64,  81, 100, 121]])
..     >>> # ???
..     array([[ 0,  4,  8],
..            [ 1,  5,  9],
..            [ 2,  6, 10],
..            [ 3,  7, 11]])
..     >>> # ???
..     array([[ 0,  1,  2],
..            [ 4,  5,  6],
..            [ 8,  9, 10]])
..     >>> # ???
..     array([[ 11.5,  10.5,   9.5],
..            [  8.5,   7.5,   6.5],
..            [  5.5,   4.5,   3.5],
..            [  2.5,   1.5,   0.5]])
..     >>> # ???
..     array([[100, 201, 302, 403],
..            [104, 205, 306, 407],
..            [108, 209, 310, 411]])
..     >>> # ???
..     array([[100, 101, 102, 103],
..            [204, 205, 206, 207],
..            [308, 309, 310, 311]])
.. Cuadrado mágico
.. ===============
.. 
.. Un `cuadrado mágico`_ es una disposición de números naturales
.. en una tabla cuadrada, de modo que las sumas de cada columna,
.. de cada fila y de cada diagonal son iguales.
.. 
.. Los cuadrados mágicos más populares
.. son aquellos que tienen los números consecutivos desde el 1 hasta `n^2`,
.. donde `n` es el número de filas y de columnas del cuadrado.
.. 
.. Por ejemplo, el siguiente es un cuadrado mágico
.. con `n = 4`. Todas sus filas, columnas y diagonales suman 34:
.. 
.. .. image:: ../../diagramas/cuadrado-magico.png
.. 
.. #. Escriba una función que reciba un arreglo cuadrado de enteros de `n\times n`,
..    e indique si está conformado por los números consecutivos
..    desde 1 hasta `n^2`::
.. 
..      >>> from numpy import array
..      >>> consecutivos(array([[3, 1, 5],
..      ...                     [4, 7, 2],
..      ...                     [9, 8, 6]]))
..      True
..      >>> consecutivos(array([[3, 1, 4],
..      ...                     [4, 0, 2],
..      ...                     [9, 9, 6]]))
..      False
.. 
.. #. Escriba una función que reciba un arreglo
..    e indique si se trata o no de un cuadrado mágico::
.. 
..      >>> es_magico(array([[3, 1, 5],
..      ...                  [4, 7, 2],
..      ...                  [9, 8, 6]]))
..      False
..      >>> es_magico(array([[2, 7, 6],
..      ...                  [9, 5, 1],
..      ...                  [4, 3, 8]]))
..      True
.. 
