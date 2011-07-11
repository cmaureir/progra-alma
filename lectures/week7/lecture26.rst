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
the bi-dimensional arrays are called matrix,
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

* *Bi-dimensional arrays creation*
 
  The ``arange`` function, return an array with numbers in the indicated range::
  
      >>> from numpy import arange
      >>> a = arange(12)
      >>> a
      array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
  
  Starting from an array  called ``a`` defined before,
  show how to obtain the following arrays of the simplest way::
  
      >>> # ???
      array([[ 0,  1,  2,  3],
             [ 4,  5,  6,  7],
             [ 8,  9, 10, 11]])
      >>> # ???
      array([[  0,   1,   4,   9],
             [ 16,  25,  36,  49],
             [ 64,  81, 100, 121]])
      >>> # ???
      array([[ 0,  4,  8],
             [ 1,  5,  9],
             [ 2,  6, 10],
             [ 3,  7, 11]])
      >>> # ???
      array([[ 0,  1,  2],
             [ 4,  5,  6],
             [ 8,  9, 10]])
      >>> # ???
      array([[ 11.5,  10.5,   9.5],
             [  8.5,   7.5,   6.5],
             [  5.5,   4.5,   3.5],
             [  2.5,   1.5,   0.5]])
      >>> # ???
      array([[100, 201, 302, 403],
             [104, 205, 306, 407],
             [108, 209, 310, 411]])
      >>> # ???
      array([[100, 101, 102, 103],
             [204, 205, 206, 207],
             [308, 309, 310, 311]])

* *Magic square*

  A `magic square`_ is a natural numbers disposal in a square table,
  so that the sums of each column, of each row and of each diagonal are the same.
  
  The most popular magic squares are those which has consecutive numbers from
  `1` to `n^2`, where `n` is the square rows and columns numbers (length).
  
  For example, the following example is a magic square with the `n = 4`.
  All their rows, columns and diagonal sums 34:
  
  .. image:: ../../diagrams/magic-square.png

  .. _magic square: http://en.wikipedia.org/wiki/Magic_square 
  
  #. Write a function which receive an integer square array of `n\times n`,
     and indicates if is conformed by the consecutive numbers from `1` to `n^2`::
  
       >>> from numpy import array
       >>> consecutive(array([[3, 1, 5],
       ...                     [4, 7, 2],
       ...                     [9, 8, 6]]))
       True
       >>> consecutive(array([[3, 1, 4],
       ...                     [4, 0, 2],
       ...                     [9, 9, 6]]))
       False
  
  #. Write a function which receive an array and indicates if is or not a magic square::
  
       >>> is_magic(array([[3, 1, 5],
       ...                  [4, 7, 2],
       ...                  [9, 8, 6]]))
       False
       >>> is_magic(array([[2, 7, 6],
       ...                  [9, 5, 1],
       ...                  [4, 3, 8]]))
       True
 
* *Matrix rotation*
 
  #. Write a function called ``rotation90(a)`` which return the ``a`` array
     rotated in 90 degrees, counter-clockwise::
  
        >>> a = arange(12).reshape((3, 4))
        >>> a
        array([[ 0,  1,  2,  3],
               [ 4,  5,  6,  7],
               [ 8,  9, 10, 11]])
        >>> rotation90(a)
        array([[ 3,  7, 11],
               [ 2,  6, 10],
               [ 1,  5,  9],
               [ 0,  4,  8]])
  
     There are two ways to do it:
     the long way (using nested loops)
     and the short way (using array operations).
     Try to do it in both ways.
  
  #. Write two functions called ``rotation180(a)`` and ``rotation270(a)``::
  
        >>> rotation180(a)
        array([[11, 10,  9,  8],
               [ 7,  6,  5,  4],
               [ 3,  2,  1,  0]])
        >>> rotation270(a)
        array([[ 8,  4,  0],
               [ 9,  5,  1],
               [10,  6,  2],
               [11,  7,  3]])
  
     There are three ways to do it:
     the long way (using nested loops),
     the short way (using array operations)
     and the clever one.
     Try to do it in three ways.
  
  #. Write a module called ``rotation.py`` which provides the three
     previous functions.
     Will be very useful in the following exercises::
  
        >>> from rotation import rotation90
        >>> a = array([[6, 3, 8],
        ...            [9, 2, 0]])
        >>> rotation90(a)
        array([[8, 0],
               [3, 2],
               [6, 9]])
 
