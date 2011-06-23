Lecture 22 - Object-Oriented Programming - More on class creation
-----------------------------------------------------------------

There are another thing that you can use
when you are programming with the OO paradigm
in Python, that in some cases will be very useful.

``objects`` are data types
~~~~~~~~~~~~~~~~~~~~~~~~~~

The objects are data tupes like any another
python data type, so you can mix it with
different Python statement.

For example:

::

    >>> class Robot():
    ...   def __init__(self,name):
    ...     self.name = name
    ...     self.x = 0
    ...     self.y = 0
    ...   def move(self,x,y):
    ...     self.x = x
    ...     self.y = y
    ... 
    >>> robot1 = Robot('R2D2')
    >>> robot1.name
    'R2D2'
    >>> robot1.move(3,5)
    >>> robot2 = Robot('C3PO')
    >>> robot2.move(4,1)
    >>> robots = []
    >>> robots.append(robot1)
    >>> robots.append(robot2)
    >>> robots.append(Robot('Robocop'))
    >>> for i in robots:
    ...   print i.name
    ... 
    R2D2
    C3PO
    Robocop
    >>> for i in robots:
    ...   i.x, i.y
    ... 
    (3, 5)
    (4, 1)
    (0, 0)
    >>> for i in robots:
    ...   i.move(i.x+2,i.y-3)
    ... 
    >>> for i in robots:
    ...   i.x, i.y
    ... 
    (5, 2)
    (6, -2)
    (2, -3)

So, we can have list, dictionaries, set, etc  of objects!.


``methods`` outside a class
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you remember the method definition,
the only rule was that the first argument must be a *self* statement,
to belong to a certain class.

It is not necessary that the method be inside the class statement,
because you can assign an external function to a local method of the class.

For example:

::

    def ext_pow(self, x, y):
        return x**y
     
    class myClass():
        def f(self):
            return 'hello, this is a method'
        p = ext_pow
        h = f

Lets talk about all the code:

* ``ext_pow`` is a normal function, except that the first
  argument is a *self* statement (this is the difference
  between a *method* and a *function*).
* The ``myClass`` is a simple class declaration.
* The ``f`` method is a normal method, without extra
  parameter, and the only functionallity is that return an string,
  with a message.
* The ``p`` attribute is initializing refering the external function object,
  so, calling *p()* will be the same that calling *ext_pow()*.
* The ``h`` attribute is initializing refering the ``f`` function,
  so, calling *h()* will be the same that calling *f()*.

Lets look the functionallity:

::

    >>> obj = myClass() # Creating an object
    >>> type(obj) 
    <type 'instance'>
    >>> obj.f
    <bound method myClass.f of <a.myClass instance at 0xb74448ac>>
    >>> obj.f()
    'hello, this is a method'
    >>> obj.p(2,3) # this is the behaviour of the ext_pow function
    8
    >>> obj.p
    <bound method myClass.ext_pow of <a.myClass instance at 0xb74448ac>>
    >>> obj.h
    <bound method myClass.f of <a.myClass instance at 0xb74448ac>>
    >>> obj.h()
    'hello, this is a method'
    >>> obj.ext_pow(4,2) # this will not work, because ext_pow is not in the class, only the reference in p
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: myClass instance has no attribute 'ext_pow'


Note that this practice usually only serves to confuse the reader of a program,
so, is valid, but not recommended.


Calling ``methods`` inside ``methods``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you create a class with a couple of methods inside,
you have visibility to all the attributes of the class,
so, you can also call one method from another.

For example, lets consider the next class:

::

    class Bag:
        def __init__(self):
            self.content = []
        def add(self, x):
            self.content.append(x)
        def addtwice(self, x):
            self.add(x) # using the other method!
            self.add(x) # using the other method!


The idea of the methods, is that can be referenced in all the code inside the class.
So, this can be very useful when you have two or more functions with a similar
objective.

Adding attributes to empty ``classes``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Class instances (objects) are **mutable** data types,
so, it is possible to have empty class definition
to build different objects, with different attributes.

For example:

::

    >>> class Student():
    ...     pass
    ... 

And now, modifying the instance:

::

    >>> john = Student()
    >>> john.name = 'John Smith'
    >>> john.age = 35
    >>> john
    <__main__.Student instance at 0xb748694c>
    >>> marie = Student()
    >>> marie.name
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: Student instance has no attribute 'name'

If you look the example,
you can note that the second instance of the Student class
have not the same attributes of the first instance.

You can also add some function to a class instance:

::

    >>> def f():
    ...   print 'Simple function'
    ... 
    >>> john.func = f
    >>> john.func()
    Simple function


Exercises
~~~~~~~~~

* PENDING
* PENDING
* PENDING
