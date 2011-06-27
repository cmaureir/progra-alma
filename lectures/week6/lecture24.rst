Lecture 24 - Design good practices
-----------------------------------

The content of this lecture is based on the chapters 28 and 30
of the Learning Python 4th edition book.

.. clases cohecionadas
.. sin acoplamiento
.. no crear clases que lo hagan todo
.. clases representan entidades
.. Diseño OO

.. Learning Python 4th, chapter 28

The `class` Statement
~~~~~~~~~~~~~~~~~~~~~

The Python class statement is very similar to another languages statement,
but only by the *name*, because if we see the closer implementation, is quite
different.

In Python, a class is not a declaration, but is an object builder.

The form of a class are very simple, and you must view and work
with its structure. Here is the statement's general form.

::

    class <name>(superclass,...): # Assign to name
        data = value              # Shared class data
        def method(self,...):     # Methods
            self.member = value   # Per-instance data


Any assignment inside a class, will be a class attribute.

To explain in more details the classes functionality,
lets study the namespace behaviour of the classes.

The idea is to perform the same steps of a module creation,
but with a different statement declaration.

When Python executes a class statement,
it perform the execution of all the statement inside
the class body, the idea is to create the names in a local
scope, to be a future attribute in a class object..

The main reason of the classes are different of the modules,
is because a class can use the idea of `inheritance`.

For example, the assignment of a simple object (not a function)
produce a shared attribute by all the class instances:

::

    >>> class SharedData:
    ...     spam = 42            # Generates a class data attribute
    ...
    >>> x = SharedData() # Make two instances
    >>> y = SharedData()
    >>> x.spam, y.spam   # They inherit and share 'spam'
    (42, 42)
    
We can change a class attribute manually, for example,
if we need to change the value of `spam` from 42 to 99:

::

    >>> SharedData.spam = 99
    >>> x.spam, y.spam, SharedData.spam
    (99, 99, 99)

But also, you can personalize the objects attributes,
it means, that for each object you can change the attribute values:

::

    >>> x.spam = 88
    >>> x.spam, y.spam, SharedData.spam
    (88, 99, 99)

It also possible to create attributes in a class,
which are not inheritable by the objects,
for example:

::

    class MixedNames:# Define class
        data = 'spam'# Assign class attr
        def __init__(self, value):# Assign method name
            self.data = value # Assign instance attr
        def display(self):
            print(self.data, MixedNames.data) # Instance attr, class attr

This implementation contains a class variable called `data` (simple variable assignation), but
also has an internal variable (inheritable) called `self.data` (class's local scope).

You can compare this issue, with the following example:

::

    >>> x = MixedNames(1) # Make two instance objects
    >>> y = MixedNames(2) # Each has its own data
    >>> x.display(); y.display() # self.data differs, MixedNames.data is the same
    1 spam
    2 spam

The result is different because the variables lives in two places,
in the instances objects (created inside the `__init___` method)
and in the class (simple assignation).

Methods
~~~~~~~

As we mentioned before, the methods are only functions created nested in a class.
If you see the concept from an abstract perspective, methods provide to instances (object)
a certain behavior.

The internal mechanism of the object methods is related to the first
argument of a method, the `self` statement.
When you write a method call like:

::

    instance.method(args...)

Python automatically translated to a class method calls:

::

    class.method(instance, args...)

As you can see, both calls are valid in Python,
because besides the normal inheritance in the instance,
the real magic is the first argument in the methods (`self`),

An example to understand this mechanism will be:

Suppose we define the following class:

::

    class PrinterClass():
        def printer(self,text)
            self.txt = text    # Modify the instance
            print self.txt     # Access the instance

Note that `self.txt` is an internal class variable,
so it is possible to perform the next lines:

::

    >>> x = PrinterClass() # Make instance
    >>> x.printer('calling from an instance')
    calling from an instance
    >>> x.message
    'calling from an instance'

So, as we mentioned before, we have two ways to called a method,
by an instance or the class itself.

::

    >> PrinterClass.printer(x, 'calling from the class')
    calling from the class
    >> x.message
    calling from the class

Specializing Inherited Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can easily change the methods
from the class instances, trying to optimize
the functionality.

A simple way to do this,
is to use the previous method (provided by a class),
but adding some other functionality,
to 'specialize' the idea.

The main idea is to re-write some methods
provided by the class.

::
 
    Class SuperClass:
       def method(self):
           print('in Super.method')
    
    Class SubClass(Super):
       def method(self):                # Override method
           print('starting Sub.method') # Adding extra actions
           Super.method(self)           # Run default action
           print('ending Sub.method')   # Adding extra actions

Documentation
~~~~~~~~~~~~~

The docstring can be used by classes and by the class components,
being strings literals to describe the mechanism and details of some
Python statement, using the `__doc__` reserved function.
(this can be used by modules, functions, classes and methods).

The following example summarizes the places where doctstrings can show up
in the code.

::

    # File: docstr.py
    
    "I am: docstr.__doc__"
    
    def func(args):
        "I am: docstr.func.__doc__"
        pass
    class spam:
        "I am: spam.__doc__ or docstr.spam.__doc__"
        def method(self, arg):
            "I am: spam.method.__doc__ or self.method.__doc__"
            pass

The main advantage is that they stick around at runtime,
and are very useful for not-trivial implementations.

::

    >>> import docstr
    >>> docstr.__doc__
    'I am: docstr.__doc__'
    >>> docstr.func.__doc__
    'I am: docstr.func.__doc__'
    >>> docstr.spam.__doc__
    'I am: spam.__doc__ or docstr.spam.__doc__'
    >>> docstr.spam.method.__doc__
    'I am: spam.method.__doc__ or self.method.__doc__'

Classes vs Modules
~~~~~~~~~~~~~~~~~~

Will be good to clarify the difference between this two Python namespaces,
because their are very similar.

* Modules

 * Are data/logic packages
 * Are created by writing Python files or C extensions
 * Are used by being imported

* Classes

 * Implement new objects
 * Are created by class statements
 * Are used by being called
 * Always live within a module

Is important to note that the `classes` support extra features that modules don't,
for example, the multiple instance generation, inheritance, etc.


Method overload
~~~~~~~~~~~~~~~

Another issue related to the method specialization
is the method overload.
If you are not familiarized with this concept,
in simple words consist to write more than one
method with the same name but with different
signature, it means that the arguments inside
the parenthesis is different.

A simple method overload can be:

::

    class ExampleClass():
        def average(self,x,y):
            return (x+y)/2
        def average(self,x,y,z):
            return (x+y+z)/3

But this example will not work,
because there are no type declarations
in Python, so, this concept does not apply,
because the polymorphism is based in the
object interfaces, not the types.

One patch, solution can be to use the `*args` parameter:

::

    class ExampleClass():
        def average(self, *args):
            if len(args) == 1:
                pass
            elif ... 


But this is not recommended too,
because we were losing the idea behind object oriented paradigm,
so, the next way to use this mechanism.

::

    class C:
        def average(self, x): # Assume x does the right thing
            x.operation()
    

Because with this implementation,
you can use the widely object-oriented. 
