Lecture 11 - Dictionaries
-------------------------

.. index:: dictionary

A **dictionary** is a data type that allows to associate value pairs.

.. index:: key (dictionary), value (dictionary)

A dictionary can be seen
as a **key** collection,
each one having an associated **value**.
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
and the associated values to them are,
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
a **key error** (``KeyError``) occurs::

    >>> telephones['Nancy']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Nancy'

It is possible to add new keys simply assigning them to a value::

    >>> telephones['Peter'] = 4448139
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 5551428, 'Shane': 5550012}

Note that the order in which the keys are stored in the dictionary
is not necessarily the same order they were added.

If you assign a value to a key that is already present in the dictionary,
the previous value is overwritten.
Remember that a dictionary cannot have repeated keys::

    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 5551428, 'Share': 5550012}
    >>> telephones['Andy'] = 4448139
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 4448139, 'Share': 5550012}

The values can be repeated.
In the previous example, Andy and Peter have the same number.

To remove a key, you can use the statement ``del``::

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

To iterate over the keys, use ``d.values()``::

    >>> for v in telephones.values():
    ...     print(v)
    ...
    5552437
    4448139
    4448139

It is also possible to create a list of keys or values::

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

``k in d`` allows to know if the key ``k`` is in the dictionary ``d``::

    >>> legs = {'cat': 4, 'human': 2, 'octopus': 8, 'dog': 4, 'centipede': 100}
    >>> 'dog' in legs
    True
    >>> 'worm' in legs
    False

To know if a key *is not* in the dictionary, it
is possible to use the ``not in`` statement::

    >>> 'worm' not in legs
    True

Exercises
~~~~~~~~~~

`1`_

.. _`1`: http://progra.usm.cl/apunte/ejercicios/2/expresiones-diccionarios.html
