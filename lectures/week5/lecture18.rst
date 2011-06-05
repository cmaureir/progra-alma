Lecture 18 - Higher-order functions
------------------------------------

List comprehension
~~~~~~~~~~~~~~~~~~~

Remembering the *list* chapter,
we can learn an extra topic about the list iteration
structure, the list comprehension.

A simple example of this new characteristic can be 
the following example, prevenient from the official python wiki,
in a section called `Performance Tips`_.

.. _`Performance Tips`: http://wiki.python.org/moin/PythonSpeed/PerformanceTips 

The main problem is that we have a list called *oldlist*
containing a lot of words with different cases (upper and lower case),
so we need to convert that words into only upper case words.

The simple initial solution would be::

    newlist = []
    for word in oldlist:
        newlist.append(word.upper())

So, using *list comprehensions*, the code would be::

    newlist = [s.upper() for s in oldlist]

Providing a more simple, efficient and compact way of writing the first version.

A *list comprehension* consists of an `expression` followed by a `for` statement
and then you can use any expressions like another `for` or `if` statement.


The result of the *list comprehension* will be the evaluation of the expression
in the context provided by the programmer.

To clarify the concept, lets look the following examples::

    >>> vector = [2,-4,5]
    >>> from math import pi
    >>> [pi*x for x in vector]
    [6.283185307179586, -12.566370614359172, 15.707963267948966]
    >>> [2*x for x in vector if abs(x) > 2]
    [-8, 10]
    >>> from math import e
    >>> [e*x for x in vector if x < 4]
    [5.43656365691809, -10.87312731383618]
    >>> [e*x for x in vector if abs(x) > 10]
    []

::

    >>> vector = [1,-1,4]
    >>> [[x,x**2] for x in vector]
    [[1, 1], [-1, 1], [4, 16]]

Be careful!

::

    >>> [x,x**2 for x in vector]
    File "<stdin>", line 1
       [x,x**2 for x in vector]
                  ^
    SyntaxError: invalid syntax

You can perform the same with `tuples`:

::

    >>> [(x, x**2) for x in vector]
    [(1, 1), (-1, 1), (4, 16)]

::

    >>> vec1 = [2, 4, 6]
    >>> vec2 = [4, 3, -9]
    >>> [x*y for x in vec1 for y in vec2]
    [8, 6, -18, 16, 12, -36, 24, 18, -54]
    >>> [x+y for x in vec1 for y in vec2]
    [6, 5, -7, 8, 7, -5, 10, 9, -3]
    >>> [vec1[i]*vec2[i] for i in range(len(vec1))]
    [8, 12, -54]


Functions as parameters
~~~~~~~~~~~~~~~~~~~~~~

In Python, the functions are values as any other kind of value.
For example, it is possible to create a new name with a simple assignation::

    >>> def multiplication(e1,e2):
    ...   return e1*e2
    ... 
    >>> multiplication(2,6)
    12
    >>> m = multiplication
    >>> m(2,6)
    12

One of the advantages of this characteristic is that it is possible
to create functions which receive other functions as parameters.

In the following example, we define a function called `my_sum`
which returns the sum of the values lower than `n`,
but before that, it applies a function received in the `f` parameter.

The program calls the function `my_sum` three times,
in each case a different function is given as parameter.
In this way, it is possible to use the same function to calculate
the sum of the values until 1000,
the sum of the squares until 1000
and the sum of the cubes until 1000.::

    def my_sum(n, f):
    	s = 0
    	for i in range(n):
    		s = s + f(i)
    	return s
    
    def identity(x):
    	return x
    
    def square(x):
    	return x ** 2
    
    def cube(x):
    	return x ** 3
    
    print my_sum(1000, identity)
    print my_sum(1000, square)
    print my_sum(1000, cube)

`map()` function
~~~~~~~~~~~~~~~~

The `map` structure is very simple::

    map(function,iterable, ...)

Which means, that each given element (of the iterable) will be passed through a function evaluation,
and returning a result list.