* *Sudoku*

  The Sudoku is a puzzle which consist in fill a grid of `9 × 9`
  with the digits from 1 to 9, so that there is no repeat value
  in each row, in each column and in each `3 × 3` section
  marked by the thick lines.
  
  The unresolved Sudoku has some of the digits in some points on the grid.
  When the puzzle has been solved, all the box has a digit,
  and between all satisfied the listed conditions.
  
  .. image:: ../../diagrams/sudoku.png
  
  In a program,
  a solved Sudoku can be saved in a 9 × 9 array::
  
      from numpy import array
      sr = array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
                  [8, 5, 7, 2, 9, 3, 1, 4, 6],
                  [1, 3, 9, 4, 6, 8, 2, 7, 5],
                  [9, 7, 1, 3, 8, 5, 6, 2, 4],
                  [5, 4, 3, 7, 2, 6, 8, 1, 9],
                  [6, 8, 2, 1, 4, 9, 7, 5, 3],
                  [7, 9, 4, 6, 3, 2, 5, 8, 1],
                  [2, 6, 5, 8, 1, 4, 9, 3, 7],
                  [3, 1, 8, 9, 5, 7, 4, 6, 2]])
  
  Write a function called ``correct_solution(Sudoku)``
  which receive as parameter a 9 × 9 array, representing a solved Sudoku,
  and which indicates if the solution is correct (i.e. if there are no repeated elements
  in rows, columns and sections)::
  
      >>> correct_solution(s)
      True
      >>> s[0, 0] = 9
      >>> correct_solution(s)
      False
  
.. 2. (¡Difícil!).
..    Un sudoku sin resolver puede ser representado como un arreglo
..    donde las casillas vacías se marcan con el número cero::
.. 
..     s = array([[0, 2, 0, 5, 0, 1, 0, 9, 0],
..                [8, 0, 0, 2, 0, 3, 0, 0, 6],
..                [0, 3, 0, 0, 6, 0, 0, 7, 0],
..                [0, 0, 1, 0, 0, 0, 6, 0, 0],
..                [5, 4, 0, 0, 0, 0, 0, 1, 9],
..                [0, 0, 2, 0, 0, 0, 7, 0, 0],
..                [0, 9, 0, 0, 3, 0, 0, 8, 0],
..                [2, 0, 0, 8, 0, 4, 0, 0, 7],
..                [0, 1, 0, 9, 0, 7, 0, 6, 0]])
.. 
..    Escriba una función ``resolver(sudoku)``
..    que reciba un sudoku sin resolver
..    y retorne el sudoku resuelto::
.. 
..     >>> resolver(s)
..     array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
..            [8, 5, 7, 2, 9, 3, 1, 4, 6],
..            [1, 3, 9, 4, 6, 8, 2, 7, 5],
..            [9, 7, 1, 3, 8, 5, 6, 2, 4],
..            [5, 4, 3, 7, 2, 6, 8, 1, 9],
..            [6, 8, 2, 1, 4, 9, 7, 5, 3],
..            [7, 9, 4, 6, 3, 2, 5, 8, 1],
..            [2, 6, 5, 8, 1, 4, 9, 3, 7],
..            [3, 1, 8, 9, 5, 7, 4, 6, 2]])
.. 
..    Sugerencia: en vez de intentar resolver el sudoku completo,
..    intente resolver sólo algunas de las casillas
..    (las más sencillas).


