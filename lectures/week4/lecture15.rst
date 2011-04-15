Lecture 15 - Use of objects and Files
-------------------------------------

In Python, the **objects** are abstraction for data.
All the data inside a Python program is represented by objects,
or in some cases, by relations between two or more objects.
We are saying that all the basic elements like `integers`, `functions`,
`strings`, `dictionaries`, and so on, they are all objects,
notoriously they have certain things in common.

About the objects
~~~~~~~~~~~~~~~~~

The idea of this lecture is to understand
the idea behind the objects, but all the
*Object Oriented Paradigm* will be
study with more detail in the next lectures.

An *object* is an instance of a *class*,
the most simple example to understand this,
is to think in a class called ``Human``,
and all of us are intances, because we are all
human beings. In the same way, a *class* 
have several functions, called *methods*.
In our example, as Human, we can *walk*, *speak*,
*run*, etc, so we as objects, can use that
methods, because we can speak, walk, etc.

Several functions that you used,
create objects of different types,
like *bool()*, *dict()*, *float()*,
*int()*, *list()*, *set()*, *tuple()*, *str()*,
 etc.

The idea of the previous methods,
is convert objects in another types,
for example::

    >>> a = 4
    >>> b =float(a)
    >>> b
    4.0
    >>> b = b + 0.3
    >>> b
    4.3
    >>> c = int(b)
    >>> c
    4
    >>> bool(c)
    True
    >>> c = c - c
    >>> c
    0
    >>> bool(c)
    False

Also between objects like, *lists*, *sets*,
*tuples* and *dictionaries*::

    >>> a = (1,2)
    >>> type(a)
    <type 'tuple'>
    >>> b = set(a)
    >>> b
    set([1, 2])
    >>> a
    (1, 2)
    >>> type(b)
    <type 'set'>
    >>> d = list(b)
    >>> d
    [1, 2]
    >>> e = dict([[1,'one'],[2,'two']])
    >>> e
    {1: 'one', 2: 'two'}
    >>> type(e)
    <type 'dict'>
    >>> set(e)
    set([1, 2])
    >>> list(e)
    [1, 2]


The object, as you saw in the previous lectures,
have several useful methods, which can be executed
as following::

    object.method()

So, the previous examples about *lists*, *sets*,
*tuples* and *dictionaries* like::

    a = [1,3,2]
    >>> a.sort()
    >>> a
    [1, 2, 3]

    



Files
~~~~~

Work with a file is a nightmare in some programmig languages,
but is very simple in Python.

First of all, you must know that an instance of a file
inside a program or script is an object, so like all the
objects, has some very useful methods.

To explain the files behaviour in Python, we will consider
the next file, called `data.txt`_.

::

    Hello first line!
    Oh! the second line
    The next line is very boring
    1,-234.5,45.8,ok
    Final line :)

.. _`data.txt`: ../../_static/data.txt


**Opening** a file is very easy:

::

    my_file=open('data.txt','r')

Now ``my_file`` is an object that is
an instance to access to the `data.txt` file.

But, what is the *'r'* statement?
The second parameter of the **open()** method 
specify the *mode* when the file is openned.
Some useful modes are:

* *r*, ``read-only`` mode,
* *w*, ``write-only`` mode,
  if the file exist will be overwrited,
* *a*, ``append`` mode.

If you do not give any mode,
the default mode is ``read-only``.

There are different ways to **Read** a file,
but now we will focus on three methods,
``read()``, ``readline()`` and ``readlines()``.

The ``read()`` method, return the entire content
of the file, for example::

    >>> my_file=open('data.txt','r')
    >>> content = my_file.read()
    >>> print content
    Hello first line!
    Oh! the second line
    The next line is very boring
    1,-234.5,45.8,ok
    Final line :)

    >>> new_content = my_file.read()
    >>> print new_content
    
    >>>

The ``content`` variable contain all the information
of the file.

But, what happend with the ``new_content`` variable?
is empty!. This is because when you open a file
a ``pointer`` is posisionated at the beginning of the file,
and when you read the file, the pointer moves forward,
so with the first call of the ``read()`` method,
the pointer reach the end of the file, so in the next
call of the ``read()`` method, there is no more
content to read, that is the reason to have an
empty variable called ``new_content``.

If you want to move backwards and forwards inside a file
you need to read about the `seek()`_ method.

.. _`seek()`: http://docs.python.org/library/stdtypes.html#file.seek

The ``readline()`` method, return only one line of the file,
for example::

    >>> my_file=open('data.txt','r')
    >>> my_file.readline()
    'Hello first line!\n'
    >>> my_file.readline()
    'Oh! the second line\n'
    >>> my_file.readline()
    'The next line is very boring\n'
    >>> my_file.readline()
    '1,-234.5,45.8,ok\n'
    >>> my_file.readline()
    'Final line :)\n'
    >>> my_file.readline()
    ''
    >>> 

You can also assign a line to a variable::

    >>> my_file=open('data.txt','r')
    >>> simple_line = my_file.readline()
    >>> print simple_line
    'Hello first line!\n'

The ``readlines()`` method, return a list with all 
the lines in the file, for example::

    >>> my_file=open('data.txt')
    >>> my_file.readlines()
    ['Hello first line!\n', 'Oh! the second line\n', 'The next line is very boring\n', '1,-234.5,45.8,ok\n', 'Final line :)\n']

So, if you remember the `list`_ lecture
you can iterate over a list to work with each element::

    >>> my_file=open('data.txt')
    >>> for line in my_file.readlines():
    ...    print line
    ... 
    Hello first line!
    
    Oh! the second line
    
    The next line is very boring
    
    1,-234.5,45.8,ok
    
    Final line :)
    
    >>> 

.. _`list`: ../week3/lecture9.html

Is very anoying to had blank lines
between each line, to avoid this
you need to add a comma to the print line,
like this::

    >>> my_file=open('data.txt')
    >>> for line in my_file.readlines():
    ...    print line,
    ... 
    Hello first line!
    Oh! the second line
    The next line is very boring
    1,-234.5,45.8,ok
    Final line :)
    >>> 


We will look two method to **Write**
a file, using the ``write()`` and the ``writelines()``
method.

The ``write()`` method allow to write a string
inside the file, for example::

    >>> my_file=open('data2.txt','w')
    >>> my_file.write('test content\n')
    >>> my_file.close()
    >>> 
    localhost~> cat data2.txt 
    test content
    


The ``writelines()`` method allow to write
several lines inside the file, this is possible
giving a list as parameter to the method,
for example ::

    >>> my_file=open('data2.txt','w')
    >>> my_list=['first line\n','second line\n','final line\n']
    >>> my_file.writelines(my_list)
    >>> my_file.close()
    >>> 
    localhost~> cat data2.txt 
    first line
    second line
    final line

If you want to *close* a file,
the function is called ``close()``.

::

    my_file.close()


Objects characteristics
~~~~~~~~~~~~~~~~~~~~~~~

Every object have three main characteristics:

* An identity (unique and unmodifiable), that is an integer returned by ``id(<object>)`` method.::

    >>> number = 13
    >>> id(number)
    163098656
    >>> name = 'carl'
    >>> id(name)
    3075656576L

* A type (unmodifiable), that is returned by ``type(<object>)`` method::

    >>> number = 13
    >>> type(number)
    <type 'int'>
    >>> name = 'carl'
    >>> type(name)
    <type 'str'>

* A value, saved in the assignment process::

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

Some objects do not allow to change their content, because are immutable like the tuples
(See lecture10_ for more details)

.. _lecture10:  ../week3/lecture10.html

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


Exercises
~~~~~~~~~

PENDING
