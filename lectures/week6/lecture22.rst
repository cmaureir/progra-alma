Lecture 22 - More on class creation
------------------------------------

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
    >>> 

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
            self.data = []
        def add(self, x):
            self.data.append(x)
        def addtwice(self, x):
            self.add(x) # using the other method!
            self.add(x) # using the other method!


Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing the class definition. (The class itself is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we’ll find some good reasons why a method would want to reference its own class.



Adding attributes to empty ``classes``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items. An empty class definition will do nicely:

class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods read() and readline() that get the data from a string buffer instead, and pass it as an argument.

Instance method objects have attributes, too: m.im_self is the instance object with the method m(), and m.im_func is the function object corresponding to the method.


``class`` vs ``dictionary``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although the simple classes of the prior section are meant to illustrate class model
basics, the techniques they employ can also be used for real work. For example, Chap-
ter 8 showed how to use dictionaries to record properties of entities in our programs.
It turns out that classes can serve this role, too—they package information like dic-
tionaries, but can also bundle processing logic in the form of methods. For reference,
here is the example for dictionary-based records we used earlier in the book:
>>>
>>>
>>>
>>>
>>>
>>>
mel
rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'
# Dictionary-based record
print(rec['name'])
This code emulates tools like records in other languages. As we just saw, though, there
are also multiple ways to do the same with classes. Perhaps the simplest is this—trading
keys for attributes:
>>>
...
>>>
>>>
>>>
>>>
>>>
40
class rec: pass
rec.name = 'mel'
rec.age = 45
rec.job = 'trainer/writer'
# Class-based record
print(rec.age)


This code has substantially less syntax than the dictionary equivalent. It uses an empty
class statement to generate an empty namespace object. Once we make the empty
class, we fill it out by assigning class attributes over time, as before.
This works, but a new class statement will be required for each distinct record we will
need. Perhaps more typically, we can instead generate instances of an empty class to
represent each distinct entity:
>>>
...
>>>
>>>
>>>
class rec: pass
pers1 = rec()
pers1.name = 'mel'
pers1.job = 'trainer'
# Instance-based records


>>> pers1.age
= 40
>>>
>>> pers2 = rec()
>>> pers2.name = 'vls'
>>> pers2.job = 'developer'
>>>
>>> pers1.name, pers2.name
('mel', 'vls')
Here, we make two records from the same class. Instances start out life empty, just like
classes. We then fill in the records by assigning to attributes. This time, though, there
are two separate objects, and hence two separate name attributes. In fact, instances of
the same class don’t even have to have the same set of attribute names; in this example,
one has a unique age name. Instances really are distinct namespaces, so each has a
distinct attribute dictionary. Although they are normally filled out consistently by class
methods, they are more flexible than you might expect.

Finally, we might instead code a more full-blown class to implement the record and its
processing:
>>> class Person:
...
def __init__(self, name, job):
...
self.name = name
...
self.job = job
...
def info(self):
...
return (self.name, self.job)
...
>>> rec1 = Person('mel', 'trainer')
>>> rec2 = Person('vls', 'developer')
>>>
>>> rec1.job, rec2.info()
('trainer', ('vls', 'developer'))
# Class = Data + Logic
This scheme also makes multiple instances, but the class is not empty this time: we’ve
added logic (methods) to initialize instances at construction time and collect attributes
into a tuple. The constructor imposes some consistency on instances here by always
setting the name and job attributes. Together, the class’s methods and instance attributes
create a package, which combines both data and logic.
We could further extend this code by adding logic to compute salaries, parse names,
and so on. Ultimately, we might link the class into a larger hierarchy to inherit an
existing set of methods via the automatic attribute search of classes, or perhaps even
store instances of the class in a file with Python object pickling to make them persistent.
In fact, we will—in the next chapter, we’ll expand on this analogy between classes and
records with a more realistic running example that demonstrates class basics in action.
In the end, although types like dictionaries are flexible, classes allow us to add behavior
to objects in ways that built-in types and simple functions do not directly support.
Although we can store functions in dictionaries, too, using them to process implied
instances is nowhere near as natural as it is in classes.



