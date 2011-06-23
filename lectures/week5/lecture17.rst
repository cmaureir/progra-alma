Lecture 17 - Advanced topics on functions
------------------------------------------

When you read the lecture about functions,
maybe you had some questions about the existence of extra function functionality,
and the answer is yes.

Functions in Python are a very powerful tool for the programmer,
if you learn some extra content.

Returning more than one value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One important thing to remember,
is that Python functions can ``return`` any Python object,
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

And so forth,
but the most important thing is that
you can return more than one object.

For example,
we can have a function to obtain the first
and last name for a determined person,
so we will usually program that as follows:

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
      last = "Smith"
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


Finally, you can use the return parameters from a function,
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


Default parameters
~~~~~~~~~~~~~~~~~~

In some cases, a function parameter is not necessary
or in some cases it requires special statements for initialization
or a different treatment.

The form of the *default parameters* is like a normal assignation,
it means `parameter=expression`.

If a parameter has a default value, the argument may be omitted from a call,
substituting the default value.

The *default parameters* are evaluated when the function definition is executed,
it means only once per script execution, using that value for each call.
In other words, the *default parameter* is a mutable object, because it is modifiable
by the user.

To explain the idea of a *default parameter*
look at the following example::

    >>> def example(var=None):
    ...   if var is None:
    ...     print 'ok, the variable is None'
    ...   else:
    ...     print 'the value of var is',var
    ... 
    >>> example()
    ok, the variable is None
    >>> example(var=10)
    the value of var is 10
    >>> example(var=None)
    ok, the variable is None
    >>> example(var='test')
    the value of var is test
    >>> var2 = 'hello'
    >>> example(var2)
    the value of var is hello



The *default parameters* can also be used by any data type,
for example::

    >>> def f(a,b=2):
    ...   print a,b
    ... 
    >>> f(1)
    1 2
    >>> f('a')
    a 2
    >>> f('a',1)
    a 1
    >>> f('a','b')
    a b

Finally, you can also use the *default parameter* to store
parameters if needed, like the following example::

    >>> def f(a=[]):
    ...  a.append(1)
    ...  return a
    ... 
    >>> f()
    [1]
    >>> f()
    [1, 1]
    >>> f()
    [1, 1, 1]
    >>> f([])
    [1]
    >>> f([2,3])
    [2, 3, 1]

Function special parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The special parameters is the main idea of the use of `*args` and `**kwargs`,
which means variable length argument lists.

The syntax of these special arguments, is used to pass variable number of arguments in a function,
the first case, `*args` is widely used to pass a non-keyworded variable length argument list,
and the second case, `**kwargs` is used to pass a keyworded variable length argument list.

In other words, the structure of these different special parameters is as follows:

* `*args`, simple multiple parameters::

    >>> def f(*args):
    ...   for i in args:
    ...     print 'argument:',i
    ... 
    >>> f()
    >>> f(23)
    argument: 23
    >>> f(23,'hello')
    argument: 23
    argument: hello
    >>> f(23,'hello',[1,2,3])
    argument: 23
    argument: hello
    argument: [1, 2, 3]
    >>> f(23,'hello',[1,2,3], set(['red','blue']))
    argument: 23
    argument: hello
    argument: [1, 2, 3]
    argument: set(['blue', 'red'])

  And if you want to know the `args` data type::

    >>> def f(*args):
    ...   print args
    ... 
    >>> f(1,[2,3],set(['hello','world']))
    (1, [2, 3], set(['world', 'hello']))

  It means, that the `args` variable is a tuple.


