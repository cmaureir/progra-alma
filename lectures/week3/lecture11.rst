Lecture 11 - Sets
-----------------

.. index:: sets

A **set** is a disordered collection of non repeated values.

The Python sets are analogues to mathematical sets.
The data type that represent the sets is called ``set``.

The ``set`` type is mutable:
it can be modified after it has been created.

How to create a ``set``
~~~~~~~~~~~~~~~~~~~~~~~
The two main ways to create sets are:

* use a literal set, in brackets::

    >>> colors = {'blue', 'red', 'white', 'white'}
    >>> colors
    {'red', 'blue', 'white'}

  Note that set does not include repeated items,
  and the items might not be in the same order they were added.

* use the ``set`` function applied over an iterable::

    >>> set('abracadabra')
    {'a', 'r', 'b', 'c', 'd'}
    >>> set(range(50, 2000, 400))
    {1250, 50, 1650, 850, 450}
    >>> set([(1, 2, 3), (4, 5), (6, 7, 8, 9)])
    {(4, 5), (6, 7, 8, 9), (1, 2, 3)}

  The empty set must be created using ``set()``,
  as ``{}`` and represents the empty dictionary.

The set items must be immutable.
For example, it is not possible to create a set of lists,
but it is to create a set of tuples::

    >>> s = {[2, 4], [6, 1]}
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    >>> s = {(2, 4), (6, 1)}
    >>> s
    set([(6, 1), (2, 4)])

As a set is not ordered, it
makes no sense trying to obtain an item using the index::

    >>> s = {'a', 'b', 'c'}
    >>> s[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing


``set`` operations
~~~~~~~~~~~~~~~~~~~

* ``len(s)`` returns the number of items of the ``s`` set::

    >>> len(set('abracadabra'))
    5
    >>> len(set())
    0

* ``x in s`` allows to know if the ``x`` item is in the ``s`` set::

    >>> 3 in {2, 3, 4}
    True
    >>> 5 in {2, 3, 4}
    False

  ``x not in s`` allows to know if ``x`` is not in the ``s`` set::

    >>> 10 not in {2, 3, 4}
    True

* ``s.add(x)`` adds the ``x`` item to the ``s`` set::

    >>> s = {6, 1, 5, 4, 3}
    >>> s.add(-37)
    >>> s
    {1, 3, 4, 5, 6, -37}
    >>> s.add(4)
    >>> s
    {1, 3, 4, 5, 6, -37}

* ``s.remove(x)`` remove the ``x`` item from the ``s`` set::

    >>> s = {6, 1, 5, 4, 3}
    >>> s.remove(1)
    >>> s
    {3, 4, 5, 6}

  If the ``x`` item is not in the set, an **key error** occurs::

    >>> s.remove(10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 10

* ``s & t`` returns the intersection between the sets ``s`` and ``t``::

    >>> a = {1, 2, 3, 4}
    >>> b = {2, 4, 6, 8}
    >>> a & b
    {2, 4}

* ``s | t`` returns the union of the sets ``s`` and ``t``::

    >>> a | b
    {1, 2, 3, 4, 6, 8}

* ``s - t`` returns the difference between the sets ``s`` and ``t``;
  i.e. the items of ``s`` that are not in ``t``::

    >>> a - b
    {1, 3}

* ``s ^ t`` returns the symmetric difference between the sets ``s`` and ``t``;
  i.e. the items that are either in ``s`` or ``t`` ,
  but not in both::

    >>> a ^ b
    {1, 3, 6, 8}

* ``s < t`` indicates if ``s`` is a subset of ``t``::

    >>> {1, 2} < {1, 2, 3}
    True
    >>> {1, 4} < {1, 2, 3}
    False

  ``s <= t`` also indicates if ``s`` is a subset of ``t``.
  The difference occurs when the sets are the same::

    >>> {1, 2, 3} < {1, 2, 3}
    False
    >>> {1, 2, 3} <= {1, 2, 3}
    True
