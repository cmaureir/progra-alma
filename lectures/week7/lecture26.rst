Lecture 26 - NumPy arrays (part II)
------------------------------------

Bi-dimensional Arrays
~~~~~~~~~~~~~~~~~~~~~~

.. index:: bi-dimensional array

The **bi-dimensional arrays**
are tables of values.
Each bi-dimensional array element
is simultaneously in a row and a column.

.. index:: matrix

In mathematics,
the bi-dimensional arrays are called matrices_,
and are widely used in engineering problems.

In a bi-dimensional array,
each element has a position
which is identified by two index:
its row and its column.

Creating Bi-dimensional Arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bi-dimensional arrays are also provided by NumPy,
so we should start importing the functions
of this module::

    from numpy import *

In the same way of one dimension array,
the bi-dimensional arrays can also be created
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
``a`` is a bi-dimensional array
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

.. index:: zeros (bi-dimensional), ones (bi-dimensional)

The ``zeros`` and ``ones`` functions
are also used to create bi-dimensional arrays.
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


Bi-dimensional Arrays Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Like a one dimension arrays,
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


Obtaining Bi-dimensional Arrays Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
.. index:: transposition, transpose

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

The ``diag`` function applied to a bi-dimensional array
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
it returns a bi-dimensional array
which has elements of the parameter on the diagonal::

    >>> diag(arange(5))
    array([[0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 2, 0, 0],
           [0, 0, 0, 3, 0],
           [0, 0, 0, 0, 4]])


Exercises
~~~~~~~~~~

* PENDING