* `**kwargs`, argument with a name:: 

    >>> def f(**kwargs):
    ...   for i in kwargs:
    ...     print i,
    ...   print '...'
    ...   for j in kwargs.values():
    ...     print j,
    ... 
    >>> f(a='hello',tmp='world',number=42)
    a tmp number ...
    hello world 42
    >>> f()
    ...
    >>> f(number=10)
    number ...
    10

  And if you want to know the `kwargs` data type::

    >>> def f(**kwargs):
    ...   print kwargs
    ... 
    >>> f(a='hello', b = 45)
    {'a': 'hello', 'b': 45}
    >>> f(a='hello', b = 45, tmp = {'i':'bye','j':'thanks'})
    {'a': 'hello', 'tmp': {'i': 'bye', 'j': 'thanks'}, 'b': 45}
    >>> 

  It means, that the `kwargs` variable is a dictionary.


  But, this special arguments are not exclusive, you can use both, indeed,
  with additional normal arguments::

    >>> def f(arg0,*args,**kwargs):
    ...   print arg0
    ...   print args
    ...   print kwargs
    ... 
    >>> f(42)
    42
    ()
    {}
    >>> f(42,[1,2])
    42
    ([1, 2],)
    {}
    >>> f(42,[1,2],'hello')
    42
    ([1, 2], 'hello')
    {}
    >>> f(42,[1,2],'hello',tmp=(0,0))
    42
    ([1, 2], 'hello')
    {'tmp': (0, 0)}
    >>> f(42,[1,2],'hello',tmp=(0,0),var={'foo':'bar'})
    42
    ([1, 2], 'hello')
    {'tmp': (0, 0), 'var': {'foo': 'bar'}}

  Be careful with the argument order!::

    >>> f(42,[1,2],var='bye','hello',tmp=(0,0))
      File "<stdin>", line 1
    SyntaxError: non-keyword arg after keyword arg


  There is another way to use this *special parameters*,
  by passing the `*args` and/or `**kwargs` as a parameter
  when the function is called.

  Lets see the following example::

    >>> def f(arg0,arg1):
    ...   print arg0
    ...   print arg1
    ... 
    >>> args = ('hello',42)
    >>> f(*args)
    hello
    42


  The same idea works with a keyworded parameter::

    >>> def f(arg0,arg1):
    ...   print arg0
    ...   print arg1
    ... 
    >>> kwargs = {'arg0': 42, 'arg1': 100}
    >>> f(**kwargs)
    42
    100

Exercises
~~~~~~~~~~

* One of the most used methods by the system administrators to generate password
  to their servers is to choose a phrase and change some vocals to numbers
  (remember the exercise in the lecture 11), for example::

     "new password"

  will be::

     "n3w p4ssw0rd"

  So the changes will be:
  
  .. math::

      'a' \rightarrow '4'\\
      'e' \rightarrow '3'\\
      'i' \rightarrow '1'\\
      'o' \rightarrow '0'
  
  But, this changes can be modified by the user,
  for example, maybe the system administrators wants to change only
  the 'i' for the character '&'.

  Write a function which returns the original password, the modified one,
  and the dictionary used, also this function must have the default previous
  configuration, but the user must modified some character if their wants.

  ::

      >>> passw = 'hello world'
      >>> change_password(passw)
      'hello world' to 'h3ll0 w0rld' using dictionary {'a':'4','e':'3','i':'1','o':'0'}
      >>> change_password(passw,{'e':'@','o':'9'})
      'hello world' to 'h@ll9 w9rld' {'e':'@','o':'9'}

  **Note**: Use *default parameters* and *return more than one value*

* Write a function which receive as parameter a undefined quantity of numbers
  and calculate the average of that numbers::

      >>> average(1)
      1
      >>> average(1,2,3,4,5)
      3
      >>> average(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
      8
      >>> average(3.14, 2.71, 5.76, 0.0000001)
      2.902500025

* If you develop the previous exercise without much details
  it is possible if you run the function without arguments,
  you will receive::

      >>> average()
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 5, in average
      ZeroDivisionError: integer division or modulo by zero

  Avoid this situation, but not using a `if` statement to verify if the count is zero.

* Write a function to calculate the `Value Added Tax (VAT)`_
  of several products given by the user (consider VAT as 10%).
 
  Print the VAT for each product::

     >>> vat(Rice=1250,Meat=5670,Beer=4000,Soap=300)
     VAT Beer 400.0
     VAT Rice 125.0
     VAT Meat 567.0
     VAT Soap 30.0

  .. _`Value Added Tax (VAT)`: http://en.wikipedia.org/wiki/Value_added_tax
