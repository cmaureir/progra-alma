Lecture 24 - Object-Oriented Programming - Design good practices
-----------------------------------------------------------------

The content of this lecture is based on the chapters 28 and 30
of the Learning Python 4th edition book.

.. como iniciar clases
.. clases cohecionadas
.. sin acoplamiento
.. no crear clases que lo hagan todo
.. clases representan entidades
.. Diseño OO


.. Learning Python 4th, chapter 28

The `class` Statement
~~~~~~~~~~~~~~~~~~~~~

The Python class statement is very similar to another languages statement,
but only by the *name*, because if we seee the closer implementation, is quite
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

To explain in more details the classes functionalities,
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
which are not inheritables by the objects,
for example:

::

    class MixedNames:# Define class
        data = 'spam'# Assign class attr
        def __init__(self, value):# Assign method name
            self.data = value # Assign instance attr
        def display(self):
            print(self.data, MixedNames.data) # Instance attr, class attr

This implementation contains a class variable called `data` (simple variable asignation), but
algo has an internal variable (inheritable) called `self.data` (class's local scope).

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


where the class is determined by locating the method name using Python’s inheritance
search procedure. In fact, both call forms are valid in Python.

Besides the normal inheritance of method attribute names, the special first argument
is the only real magic behind method calls. In a class method, the first argument is
usually called self by convention (technically, only its position is significant, not its
name). This argument provides methods with a hook back to the instance that is the
subject of the call—because classes generate many instance objects, they need to use
this argument to manage data that varies per instance.

C++ programmers may recognize Python’s self argument as being similar to C++’s
this pointer. In Python, though, self is always explicit in your code: methods must
always go through self to fetch or change attributes of the instance being processed
by the current method call. This explicit nature of self is by design—the presence of
this name makes it obvious that you are using instance attribute names in your script,
not names in the local or global scope.

Method Example

To clarify these concepts, let’s turn to an example. Suppose we define the following
class:

class NextClass: # Define class
    def printer(self, text): # Define method
        self.message = text # Change instance
        print(self.message) # Access instance

The name printer references a function object; because it’s assigned in the class state-
ment’s scope, it becomes a class object attribute and is inherited by every instance made
from the class. Normally, because methods like printer are designed to process in-
stances, we call them through instances:

>>> x = NextClass() # Make instance
>>> x.printer('instance call') # Call its method
instance call
>>> x.message  	# Instance changed
'instance call'

When we call the method by qualifying an instance like this, printer is first located by
inheritance, and then its self argument is automatically assigned the instance object
(x); the text argument gets the string passed at the call ('instance call'). Notice that
because Python automatically passes the first argument to self for us, we only actually
have to pass in one argument. Inside printer, the name self is used to access or set
per-instance data because it refers back to the instance currently being processed.

Methods may be called in one of two ways—through an instance, or through the class
itself. For example, we can also call printer by going through the class name, provided
we pass an instance to the self argument explicitly:

    >>> NextClass.printer(x, 'class call') # Direct class call
    class call


    >>> x.message # Instance changed again
    'class call'


Calls routed through the instance and the class have the exact same effect, as long as
we pass the same instance object ourselves in the class form. By default, in fact, you get
an error message if you try to call a method without any instance:

>>> NextClass.printer('bad call')
TypeError: unbound method printer() must be called with NextClass instance...


Calling Superclass Constructors

Methods are normally called through instances. Calls to methods through a class,
though, do show up in a variety of special roles. One common scenario involves the
constructor method. The __init__ method, like all attributes, is looked up by inheri-
tance. This means that at construction time, Python locates and calls just one
__init__. If subclass constructors need to guarantee that superclass construction-time
logic runs, too, they generally must call the superclass’s __init__ method explicitly
through the class:

class Super:
def __init__(self, x):
...default code...
class Sub(Super):
def __init__(self, x, y):
Super.__init__(self, x)
...custom code...
# Run superclass __init__
# Do my init actions
I = Sub(1, 2)

This is one of the few contexts in which your code is likely to call an operator over-
loading method directly. Naturally, you should only call the superclass constructor this
way if you really want it to run—without the call, the subclass replaces it completely.
For a more realistic illustration of this technique in action, see the Manager class example
in the prior chapter’s tutorial.

Other Method Call Possibilities

This pattern of calling methods through a class is the general basis of extending (instead
of completely replacing) inherited method behavior. In Chapter 31, we’ll also meet a
new option added in Python 2.2, static methods, that allow you to code methods that
do not expect instance objects in their first arguments. Such methods can act like simple
instanceless functions, with names that are local to the classes in which they are coded,
and may be used to manage class data. A related concept, the class method, receives a
class when called instead of an instance and can be used to manage per-class data. These
are advanced and optional extensions, though; normally, you must always pass an
instance to a method, whether it is called through an instance or a class.

Inheritance
~~~~~~~~~~~

In Python, inheritance happens when an object is qualified, and it involves searching
an attribute definition tree (one or more namespaces). Every time you use an expression
of the form object.attr (where object is an instance or class object), Python searches
the namespace tree from bottom to top, beginning with object, looking for the first
attr it can find. This includes references to self attributes in your methods. Because
lower definitions in the tree override higher ones, inheritance forms the basis of
specialization.

Attribute Tree Construction

Figure 28-1 summarizes the way namespace trees are constructed and populated with
names. Generally:

• Instance attributes are generated by assignments to self attributes in methods.
• Class attributes are created by statements (assignments) in class statements.
• Superclass links are made by listing classes in parentheses in a class statement
header.

The net result is a tree of attribute namespaces that leads from an instance, to the class
it was generated from, to all the superclasses listed in the class header. Python searches
upward in this tree, from instances to superclasses, each time you use qualification to
fetch an attribute name from an instance object.

Specializing Inherited Methods

The tree-searching model of inheritance just described turns out to be a great way to
specialize systems. Because inheritance finds names in subclasses before it checks su-
perclasses, subclasses can replace default behavior by redefining their superclasses’
attributes. In fact, you can build entire systems as hierarchies of classes, which are
extended by adding new external subclasses rather than changing existing logic
in-place.

The idea of redefining inherited names leads to a variety of specialization techniques.
For instance, subclasses may replace inherited attributes completely, provide attributes
that a superclass expects to find, and extend superclass methods by calling back to the
superclass from an overridden method. We’ve already seen replacement in action.
Here’s an example that shows how extension works:

::

    >>> class Super:
    ...    def method(self):
    ...    print('in Super.method')
    ...
    >>> class Sub(Super):
    ...    def method(self): # Override method
    ...    print('starting Sub.method') # Add actions here
    ...    Super.method(self) # Run default action
    ...    print('ending Sub.method')
    ...

DIAGRAMA


Namespaces
~~~~~~~~~~

Now that we’ve examined class and instance objects, the Python namespace story is
complete. For reference, I’ll quickly summarize all the rules used to resolve names here.
The first things you need to remember are that qualified and unqualified names are
treated differently, and that some scopes serve to initialize object namespaces:

• Unqualified names (e.g., X) deal with scopes.
• Qualified attribute names (e.g., object.X) use object namespaces.
• Some scopes initialize object namespaces (for modules and classes).

Simple Names: Global Unless Assigned

Unqualified simple names follow the LEGB lexical scoping rule outlined for functions
in Chapter 17:

Assignment (X = value)
	Makes names local: creates or changes the name X in the current local scope, unless
	declared global.

Reference (X)
	Looks for the name X in the current local scope, then any and all enclosing func-
	tions, then the current global scope, then the built-in scope.

Attribute Names: Object Namespaces

Qualified attribute names refer to attributes of specific objects and obey the rules for
modules and classes. For class and instance objects, the reference rules are augmented
to include the inheritance search procedure:

Assignment (object.X = value)
	Creates or alters the attribute name X in the namespace of the object being quali-
	fied, and none other. Inheritance-tree climbing happens only on attribute refer-
	ence, not on attribute assignment.
Reference (object.X)
	For class-based objects, searches for the attribute name X in object, then in all
	accessible classes above it, using the inheritance search procedure. For nonclass
	objects such as modules, fetches X from object directly.

The “Zen” of Python Namespaces: Assignments Classify Names

With distinct search procedures for qualified and unqualified names, and multiple
lookup layers for both, it can sometimes be difficult to tell where a name will wind up
going. In Python, the place where you assign a name is crucial—it fully determines the
scope or object in which a name will reside. The file manynames.py illustrates how this
principle translates to code and summarizes the namespace ideas we have seen through-
out this book:

::

    # manynames.py
    X = 11 # Global (module) name/attribute (X, or manynames.X)
    def f():
        print(X) # Access global X (11)
    def g():
        X = 22 # Local (function) variable (X, hides module X)
        print(X)
    class C:
        X = 33 # Class attribute (C.X)
        def m(self):
            X = 44 # Local variable in method (X)
            self.X = 55 # Instance attribute (instance.X)
    

This file assigns the same name, X, five times. Because this name is assigned in five
different locations, though, all five Xs in this program are completely different variables.
From top to bottom, the assignments to X here generate: a module attribute (11), a local
variable in a function (22), a class attribute (33), a local variable in a method (44), and
an instance attribute (55). Although all five are named X, the fact that they are all as-
signed at different places in the source code or to different objects makes all of these
unique variables.

You should take the time to study this example carefully because it collects ideas we’ve
been exploring throughout the last few parts of this book. When it makes sense to you,
you will have achieved a sort of Python namespace nirvana. Of course, an alternative
route to nirvana is to simply run the program and see what happens. Here’s the re-
mainder of this source file, which makes an instance and prints all the Xs that it can fetch:

# manynames.py, continued
if __name__ == '__main__':
    print(X) # 11: module (a.k.a. manynames.X outside file)
    f() # 11: global
    g() # 22: local
    print(X) # 11: module name unchanged

    obj = C() # Make instance
    print(obj.X)  # 33: class name inherited by instance
    
    obj.m() # Attach attribute name X to instance now
    print(obj.X) # 55: instance
    print(C.X) # 33: class (a.k.a. obj.X if no X in instance)
    
    #print(C.m.X) # FAILS: only visible in method
    #print(g.X) # FAILS: only visible in function
    
The outputs that are printed when the file is run are noted in the comments in the code;
trace through them to see which variable named X is being accessed each time. Notice
in particular that we can go through the class to fetch its attribute (C.X), but we can
never fetch local variables in functions or methods from outside their def statements.
Locals are visible only to other code within the def, and in fact only live in memory
while a call to the function or method is executing.

Some of the names defined by this file are visible outside the file to other modules, but
recall that we must always import before we can access names in another file—that is
the main point of modules, after all:

# otherfile.py
import manynames
X = 66
print(X)
print(manynames.X)
# 66: the global here
# 11: globals become attributes after imports
manynames.f()
manynames.g()
# 11: manynames's X, not the one here!
# 22: local in other file's function
print(manynames.C.X)
I = manynames.C()
print(I.X)
I.m()
print(I.X)
# 33: attribute of class in other module
# 33: still from class here
# 55: now from instance!


Notice here how manynames.f() prints the X in manynames, not the X assigned in this file—
scopes are always determined by the position of assignments in your source code (i.e.,
lexically) and are never influenced by what imports what or who imports whom. Also,
notice that the instance’s own X is not created until we call I.m()—attributes, like all
variables, spring into existence when assigned, and not before. Normally we create
instance attributes by assigning them in class __init__ constructor methods, but this
isn’t the only option.

Finally, as we learned in Chapter 17, it’s also possible for a function to change names
outside itself, with global and (in Python 3.0) nonlocal statements—these statements
provide write access, but also modify assignment’s namespace binding rules:

X = 11
# Global in module
def g1():
print(X)
# Reference global in module
def g2():
global X
X = 22
# Change global in module
def h1():
X = 33
def nested():
print(X)
def h2():
X = 33
def nested():
nonlocal X
X = 44
# Local in function
# Reference local in enclosing scope
# Local in function
# Python 3.0 statement
# Change local in enclosing scope

Of course, you generally shouldn’t use the same name for every variable in your script—
but as this example demonstrates, even if you do, Python’s namespaces will work to
keep names used in one context from accidentally clashing with those used in another.

Documentation
~~~~~~~~~~~~~

The docstring can be used by classes and by the class components,
being strings literals to describe the mechanism and details of some
Python statement, using the `__doc__` reserver function.
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

Python and OOP
~~~~~~~~~~~~~~

Let’s begin with a review—Python’s implementation of OOP can be summarized by
three ideas:

Inheritance
	Inheritance is based on attribute lookup in Python (in X.name expressions).

Polymorphism
	In X.method, the meaning of method depends on the type (class) of X.

Encapsulation
	Methods and operators implement behavior; data hiding is a convention by default.

By now, you should have a good feel for what inheritance is all about in Python. We’ve
also talked about Python’s polymorphism a few times already; it flows from Python’s
lack of type declarations. Because attributes are always resolved at runtime, objects that
implement the same interfaces are interchangeable; clients don’t need to know what
sorts of objects are implementing the methods they call.

Encapsulation means packaging in Python—that is, hiding implementation details be-
hind an object’s interface. It does not mean enforced privacy, though that can be
implemented with code, as we’ll see in Chapter 38. Encapsulation allows the imple-
mentation of an object’s interface to be changed without impacting the users of that
object.

Overloading by Call Signatures (or Not)

Some OOP languages also define polymorphism to mean overloading functions based
on the type signatures of their arguments. But because there are no type declarations
in Python, this concept doesn’t really apply; polymorphism in Python is based on object
interfaces, not types.

You can try to overload methods by their argument lists, like this:

class C:
def meth(self, x):
...
def meth(self, x, y, z):
...

This code will run, but because the def simply assigns an object to a name in the class’s
scope, the last definition of the method function is the only one that will be retained
(it’s just as if you say X = 1 and then X = 2; X will be 2).

Type-based selections can always be coded using the type-testing ideas we met in
Chapters 4 and 9, or the argument list tools introduced in Chapter 18:

::

    class C:
        def meth(self, *args):
            if len(args) == 1:
            ...
            elif type(arg[0]) == int:
            ...

You normally shouldn’t do this, though—as described in Chapter 16, you should write
your code to expect an object interface, not a specific data type. That way, it will be
useful for a broader category of types and applications, both now and in the future:

class C:
def meth(self, x):
x.operation()
# Assume x does the right thing

It’s also generally considered better to use distinct method names for distinct opera-
tions, rather than relying on call signatures (no matter what language you code in).

Although Python’s object model is straightforward, much of the art in OOP is in the
way we combine classes to achieve a program’s goals. The next section begins a tour
of some of the ways larger programs use classes to their advantage.


`Is-a` relationships
~~~~~~~~~~~~~~~~~~~~

We’ve explored the mechanics of inheritance in depth already, but I’d like to show you
an example of how it can be used to model real-world relationships. From a program-
mer’s point of view, inheritance is kicked off by attribute qualifications, which trigger
searches for names in instances, their classes, and then any superclasses. From a de-
signer’s point of view, inheritance is a way to specify set membership: a class defines a
set of properties that may be inherited and customized by more specific sets (i.e.,
subclasses).

To illustrate, let’s put that pizza-making robot we talked about at the start of this part
of the book to work. Suppose we’ve decided to explore alternative career paths and
open a pizza restaurant. One of the first things we’ll need to do is hire employees to
serve customers, prepare the food, and so on. Being engineers at heart, we’ve decided
to build a robot to make the pizzas; but being politically and cybernetically correct,
we’ve also decided to make our robot a full-fledged employee with a salary.

Our pizza shop team can be defined by the four classes in the example file,
employees.py. The most general class, Employee, provides common behavior such as
bumping up salaries (giveRaise) and printing (__repr__). There are two kinds of em-
ployees, and so two subclasses of Employee: Chef and Server. Both override the inherited
work method to print more specific messages. Finally, our pizza robot is modeled by an
even more specific class: PizzaRobot is a kind of Chef, which is a kind of Employee. In
OOP terms, we call these relationships “is-a” links: a robot is a chef, which is a(n)
employee. Here’s the employees.py file:

class Employee:
def __init__(self, name, salary=0):
self.name
= name
self.salary = salary
def giveRaise(self, percent):
self.salary = self.salary + (self.salary * percent)
def work(self):
print(self.name, "does stuff")
def __repr__(self):
return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
class Chef(Employee):
def __init__(self, name):
Employee.__init__(self, name, 50000)
def work(self):
print(self.name, "makes food")
class Server(Employee):
def __init__(self, name):
Employee.__init__(self, name, 40000)
def work(self):
print(self.name, "interfaces with customer")
class PizzaRobot(Chef):

def __init__(self, name):
Chef.__init__(self, name)
def work(self):
print(self.name, "makes pizza")
if __name__ == "__main__":
bob = PizzaRobot('bob')
print(bob)
bob.work()
bob.giveRaise(0.20)
print(bob); print()
# Make a robot named bob
# Run inherited __repr__
# Run type-specific action
# Give bob a 20% raise
for klass in Employee, Chef, Server, PizzaRobot:
obj = klass(klass.__name__)
obj.work()

When we run the self-test code included in this module, we create a pizza-making robot
named bob, which inherits names from three classes: PizzaRobot, Chef, and Employee.
For instance, printing bob runs the Employee.__repr__ method, and giving bob a raise
invokes Employee.giveRaise because that’s where the inheritance search finds that
method:

C:\python\examples> python employees.py
<Employee: name=bob, salary=50000>
bob makes pizza
<Employee: name=bob, salary=60000.0>
Employee does stuff
Chef makes food
Server interfaces with customer
PizzaRobot makes pizza

In a class hierarchy like this, you can usually make instances of any of the classes, not
just the ones at the bottom. For instance, the for loop in this module’s self-test code
creates instances of all four classes; each responds differently when asked to work be-
cause the work method is different in each. Really, these classes just simulate real-world
objects; work prints a message for the time being, but it could be expanded to do real
work later.


`Has-a` relationships
~~~~~~~~~~~~~~~~~~~~~

The notion of composition was introduced in Chapter 25. From a programmer’s point
of view, composition involves embedding other objects in a container object, and ac-
tivating them to implement container methods. To a designer, composition is another
way to represent relationships in a problem domain. But, rather than set membership,
composition has to do with components—parts of a whole.

Composition also reflects the relationships between parts, called a “has-a” relation-
ships. Some OOP design texts refer to composition as aggregation (or distinguish be-
tween the two terms by using aggregation to describe a weaker dependency between
container and contained); in this text, a “composition” simply refers to a collection of
embedded objects. The composite class generally provides an interface all its own and
implements it by directing the embedded objects.

Now that we’ve implemented our employees, let’s put them in the pizza shop and let
them get busy. Our pizza shop is a composite object: it has an oven, and it has employees
like servers and chefs. When a customer enters and places an order, the components
of the shop spring into action—the server takes the order, the chef makes the pizza,
and so on. The following example (the file pizzashop.py) simulates all the objects and
relationships in this scenario:

from employees import PizzaRobot, Server
class Customer:
def __init__(self, name):
self.name = name
def order(self, server):
print(self.name, "orders from", server)
def pay(self, server):
print(self.name, "pays for item to", server)
class Oven:
def bake(self):
print("oven bakes")
class PizzaShop:
def __init__(self):
self.server = Server('Pat')
self.chef
= PizzaRobot('Bob')
self.oven
= Oven()
def order(self, name):
customer = Customer(name)
customer.order(self.server)
self.chef.work()
self.oven.bake()
customer.pay(self.server)
if __name__ == "__main__":
scene = PizzaShop()
scene.order('Homer')
print('...')
scene.order('Shaggy')
# Embed other objects
# A robot named bob
# Activate other objects
# Customer orders from server
# Make the composite
# Simulate Homer's order
# Simulate Shaggy's order

The PizzaShop class is a container and controller; its constructor makes and embeds
instances of the employee classes we wrote in the last section, as well as an Oven class
defined here. When this module’s self-test code calls the PizzaShop order method, the
embedded objects are asked to carry out their actions in turn. Notice that we make a
new Customer object for each order, and we pass on the embedded Server object to
Customer methods; customers come and go, but the server is part of the pizza shop
composite. Also notice that employees are still involved in an inheritance relationship;
composition and inheritance are complementary tools.

When we run this module, our pizza shop handles two orders—one from Homer, and
then one from Shaggy:
C:\python\examples> python pizzashop.py
Homer orders from <Employee: name=Pat, salary=40000>
Bob makes pizza
oven bakes
Homer pays for item to <Employee: name=Pat, salary=40000>
...
Shaggy orders from <Employee: name=Pat, salary=40000>
Bob makes pizza
oven bakes
Shaggy pays for item to <Employee: name=Pat, salary=40000>

Again, this is mostly just a toy simulation, but the objects and interactions are repre-
sentative of composites at work. As a rule of thumb, classes can represent just about
any objects and relationships you can express in a sentence; just replace nouns with
classes, and verbs with methods, and you’ll have a first cut at a design.

Stream Processors Revisited

For a more realistic composition example, recall the generic data stream processor
function we partially coded in the introduction to OOP in Chapter 25:

def processor(reader, converter, writer):
while 1:
data = reader.read()
if not data: break
data = converter(data)
writer.write(data)

Rather than using a simple function here, we might code this as a class that uses com-
position to do its work to provide more structure and support inheritance. The fol-
lowing file, streams.py, demonstrates one way to code the class:

class Processor:
def __init__(self, reader, writer):
self.reader = reader
self.writer = writer
def process(self):
while 1:
data = self.reader.readline()
if not data: break
data = self.converter(data)
self.writer.write(data)
def converter(self, data):
assert False, 'converter must be defined'
# Or raise exception

This class defines a converter method that it expects subclasses to fill in; it’s an example
of the abstract superclass model we outlined in Chapter 28 (more on assert in
Part VII). Coded this way, reader and writer objects are embedded within the class
instance (composition), and we supply the conversion logic in a subclass rather than
passing in a converter function (inheritance). The file converters.py shows how:


from streams import Processor
class Uppercase(Processor):
def converter(self, data):
return data.upper()
if __name__ == '__main__':
import sys
obj = Uppercase(open('spam.txt'), sys.stdout)
obj.process()

Here, the Uppercase class inherits the stream-processing loop logic (and anything else
that may be coded in its superclasses). It needs to define only what is unique about it—
the data conversion logic. When this file is run, it makes and runs an instance that reads
from the file spam.txt and writes the uppercase equivalent of that file to the stdout
stream:

C:\lp4e> type spam.txt
spam
Spam
SPAM!
C:\lp4e> python converters.py
SPAM
SPAM
SPAM!

To process different sorts of streams, pass in different sorts of objects to the class con-
struction call. Here, we use an output file instead of a stream:

C:\lp4e> python
>>> import converters
>>> prog = converters.Uppercase(open('spam.txt'), open('spamup.txt', 'w'))
>>> prog.process()
C:\lp4e> type spamup.txt
SPAM
SPAM
SPAM!

But, as suggested earlier, we could also pass in arbitrary objects wrapped up in classes
that define the required input and output method interfaces. Here’s a simple example
that passes in a writer class that wraps up the text inside HTML tags:

C:\lp4e> python
>>> from converters import Uppercase
>>>
>>> class HTMLize:
...
def write(self, line):
...
print('<PRE>%s</PRE>' % line.rstrip())
...
>>> Uppercase(open('spam.txt'), HTMLize()).process()
<PRE>SPAM</PRE>
<PRE>SPAM</PRE>
<PRE>SPAM!</PRE>

If you trace through this example’s control flow, you’ll see that we get both uppercase
conversion (by inheritance) and HTML formatting (by composition), even though the
core processing logic in the original Processor superclass knows nothing about either
step. The processing code only cares that writers have a write method and that a method
named convert is defined; it doesn’t care what those methods do when they are called.
Such polymorphism and encapsulation of logic is behind much of the power of classes.

As is, the Processor superclass only provides a file-scanning loop. In more realistic
work, we might extend it to support additional programming tools for its subclasses,
and, in the process, turn it into a full-blown framework. Coding such a tool once in a
superclass enables you to reuse it in all of your programs. Even in this simple example,
because so much is packaged and inherited with classes, all we had to code was the
HTML formatting step; the rest was free.

For another example of composition at work, see exercise 9 at the end of Chapter 31
and its solution in Appendix B; it’s similar to the pizza shop example. We’ve focused
on inheritance in this book because that is the main tool that the Python language itself
provides for OOP. But, in practice, composition is used as much as inheritance as a
way to structure classes, especially in larger systems. As we’ve seen, inheritance and
composition are often complementary (and sometimes alternative) techniques. Because
composition is a design issue outside the scope of the Python language and this book,
though, I’ll defer to other resources for more on this topic.