It is possible to give additional iterable arguments,
but the function must take all the arguments and be applied to the items
from the iterables in parallel.

If there are several arguments,
the function `map` returns an entire list of tuples,
with the items from all the iterables.::

    >>> def double(x):
    ...   return 2*x
    ... 
    >>> map(double,range(1,11))
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


It is possible to give more than one sequence,
but it is important to give the same number of sequences as the function parameters:

For example::

    >>> seq1 = range(8)
    >>> seq2 = range(10,90,10)
    >>> seq1
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> seq2
    [10, 20, 30, 40, 50, 60, 70, 80]
    >>> def add(x,y):
    ...   return x + y
    ... 
    >>> map(add, seq1, seq2)
    [10, 21, 32, 43, 54, 65, 76, 87]


Since it's a built-in function,
it will be very useful for simple tasks,
so `map` will be available any time.

For example, if we need to calculate the power of several
numbers::

    >>> pow(3,5)
    243
    >>> pow(2,10)
    1024
    >>> pow(3,11)
    177147
    >>> pow(4,12)
    16777216

we can easily do this simple task with the `map` function::

    >>> map(pow,[2, 3, 4], [10, 11, 12])
    [1024, 177147, 16777216]


`reduce()` function
~~~~~~~~~~~~~~~~~~~~

The `reduce` struct is::

    reduce(function, iterable[, initializer])

This function gives the possibility to apply a function of two arguments to the items of the iterable,
to obtain a final single value.

The evaluation of the function is from left to right,
taking the given elements,

for example if we want to substract a list of numbers,
like ``9,4,3,2``, the internal behaviour of the `reduce` function
would be::

    (((9-4)-3)-2) = 0

which is different result, in comparison to the substraction
of the list ``2,3,4,9``::

    (((2-3)-4)-9) = -14

So, the code would be::

    >>> def subs(x,y):
    ...   return x - y
    ... 
    >>> reduce(subs,[9,4,3,2])
    0
    >>> reduce(subs,[2,3,4,9])
    -14


If there is an optional initializer,
it is placed before the items of the iterable in the calculation,
and give us a default result if the iterable is empty.

Another simple example, would be to reduce a list of numbers
between 5 and 20, using a sum::

    >>> def add(x,y):
    ...   return x + y
    ... 
    >>> reduce(add, range(5,21))
    200

If there is only one item in the iterable sequence, its value
is returned::

    >>> reduce(add, [1])
    1

If the iterable sequence is empty,
an exception is raised.::

    >>> reduce(add, [])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: reduce() of empty sequence with no initial value

As we said previously, the initializer is a kind of safe-status
to avoid some weird behaviour, or just a default value to prevent
an exception::

    >>> def my_sum(seq):
    ...     return reduce(add, seq, 0)
    ...
    >>> my_sum(range(1, 11))
    55
    >>> my_sum([])
    0

`filter()` function
~~~~~~~~~~~~~~~~~~~~

The `filter` structure is::

    filter(function, iterable)

The main idea of the `filter` function is to construct a list from an initial ``iterable``,
but only with the elements which satisfies a condition inside the ``function``.

If the iterable has a special data type,
like `string` or `tuple` the result also has that type.

Another case is when the iterable is `None`,
assuming an indentity function,
all the elements of the iterable which are false are removed.

Remembering the *list comprehension* we can note two situations:

* ``filter(function, iterable)`` is equivalent to :

 * ``[item for item in iterable if function(item)]`` if function is `not` None, and
 * ``[item for item in iterable if item]`` if function is None.


For example,
if we need to determine the primes up to 20::

    >>> def primes(x):
    ...   return x % 2 != 0 and x % 3 != 0
    ...
    >>> filter(primes, range(0, 21))
    [5, 7, 11, 13, 17, 19]
    >>> [x for x in range(0, 21) if primes(x)]
    [1, 5, 7, 11, 13, 17, 19]

Exercises
~~~~~~~~~

* PENDING
* PENDING
* PENDING
