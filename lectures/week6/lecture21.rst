Lecture 21 - Object-Oriented Programming - Class creation
----------------------------------------------------------

The object-oriented (OO) programming paradigm,
is widely used in serious project,
the main idea is to work with objects as data structures,
which contain a lot of functionality programmed by
the user, called methods, giving the chance to interact
with another objects.

There are some concepts in the object-oriented paradigm,
which will be explained in this lectures, like,
polymorphism, modularity, encapsulation, etc.

The modern and robust programming languages
support object-oriented programming,
like, *C++*, *Java*, *.NET*, etc.

Understanding the OO paradigm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A very simple example to understand the idea behind
the **classes** and **objects**, is the following:

A **human** being is an animal specie,
which can *walk*, *talk*, *run*, *jump*, etc.
We are humans, so, we are types of humans.

So, we can think the concepts, as  the following,

* Human, will be a *class*,
* Functionalists (walk, talk, etc) will be *methods*,
* We, people, are *objects* of the *human class*.

*Objects* (humans) can *walk*, *talk*, etc.
because we inherit the **methods** from the **class** Human.

Formally,
and *object* is an instance of a *class*

There are five main reasons to use OO,

* **Inheritance**, we can obtain special object, which
  inherit some *methods* from main *class*, so can
  be reused by all the class objects. Also, we can develop
  *classes* who inherit a structure from another *class*.
* **Composition**, you can see an object as a composition
  of component working together. (methods, attributes)
* **Multiple instances**, you can create more than one
  object for each class.
* **Customization via inheritance**, you can instance an object
  from a class, adding new attributes, and methods, which is
  the customization of an existing object which previously
  has a inherit from the main class.
* **Operator overloading**, you can develop and operator
  which could be called, using different parameters.


Following, we will explain the previous terms,
writing in code, to make more easy to understand the OO
paradigm.

Class and Objects
~~~~~~~~~~~~~~~~~~

A **class** is like an instance factory,
in which their attributes, variable, functions, etc;
provide a certain behavior for all the instances.

An **instance** represent the concrete items in a program's
domain. An instance will be the object, something called as,
a class abstraction.

A **method** is a functionality inside a class,
in simple words, a method is a function inside
a class with the parameter *self* as the first argument.

A **constructor** is a special method called *__init__* inside a class,
which initialize the attributes with a certain value,
the class attributes must be written with a *self*
statement before their name.


A Python class will be wrote as follow:

::

    >>> class my_class():
    ...    def __init__(self): # Constructor
    ...        self.first_attribute = 0 # atribute
    ...        self.second_attribute = 3.14 # attribute
    ...    def my_method(self, my_parameter): # method
    ...        return my_parameter * 2

An object will be create as follow:

::

    >>> my_object = my_class()
    >>> my_object
    <__main__.my_class instance at 0xb74218ac>

The attributes and methods will be callable as follow:

::

    >>> my_object.first_attribute
    0
    >>> my_object.second_attribute
    3.14
    >>> my_object.my_method('hello')
    'hellohello'
    >>> my_object.my_method(2)
    4

You can *instance* every *object* as you want from a *class*.

The __init__ method
~~~~~~~~~~~~~~~~~~~~

Lets look deeply into the *__init__* method.

As we mention earlier, the idea of a class is be an object
factory, so, we will need a more *personalized* objects
from a class, it means give some initial arguments
to build an object.

The *__init__* method will be able to manipulate
the arguments of a class, passing in the object contructor.

For example:

::

    class Square():
        def __init__(self, length, width):
            self.length = length
            self.width = width
        def perimeter(self):
            return 2 * (self.length + self.width)
        def area(self):
            return self.length * self.width

If you can see the *__init__* method has two
extra argument, *length* and *width* and in the body
of the *__init__* method, is applied an initialization
of two internal class variables, *self.length* and *self.width*.

So, how we can pass these two arguments?
We can pass the value of the attributes inside the class
parenthesis:

::

    >>> my_square = Square(3,4)
    >>> type(my_square)
    <type 'instance'>
    >>> my_square.length
    3
    >>> my_square.width
    4
    >>> my_square.perimeter()
    14
    >>> my_square.area()
    12
    >>> another_square = Square(2,2)
    >>> another_square.width, another_square.length
    (2, 2)
    >>> another_square.perimeter()
    8
    >>> another_square.area()
    4



Exercises
~~~~~~~~~

* PENDING
* PENDING
* PENDING

.. MyBag. con metodos para agregar elementos, ordenar, sacar, verificar repetidos, buscar elementos, imprimir, 
.. Vectors, (x,y) calcular distancia entre puntos, y otras cosas
.. Polinomios, construirlos y mostrarlos, operaciones de mult, sum, resta, solve, etc
.. Generar piezas de ajedres y simular el movimiento de una a una.
.. Dos personas que intercambian laminas
.. Generar dispositivos que van generando datos pero que pueden tener errores y cambian estados o enrtegan datos manipulados.
.. Cubo y Bola  obtener area y volumen
