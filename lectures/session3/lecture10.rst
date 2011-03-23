Lecture 10 - Tuples
-------------------

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

