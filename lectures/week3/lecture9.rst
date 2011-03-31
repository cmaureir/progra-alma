Lecture 9 - Lists
-----------------

.. index:: list

A **list** is an ordered collection of values.

In Python, the data type which represents lists is called
``list``.

How to create a ``list``
~~~~~~~~~~~~~~~~~~~~~~~~

The two main ways to create a list, are:

* use a literal list, with the values in brackets, separated by commas::

    >>> ['hello ' + 'world', 24 * 7, True or False]
    ['hello world', 168, True]
    >>> primes = [2, 3, 5, 7, 11]
    >>> primes
    [2, 3, 5, 7, 11]
    >>> []
    []

* use the ``list`` function applied over an iterable::

    >>> list('hello')
    ['h', 'e', 'l', 'l', 'o']
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list()
    []

``list`` operations
~~~~~~~~~~~~~~~~~~~

* ``len(l)`` return the length of the list;
  i.e. how many elements it has::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> len(colors)
    4
    >>> len([True, True, True])
    3
    >>> len([])
    0

* ``l[i]`` return the ``i``-th value of the list.
  The ``i`` value is called **index** of the value.
  Be careful, because it starts counting from 0
  and not from 1::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> colors[0]
    'blue'
    >>> colors[3]
    'yellow'

  If the ``i`` index indicates an item which is not in the list,
  then an **index error** occurs::

    >>> colors[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

  If the index is negative,
  the item counts from the end backwards::

    >>> colors[-1]
    'yellow'
    >>> colors[-4]
    'blue'

* ``l.append(x)`` adds the ``x`` item to the end of the list::

    >>> primes = [2, 3, 5, 7, 11]
    >>> primes.append(13)
    >>> primes.append(17)
    >>> primes
    [2, 3, 5, 7, 11, 13, 17]

* ``sum(x)`` returns the sum of the list values::

    >>> sum([1, 2, 1, -1, -2])
    1
    >>> sum([])
    0

* ``l1 + l2`` concatenates the lists  ``l1`` and ``l2``::

    >>> list('dog') + [2, 3, 4]
    ['d', 'o', 'g', 2, 3, 4]

* ``l * n`` repeats ``n`` times the ``l`` list::

    >>> [3.14, 6.28, 9.42] * 2
    [3.14, 6.28, 9.42, 3.14, 6.28, 9.42]
    >>> [3.14, 6.28, 9.42] * 0
    []

* ``x in l`` allows to know if the ``x`` item is in the list or not::

    >>> r = list(range(0, 20, 2))
    >>> r
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> 12 in r
    True
    >>> 15 in r
    False

* ``l[i:j]`` allows to obtain a sub-list,
  from the ``i``-th to the ``j``-th items::

    >>> x = [1.5, 3.3, 8.4, 3.1, 2.9]
    >>> x[2:4]
    [8.4, 3.1]

* ``l.count(x)`` counts how many times the ``x`` item
  is in the list::

    >>> list('millimeter').count('i')
    3

* ``l.index(x)`` returns the index of the ``x`` item::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> colors.index('green')
    2
    >>> colors.index('pink')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 'pink' is not in list

* ``l.remove(x)`` removes the ``x`` item from the list::

    >>> todo = ['visit Paris','plant a tree','learn python','do skydiving']
    >>> todo.remove('learn python')
    >>> todo
    ['visit Paris', 'plant a tree', 'do skydiving']
    >>> todo.remove('learn french')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: list.remove(x): x not in list

* ``l.reverse()`` reverses a list::

    >>> palindrome = = list("No lemon, no melon")
    >>> palindrome
    ['N', 'o', ' ', 'l', 'e', 'm', 'o', 'n', ',', ' ', 'n', 'o', ' ', 'm', 'e', 'l', 'o', 'n']   
    >>> palindrome.reverse()
    >>> palindrome
    ['n', 'o', 'l', 'e', 'm', ' ', 'o', 'n', ' ', ',', 'n', 'o', 'm', 'e', 'l', ' ', 'o', 'N']
    >>> numbers = [1,2,3,4]
    >>> numbers.reverse() 
    >>> numbers
    [4, 3, 2, 1]

* ``l.sort()`` sorts the list::

    >>> numbers = [1,6,3,7,4,2,3,9,6,0]
    >>> numbers
    [1, 6, 3, 7, 4, 2, 3, 9, 6, 0]
    >>> numbers.sort()
    >>> numbers
    [0, 1, 2, 3, 3, 4, 6, 6, 7, 9]
    >>> friends = ['John','Maria','Joseph','Aron']
    >>> friends
    ['John','Maria','Joseph','Aron']
    >>> friends.sort()
    >>> friends
    ['Aron', 'John', 'Joseph', 'Maria']

Exercises
~~~~~~~~~

`1`_ `2`_  `3`_ `4`_

.. _`1`: http://progra.usm.cl/apunte/ejercicios/2/expresiones-listas.html
.. _`2`: http://progra.usm.cl/apunte/ejercicios/2/estadisticos-localizacion.html
.. _`3`: http://progra.usm.cl/apunte/ejercicios/2/polinomios.html
.. _`4`: http://progra.usm.cl/apunte/ejercicios/2/problema-josefo.html
