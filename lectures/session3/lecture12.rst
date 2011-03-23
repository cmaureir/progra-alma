Lecture 12 - Dictionaries
-------------------------

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