* *Special matrix*

  #. A matrix called ``a`` is **symmetrical**
     if for all index ``i`` and ``j`` pair is satisfied the condition
     ``a[i, j] == a[j, i]``.
  
     Write a function called ``is_symmetrical(a)``
     which indicates if the ``a`` matrix is or not
     symmetrical.
  
     Write some symmetrical matrix and other
     non-symmetrical matrix to test the function.
  
  #. A matrix called ``a`` is **antisymmetric**
     if for all index ``i`` and ``j`` pair is satisfied the
     condition ``a[i, j] == -a[j, i]``
     (please note the minus sign).
  
     Write a function called ``is_antisymmetric(a)``
     which indicates if the ``a`` matrix is or not
     antisymmetric.
  
     Write some antisymmetric matrix and other
     non-antisymmetric matrix to test the function.
  
  #. A matrix called ``a`` is **diagonal**
     if all their elements which are not in the main diagonal
     has the zero value.
     For example,
     the following matrix is diagonal:
  
     .. math:: 
  
       \begin{bmatrix}
         9 & 0 & 0 & 0 \\
         0 & 2 & 0 & 0 \\
         0 & 0 & 0 & 0 \\
         0 & 0 & 0 & -1 \\
       \end{bmatrix}
  
     Write a function called ``is_diagonal(a)``
     which indicates if the matrix ``a`` is or not diagonal.
  
  #. A matrix called ``a`` is **upper triangular**
     if all their elements down the main diagonal
     has the zero value.
     For example,
     the following example is an upper triangular matrix:
  
     .. math:: 
  
       \begin{bmatrix}
         9 & 1 & 0 & 4 \\
         0 & 2 & 8 & -3 \\
         0 & 0 & 0 & 7 \\
         0 & 0 & 0 & -1 \\
       \end{bmatrix}
  
     Write a function called  ``upper_triangular(a)``
     which indicates if the matrix ``a`` is or not upper triangular.
  
  #. Is easy to understand the meaning of a
     matrix **lower triangular**.
     Write a function called ``lower_triangular(a)``.
     To do less work, you can use inside this function
     the previous function called ``upper_triangular()``.
  
  #. A matrix is **idempotent**
     if the result of the matrix product with itself
     is the same matrix.
     For example:
  
     .. math::
  
          \begin{bmatrix}
             2 & -2 & -4 \\
            -1 &  3 &  4 \\
             1 & -2 & -3 \\
          \end{bmatrix}
          \begin{bmatrix}
             2 & -2 & -4 \\
            -1 &  3 &  4 \\
             1 & -2 & -3 \\
          \end{bmatrix}
          =
          \begin{bmatrix}
             2 & -2 & -4 \\
            -1 &  3 &  4 \\
             1 & -2 & -3 \\
          \end{bmatrix}
  
     Write a function called ``is_idempotent(a)``
     which indicated if the ``a`` matrix is or not
     idempotent.
  
  #. Is said that two matrix *A* and *B* **commute**
     if the matrix product between *A* and *B*
     and between *B* and *A* are the same.
  
     For example, this both matrix commute:
  
     .. math::
  
         \begin{bmatrix}
           1 & 3 \\ 3 & 2 \\
         \end{bmatrix}
         \begin{bmatrix}
           -1 & 3 \\ 3 & 0 \\
         \end{bmatrix} =
         \begin{bmatrix}
           -1 & 3 \\ 3 & 0 \\
         \end{bmatrix}
         \begin{bmatrix}
           1 & 3 \\ 3 & 2 \\
         \end{bmatrix} =
         \begin{bmatrix}
           8 & 3 \\ 3 & 9 \\
         \end{bmatrix}
  
     Write a function called ``commute``
     which indicates if two matrix commute or not.
     Test your function with this examples::
  
         >>> a = array([[ 1, 3], [3, 2]])
         >>> b = array([[-1, 3], [3, 0]])
         >>> commute(a, b)
         True
         
         >>> a = array([[3, 1, 2], [9, 2, 4]])
         >>> b = array([[1, 7], [2, 9]])
         >>> commute(a, b)
         False
