Lecture 21 - Class creation
----------------------------

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

    .. image:: ../../diagrams/object-interaction.png
       :alt: (object interaction diagram)

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
    ...        self.first_attribute = 0 # attribute
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
the arguments of a class, passing in the object constructor.

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

* Lets consider a class called `Bag`, which will provide a lot of functionalities.
  To personalize my own bag (instance) with a certain total volume, each element has a name and dimensions
  (width, height, profundity (z))

  Create the class `Bag` and develop the following methods:
  
  * Sort the bag elements by volume,
  * Add new elements,
  * Remove elements,
  * Search elements with a given volume,
  * Show elements with the same volume,
  * Put the whole content of my bag in another new bag.

* The vectors in two dimensions are structures which contain two pair of coordinates:

  ::

      x1, y1, x2, y2

  which means that the origin point is constructed by ``(x1,y1)`` and the end of the vector
  is giving by ``(x2,y2)``.

  Create a class called `Vector` which contain the previous variables as local variables,
  and provide the following methods:

  * Imagine the vector as the diagonal of a rectangle, so, now it is possible to calculate
    the rectangle area. Create a method to calculate the associated rectangle area.
  * Calculate the distance between the points of the vector.
    Remember that the distance can be calculated as follows:

    .. math::

        distance = \sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}
      
* The previous exercise consider a vector with a position in the space,
  because we have the origin and destiny point.
  Lets consider now vectors but without a position in the space,
  it means, we provide a vector with one x and y component,
  for example the vector ``(3,4)`` will be a vector 

  .. image:: ../../diagrams/simple-vector.png 
     :alt: (simple-vector diagram)
 
  Develop a class called `Vector` which provide the following methods:

  * The method will receive an object, which will be another `Vector`
    and will calculate the addition of both vectors, for example
    the addition of the vectors ``(1,3)`` and ``(4,2)`` will be ``(5,5)``.

    .. image:: ../../diagrams/suma-vectores.png 
       :alt: (addition-vector diagram)

  * The method will receive an object, which will be another `Vector`
    and will calculate the subtraction of both vectors, for example
    the subtraction of the vectors ``(4,2)`` and ``(1,-2)`` will be ``(3,4)``.

    .. image:: ../../diagrams/resta-vectores.png 
       :alt: (subtraction-vector diagram)

  * The method will receive an object, which will be another `Vector`
    and will calculate the angle between both vectors, for example
    the angle between the vectors ``(3,0)`` and ``(5,5)`` is `\alpha = 45^{o}`.

    .. image:: ../../diagrams/angulo-vectores.png 
       :alt: (angle-vector diagram)

    Remember the formula:

    .. math::
    
        \vec{u} = (3,0) \\
        \vec{v} = (5,5) \\
        \cos \alpha = \frac{3\cdot 5 + 0\cdot 5}{\sqrt{3^{2} + 0^{2}} \cdot \sqrt{5^{2}+5^{2}}} = \frac{\sqrt{2}}{2}
    
     

* Create two classes called `Cube` and `Sphere`, which receive the dimensions, and radius respectively,
  and provide three methods:

  * ``get_area(self)``, which return the figure area.
  * ``get_volume(self)``, which return the figure volume.
  * ``get_difference(self,object)``, which return the volume difference between the figure and an object
    of the same kind, giving as parameter.
