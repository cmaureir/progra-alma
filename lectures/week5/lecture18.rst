Lecture 18 - Higher-order functions
------------------------------------

List comprehensions
~~~~~~~~~~~~~~~~~~~

Remembering the *list* chapter,
we can learn an extra issue about the list iteration
structure, the list comprehensions.

A simple example of this new characteristic can be 
the following example, prevenient of the official python wiki,
in a section called `Performance Tips`_.

.. _`Performance Tips`: http://wiki.python.org/moin/PythonSpeed/PerformanceTips 

The main problem is that we have a list called *oldlist*
containing a lot of word with different cases (upper and lower case),
so we need to convert that words into only upper case words.

The simple initial solution will be::

    newlist = []
    for word in oldlist:
        newlist.append(word.upper())

So, using *list comprehensions*, the code will be::

    newlist = [s.upper() for s in oldlist]

Providing a more simple, efficient and compact way of writing the first version.

A *list comprehension* consist of an `expression` followed by a `for` statement,
then you can use any expressions like another `for` or `if` statement.


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


Function as parameters
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

One of the advantages of this characteristic is that is possible
to create functions which receive other functions as parameters.

In the following example, we define a function called `my_sum`
which return the sum of the values lower than `n`,
but before apply a function received with the `f` parameter.

The program call the function `my_sum` three times,
in each case a different function is given as parameter.
In this way, it is possible to use a unique function to calculate
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

There is possible to give additional iterable arguments,
but function must take  all the arguments and applied to the items
from the iterables in parallel.

If there are several arguments,
the function `map` return an entire list of tuples,
with the items from all iterables.::

    >>> def double(x):
    ...   return 2*x
    ... 
    >>> map(double,range(1,11))
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


It is possible to give more than one sequence,
but is important to give the same number of sequences as the function parameters:

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
will be very useful for simple tasks,
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

.. reduce(function, iterable[, initializer])
.. Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.
.. 
.. reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. For example, to compute the sum of the numbers 1 through 10:
.. 
.. >>> def add(x,y): return x+y
.. ...
.. >>> reduce(add, range(1, 11))
.. 55
.. If there’s only one item in the sequence, its value is returned; if the sequence is empty, an exception is raised.
.. 
.. A third argument can be passed to indicate the starting value. In this case the starting value is returned for an empty sequence, and the function is first applied to the starting value and the first sequence item, then to the result and the next item, and so on. For example,
.. 
.. >>> def sum(seq):
.. ...     def add(x,y): return x+y
.. ...     return reduce(add, seq, 0)
.. ...
.. >>> sum(range(1, 11))
.. 55
.. >>> sum([])
.. 0
.. Don’t use this example’s definition of sum(): since summing numbers is such a common need, a built-in function sum(sequence) is already provided, and works exactly like this.
.. 
.. 
.. 
.. 
.. 
.. The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, but it's not an iterator itself. It returns a single result:
.. 
.. >>> 
.. >>> from functools import reduce
.. >>> reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
.. 24
.. >>> reduce( (lambda x, y: x / y), [1, 2, 3, 4] )
.. 0.041666666666666664
.. >>> 
.. At each step, reduce passes the current product or division, along with the next item from the list, to the passed-in lambda function. By default, the first item in the sequence initialized the starting value. Here's the for loop version of the first of these calls, with the multiplication hardcoded inside the loop:
.. 
.. >>> L = [1, 2, 3, 4]
.. >>> result = L[0]
.. >>> for x in L[1:]:
.. 	result = result * x
.. 
.. 	
.. >>> result
.. 24
.. >>> 
.. Let's make our own version of reduce.
.. 
.. >>> def myreduce(fnc, seq):
.. 	tally = seq[0]
.. 	for next in seq[1:]:
.. 		tally = fnc(tally, next)
.. 	return tally
.. 
.. >>> myreduce( (lambda x, y: x * y), [1, 2, 3, 4])
.. 24
.. >>> myreduce( (lambda x, y: x / y), [1, 2, 3, 4])
.. 0.041666666666666664
.. >>> 
.. The built-in reduce also allows an optional third argument placed before the items in the sequence to serve as a default result when the sequence is empty.


`filter()` function
~~~~~~~~~~~~~~~~~~~~
.. 
.. filter(function, iterable)
.. Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If iterable is a string or a tuple, the result also has that type; otherwise it is always a list. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
.. 
.. Note that filter(function, iterable) is equivalent to [item for item in iterable if function(item)] if function is not None and [item for item in iterable if item] if function is None.
.. 
.. See itertools.ifilter() and itertools.ifilterfalse() for iterator versions of this function, including a variation that filters for elements where the function returns false.
.. 
.. 
.. 
.. 
.. filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list. For example, to compute primes up to 25:
.. 
.. >>> def f(x): return x % 2 != 0 and x % 3 != 0
.. ...
.. >>> filter(f, range(2, 25))
.. [5, 7, 11, 13, 17, 19, 23]
.. 
.. 
.. 
.. 
.. As an example, the following filter call picks out items in a sequence that are less than zero:
.. 
.. >>> list(range(-5,5))
.. [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
.. >>>
.. >>> list( filter((lambda x: x < 0), range(-5,5)))
.. [-5, -4, -3, -2, -1]
.. >>> 
.. Items in the sequence or iterable for which the function returns a true, the result are added to the result list. Like map, this function is roughly equivalent to a for loop, but it is built-in and fast:
.. 
.. >>> 
.. >>> result = []
.. >>> for x in range(-5, 5):
.. 	if x < 0:
.. 		result.append(x)
.. 
.. 		
.. >>> result
.. [-5, -4, -3, -2, -1]
.. >>> 
