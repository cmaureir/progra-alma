Lecture 3
=========

Lists
-----

.. index:: list

A **list** is a ordered collection of values.

In Python, the data type which represent lists is called
``list``.

How to create a ``list``
~~~~~~~~~~~~~~~~~~~~~~~~

The two main ways to create a list, are:

* use a literal list, with the values in brackets::

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
  i.e. how many element have::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> len(colors)
    4
    >>> len([True, True, True])
    3
    >>> len([])
    0

* ``l[i]`` return the ``i``-th value of the list.
  The ``i`` value is called **index** of the value.
  Be careful because it start counting from 0,
  and not from 1::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> colors[0]
    'blue'
    >>> colors[3]
    'yellow'

  If the ``i`` index indicates an item which is not in the list,
  occurs an **index error**::

    >>> colors[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

  If the index is negative,
  the item counts from the end backward::

    >>> colors[-1]
    'yellow'
    >>> colors[-4]
    'blue'

* ``l.append(x)`` add the ``x`` item to the end of the list::

    >>> primes = [2, 3, 5, 7, 11]
    >>> primes.append(13)
    >>> primes.append(17)
    >>> primes
    [2, 3, 5, 7, 11, 13, 17]

* ``sum(x)`` return the sum of the list values::

    >>> sum([1, 2, 1, -1, -2])
    1
    >>> sum([])
    0

* ``l1 + l2`` concatenates the  ``l1`` and ``l2`` lists::

    >>> list('dog') + [2, 3, 4]
    ['d', 'o', 'g', 2, 3, 4]

* ``l * n`` repeats ``n`` times the ``l`` list::

    >>> [3.14, 6.28, 9.42] * 2
    [3.14, 6.28, 9.42, 3.14, 6.28, 9.42]
    >>> [3.14, 6.28, 9.42] * 0
    []

* ``x in l`` allows to know if the  ``x`` item is or not in the list::

    >>> r = list(range(0, 20, 2))
    >>> r
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> 12 in r
    True
    >>> 15 in r
    False

* ``l[i:j]`` allows to obtain a list slice,
  from the ``i``-th to the ``j``-th items::

    >>> x = [1.5, 3.3, 8.4, 3.1, 2.9]
    >>> x[2:4]
    [8.4, 3.1]

* ``l.count(x)`` counts how many times the ``x`` item
  is in the list::

    >>> list('millimeter').count('i')
    3

* ``l.index(x)`` return the index of the ``x`` item::

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

* ``l.reverse()`` reverse a list::

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

* ``l.sort()`` sort the list::

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

Tuples
------

.. index:: tuple

A **tuple** is a sequence of grouped values.

A tuple used to group, like a single value,
several related values.

The data type that represents the tuple is called ``tuple``.
The ``tuple`` type is immutable: a tuple can not be modified once created.

.. index:: tuple literal

A tuple can be created
setting comma separated values and in round brackets.
For example,
we can create a tuple with the first-name and last-name of a person::

    >>> person = ('John', 'Smith')
    >>> person
    ('John', 'Smith')

Unpacking tuples
~~~~~~~~~~~~~~~~

.. index:: unpacking

The tuple values can be recovered assigning the tuple to respective variables.
This is called **unpacking tuples**::

    >>> person = ('John', 'Smith')
    >>> name, surname = person
    >>> name
    'John'

If you try to unpack the wrong number of values,
occur a value error::

    >>> a, b, c = person
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 2 values to unpack

Also, is possible to extract the values using their index::

    >>> person[1]
    'Smith'

``tuple`` comparison
~~~~~~~~~~~~~~~~~~~~~~

Two tuples are the same
when have the same size
and each of their items have the same value::

    >>> (1, 2) == (3 // 2, 1 + 1)
    True
    >>> (6, 1) == (6, 2)
    False
    >>> (6, 1) == (6, 1, 0)
    False

.. index:: lexicographic order

To determinate if a tuple is less than another,
is used which denominates **lexicographic order**.
If the first position items from both tuples are not the same,
they determine the order of the tuples::

    >>> (1, 4, 7) < (2, 0, 0, 1)
    True
    >>> (1, 9, 10) < (0, 5)
    False

The first comparison is  ``True`` because ``1 < 2``.
The second comparison is ``False`` because ``1 > 0``.
No matter the value of the following values,
or if a tuple has more element than the other.

If the first position items are the same,
then used the next value to do the comparison::

    >>> (6, 1, 8) < (6, 2, 8)
    True
    >>> (6, 1, 8) < (6, 0)
    False

The first comparison is  ``True`` because ``6 == 6`` and ``1 < 2``.
The second comparison is ``False`` because ``6 == 6`` and ``1 > 0``.

If the respective items continue being the same,
we continue trying with the next values.
If a tuple run out of items to compare before the other,
then is immediately less than the other::

    >>> (1, 2) < (1, 2 ,4)
    True
    >>> (1, 3) < (1, 2, 4)
    False

The first comparison is ``True`` because ``1 == 1``, ``2 == 2``,
and end there are completed items in the first tuple.
The second comparison is ``False`` because ``1 == 1`` and ``3 < 2``;
in this case, if reached to determine the outcome before they run out the elements.

This comparison method is the same used to set words in alphabetic order.
(for example, in directories and dictionaries)::

    >>> 'car' < 'carousel'
    True
    >>> 'car' < 'cars'
    True
    >>> 'mon' < 'month' < 'monthly''
    True


Sets
----

.. index:: sets

A **set** is a disordered collection of non repeated values.

The Python sets are analogues to mathematical sets.
The data type that represent the sets is called ``set``.

The ``set`` type is mutable:
once a set was created, can be modified.

How to create a ``set``
~~~~~~~~~~~~~~~~~~~~~~~
The two main ways to create a set are:

* use a literal set, in brackets::

    >>> colors = {'blue', 'red', 'white', 'white'}
    >>> colors
    {'red', 'blue', 'white'}

  Note that set does not include repeated items,
  and the items are not in the same order they were added.

* use the ``set`` function applied over an iterable::

    >>> set('abracadabra')
    {'a', 'r', 'b', 'c', 'd'}
    >>> set(range(50, 2000, 400))
    {1250, 50, 1650, 850, 450}
    >>> set([(1, 2, 3), (4, 5), (6, 7, 8, 9)])
    {(4, 5), (6, 7, 8, 9), (1, 2, 3)}

  The empty set must be created using ``set()``,
  as ``{}`` represents the empty dictionary.

The set items must be immutable.
For example, is not possible to create a set of list,
but yes a set of tuples::

    >>> s = {[2, 4], [6, 1]}
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    >>> s = {(2, 4), (6, 1)}
    >>> s
    set([(6, 1), (2, 4)])

As a set is not  ordered,
makes no sense try to obtain an item using the index::

    >>> s = {'a', 'b', 'c'}
    >>> s[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing


``set`` operations
~~~~~~~~~~~~~~~~~~~

* ``len(s)`` return the number of items of the ``s`` set::

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

  If the ``x`` item is not in the set, occurs a **key error**::

    >>> s.remove(10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 10

* ``s & t`` return the intersection between the ``s`` and ``t`` sets::

    >>> a = {1, 2, 3, 4}
    >>> b = {2, 4, 6, 8}
    >>> a & b
    {2, 4}

* ``s | t`` return the union of the ``s`` and ``t`` sets::

    >>> a | b
    {1, 2, 3, 4, 6, 8}

* ``s - t`` return the difference between ``s`` and ``t``;
  i.e. the items of ``s`` that are not in ``t``::

    >>> a - b
    {1, 3}

* ``s ^ t`` return the symmetric difference between ``s`` and ``t``;
  i.e. the items in ``s`` or in ``t``,
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
* ``s & t`` return the intersection between the ``s`` and ``t`` sets::

    >>> a = {1, 2, 3, 4}
    >>> b = {2, 4, 6, 8}
    >>> a & b
    {2, 4}

* ``s | t`` return the union of the sets ``s`` and ``t``::

    >>> a | b
    {1, 2, 3, 4, 6, 8}

* ``s - t`` return the difference between ``s`` and ``t``;
  i.e. the items of ``s`` that is not in ``t``::

    >>> a - b
    {1, 3}

* ``s ^ t`` return the symmetric difference between ``s`` and ``t``;
  i.e.  the items in ``s`` or in ``t``,
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


Dictionaries
------------

.. index:: dictionary

A **dictionary** is a data type that allow to associate value pairs.

.. index:: key (dictionary), value (dictionary)

A dictionary can be see
like a **key** collection,
each one has a **value** associated.
The keys are disordered
and there are no repeated keys.
The only way to access a value
is through their key.

How to create a ``dictionary``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main way to create a dictionary is using a literal dictionary.
The key is associated to a value using two points (colon)::

    >>> telephones = {'John': 5552437, 'Andy': 5551428, 'Shane': 5550012}

In this example,
the keys are ``'John'``, ``'Andy'`` and ``'Shane'``,
and the associated values to their are,
``5552437``, ``5551428`` and ``5550012`` respectively.

An empty dictionary can be created using ``{}`` or with a function called ``dict()``::

    >>> d = {}
    >>> d = dict()

How to use a ``dictionary``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The associated value to the ``k`` key in the ``d`` dictionary
can be obtained through ``d[k]``. ::

    >>> telephones['John']
    5552437
    >>> telephones['Andy']
    5551428

If the key is not present in the dictionary,
occurs a **key error** (``KeyError``)::

    >>> telephones['Nancy']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Nancy'

It is possible to add new keys simply assigning to a value::

    >>> telephones['Peter'] = 4448139
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 5551428, 'Shane': 5550012}

Note that the order in which the keys are in the dictionary
is not necessarily the same order in they were added.

If you assign a value to a key already in the dictionary,
the previous value  is overwritten.
Remember that a dictionary can not have repeated keys::

    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 5551428, 'Share': 5550012}
    >>> telephones['Andy'] = 4448139
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 4448139, 'Share': 5550012}

The values can be repeated.
In the previous example, Andy and Peter have the same number.

To remove a key, you can use the ``del`` statement::

    >>> del telephones['Share']
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 4448139}

If you use a dictionary in a ``for`` cycle, 
in each iteration a key is obtained::

    >>> for k in telephones:
    ...     print(k)
    ...
    John
    Peter
    Andy

To iterate over the keys, used ``d.values()``::

    >>> for v in telephones.values():
    ...     print(v)
    ...
    5552437
    4448139
    4448139

Also is possible create key lists or values::

    >>> list(telephones)
    ['John', 'Peter', 'Andy']
    >>> list(telephones.values())
    [5552437, 4448139, 4448139]

``len(d)`` return how many key-value pairs are in the dictionary::

    >>> numbers = {15: 'fifteen', 24: 'twenty-four'}
    >>> len(numbers)
    2
    >>> len({})
    0

``k in d`` allow to know if the ``k`` key is in the ``d`` dictionary::

    >>> legs = {'cat': 4, 'human': 2, 'octopus': 8, 'dog': 4, 'centipede': 100}
    >>> 'dog' in legs
    True
    >>> 'worm' in legs
    False

To know if a key *is not* in the dictionary,
is possible to use the ``not in`` statement::

    >>> 'worm' not in legs
    True

Assignment 3
------------

PENDING
