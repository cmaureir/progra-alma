Lecture 10 - Tuples
-------------------

.. index:: tuple

A **tuple** is a sequence of grouped values.

A tuple is used to group several related values as a single value.

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

The tuple values can be recovered assigning the tuple to the corresponding variables.
This is called **unpacking tuples**::

    >>> person = ('John', 'Smith')
    >>> name, surname = person
    >>> name
    'John'

If you try to unpack the wrong number of values,
a value error occurs::

    >>> a, b, c = person
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 2 values to unpack

Also, it is possible to extract the values using their index::

    >>> person[1]
    'Smith'

``tuple`` comparison
~~~~~~~~~~~~~~~~~~~~~~

Two tuples are the same
when they have the same size
and each of their items have the same value::

    >>> (1, 2) == (3 // 2, 1 + 1)
    True
    >>> (6, 1) == (6, 2)
    False
    >>> (6, 1) == (6, 1, 0)
    False

.. index:: lexicographic order

To determine if a tuple is smaller than other,
the rule called **lexicographic order** is used.
If the items in the first position from both tuples are different,
comparing them determines the order of the tuples::

    >>> (1, 4, 7) < (2, 0, 0, 1)
    True
    >>> (1, 9, 10) < (0, 5)
    False

The first comparison is  ``True`` because ``1 < 2``.
The second comparison is ``False`` because ``1 > 0``.
No matter the value of the following values
or if a tuple has more elements than the other.

If the first position items are the same,
then the same comparison is used with the next value::

    >>> (6, 1, 8) < (6, 2, 8)
    True
    >>> (6, 1, 8) < (6, 0)
    False

The first comparison is  ``True`` because ``6 == 6`` and ``1 < 2``.
The second comparison is ``False`` because ``6 == 6`` and ``1 > 0``.

If the respective items continue being the same,
we continue comparing with the next values.
If a tuple runs out of items to compare before the other,
then it is immediately smaller than the other::

    >>> (1, 2) < (1, 2 ,4)
    True
    >>> (1, 3) < (1, 2, 4)
    False

The first comparison is ``True`` because ``1 == 1``, ``2 == 2``
and, at this point, all the elements from the first tuple have been compared.
The second comparison is ``False`` because ``1 == 1`` and ``3 < 2``;
in this case, it does reach the outcome before any of the tuples run out of elements.

This comparison method is the same used to sort words in alphabetic order.
(for example, in directories and dictionaries)::

    >>> 'car' < 'carousel'
    True
    >>> 'car' < 'cars'
    True
    >>> 'mon' < 'month' < 'monthly''
    True

