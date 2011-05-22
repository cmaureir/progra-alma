Lecture 17 - Advanced topics on functions
------------------------------------------

When you read the lecture about the function,
maybe you had some questions about extra functions functionalities,
and the answer is yes.

Functions in Python are a very powerfull tool to the programmer,
if you learn some extra content.

Returning more than one value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One important thing to remember,
is that the Python functions can ``return`` any Python object,
so you can return anything.

For example, Lists:

::

   def f(var):
      my_list = [var*2,var*3,var*4,var*5]
      return my_list

or

::

   def f(var):
      return  [var*2,var*3,var*4,var*5]

Tuples:

::

   def f(var):
      return (var,var*var)

And so,
but the more important thing is that
you can return more than one object.

For example,
we can have a function to obtain the first
and last name for a determinated person,
so we will program that as following:

::
   
   def get_first_name():
      first = "John"
      return first

   def get_last_name():
      last = "Smith"
      return last

   firstname = get_first_name() 
   lastname = get_last_name() 

But we can do it in only one function:

::

   def get_names():
      first = "John"
      last ="Smith"
      return first,last

   firstname, lastname = get_names()


But be careful!
This return statements are not the same in all the cases:

::

   >>> def fun():
   ...    return (1,2)
   ... 
   >>> a = fun()
   >>> a
   (1, 2)
   >>> type(a)
   <type 'tuple'>
   >>> b,c = fun()
   >>> b
   1
   >>> c
   2
   >>> type(b)
   <type 'int'>
   >>> type(c)
   <type 'int'>


Means that if we assign a multiple return
function, the variable will be a tuple (immutable object),
including different types of objects:

::

   >>> def fun():
   ...   return [1,2],(3,4),5
   ... 
   >>> var = fun()
   >>> var
   ([1, 2], (3, 4), 5)


If you want to receive only one value in some cases,
you can use the ``_`` statement if you do not care about
the other values, for example:

::

   >>> def fun():
   ...   return [1,2],(3,4),5
   ... 
   >>> _,_,var = fun()
   >>> var
   5


Finally, you can user the return parameters from a function,
like a list, for example:

::

   >>> def fun():
   ...   return ['hello','bye'],(5,1)
   ... 
   >>> fun()[0]
   ['hello', 'bye']
   >>> fun()[1]
   (5, 1)
   >>> fun()[2]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: tuple index out of range


Returning functions
~~~~~~~~~~~~~~~~~~~



Default parameters
~~~~~~~~~~~~~~~~~~

When one or more top-level parameters have the form parameter = expression, the function is said to have “default parameter values.” For a parameter with a default value, the corresponding argument may be omitted from a call, in which case the parameter’s default value is substituted. If a parameter has a default value, all following parameters must also have a default value — this is a syntactic restriction that is not expressed by the grammar.

Default parameter values are evaluated when the function definition is executed. This means that the expression is evaluated once, when the function is defined, and that that same “pre-computed” value is used for each call. This is especially important to understand when a default parameter is a mutable object, such as a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), the default value is in effect modified. This is generally not what was intended. A way around this is to use None as the default, and explicitly test for it in the body of the function, e.g.:

def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin

Function call semantics are described in more detail in section Calls. A function call always assigns values to all parameters mentioned in the parameter list, either from position arguments, from keyword arguments, or from default values. If the form “*identifier” is present, it is initialized to a tuple receiving any excess positional parameters, defaulting to the empty tuple. If the form “**identifier” is present, it is initialized to a new dictionary receiving any excess keyword arguments, defaulting to a new empty dictionary.

It is also possible to create anonymous functions (functions not bound to a name), for immediate use in expressions. This uses lambda forms, described in section Lambdas. Note that the lambda form is merely a shorthand for a simplified function definition; a function defined in a “def” statement can be passed around or assigned to another name just like a function defined by a lambda form. The “def” form is actually more powerful since it allows the execution of multiple statements.

Programmer’s note: Functions are first-class objects. A “def” form executed inside a function definition defines a local function that can be returned or passed around. Free variables used in the nested function can access the local variables of the function containing the def. See section Naming and binding for details.


def f(a=[])
def f(a, b=2)



Function special parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f(a,b, *args)	
def f(a, b, **kwards)

How to use *args and **kwargs in Python
Date: 2008-01-03  |   Modified: 2010-03-15  |   Tags: python   |   63 Comments
Or, How to use variable length argument lists in Python.

The special syntax, *args and **kwargs in function definitions is used to pass a variable number of arguments to a function. The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, and the double asterisk form is used to pass a keyworded, variable-length argument list. Here is an example of how to use the non-keyworded form. This example passes one formal (positional) argument, and two more variable length arguments.

def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3)
Results:

formal arg: 1
another arg: two
another arg: 3

Here is an example of how to use the keyworded form. Again, one formal argument and two keyworded variable arguments are passed.

def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

test_var_kwargs(farg=1, myarg2="two", myarg3=3)
Results:

formal arg: 1
another keyword arg: myarg2: two
another keyword arg: myarg3: 3

Using *args and **kwargs when calling a function
This special syntax can be used, not only in function definitions, but also when calling a function.

def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3)
test_var_args_call(1, *args)
Results:

arg1: 1
arg2: two
arg3: 3
Here is an example using the keyworded form when calling a function:

def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)
Results:
