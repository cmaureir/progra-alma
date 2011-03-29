Lecture 15 - Use of objects
---------------------------

In Python, the **objects** are abstraction for data.
All the data inside a Python program is represented by objects,
or in some cases, by relations between two or more objects.
We are saying that all the basic elements like `integers`, `functions`,
`strings`, `dictionaries`, and so on, they are all objects,
notoriously they have certain things in common.

Every object have three main characteristics:
* An identity (unique and unmodifiable), that is an integer returned by ``id(<object>)`` method.::

    >>> number = 13
    >>> id(number)
    163098656
    >>> name = 'carl'
    >>> id(name)
    3075656576L

* A type (unmodifiable), that is returned by ``type(<object>)`` method.::

    >>> number = 13
    >>> type(number)
    <type 'int'>
    >>> name = 'carl'
    >>> type(name)
    <type 'str'>

* A value, saved in the assignation process.::

    >>> number = 13
    >>> number
    13
    >>> name = 'carl'
    >>> name
    'carl'

If you change the value of a variable, the identity will change is almost all the cases.::

    >>> number = 12
    >>> id(number)
    163098668
    >>> number += 1
    >>> id(number)
    163098656

Some objects don't allow to change their content, because are immutable like the tuples
(See lecture10_ for more details)

.. _lecture10:  ../session3/lecture10.html

The idea of the **type** of an object is know some details from it,
the methods they have, the bytes of memory that use, etc.

The **name** of an object is different,
is not a property itself, because the object
does not know their name.
An object can have several names or not have a name,
so they live only in the namespace
(Namespace, collection of name and object references pairs).

To clarify this idea,
lets see this simple line::

   >>> variable = 42

this means that we are adding the name 'variable' in our namespace,
making it refer to an integer object with the value '42'.

You can assign a new object reference to a name,
simple adding a new value in your code,
for example::

    >>> variable = 42
    >>> variable = 'hello'

First, we add the name ``variable`` to the local namespace,
making it refer to a integer object with the value 42,
and in the next line, we making it point to a string
with the value ``hello``.

This is very different,
when we work with **containers**,
which are *objects* that contain references to other *objects*.
For example, tuples, dictionaries, list, and so.

If we perform the next procedure::

    >>> list1 = []
    >>> list1
    []
    >>> id(list1)
    3074653516L
    >>> list1.append(23)
    >>> list1
    [23]
    >>> id(list1)
    3074653516L

We are adding the name ``list1`` to the namespace,
making it refer to an empty list object.
Then we are calling an object method, to append an integer
to itself.
This modify the content of ``list1``, but do not touch the namespace name,
or the integer object, or the identity of the object.

So, each time that we use a *method* of any previous
`Data Type`_ we are using objects,
for example::

    >>> mylist = [5,3,2]
    >>> mylist.sort()
    >>> mylist
    [2, 3, 5]
    >>> mylist.remove(2)
    >>> mylist
    [3, 5]
    >>> number = mylist[0]
    >>> number*'hello ' 
    'hello hello hello '
    >>> line = number*'hello '
    >>> line
    'hello hello hello '
    >>> line.replace('o','')
    'hell hell hell '

Means that we are using the methods ``sort()``, ``remove()``,
own by all the **list** objects,
the method ``replace()``, own by all the **str** objects.

.. _Data Type: ../session1/lecture2.html


We will look more deeply the *objects*,
in the `Sixth session`_

.. _Sixth session: ../session6/index.html

