Lecture 14 - Modules creation
-----------------------------
.. index:: module (creation)

A simple module is simply a file with Python code.
The name of the file indicates which is the module name.

For example, we can create a file called ``parity.py``
which have functions related to the parity numbers.::

 def is_even(n):
    return n % 2 == 0

 def is_odd(n):
    return not es_par(n)

 def to_even(n):
    return range(0, n, 2)

In this case, the name of the module is ``parity``.
To use the functions in another program, the file ``parity.py`` must be
in the same folder that the program.

For example,
the ``show_even.py`` program can be 
written as follows::

 from parity import to_even

 n = int(raw_input('Enter an integer: '))
 print 'The even number to', n, 'are:'
 for i in to_even(n):
    print i

And the ``check_even.py`` program
can be written as follows::

 import parity

 n = int(raw_input('Enter an integer: '))
 if parity.is_even(n):
    print n, 'is even'
 else:
    print n, 'is odd'

As seen, both programs can use objects defined in the module 
simply by importing it.

Use modules as programs
~~~~~~~~~~~~~~~~~~~~~~~

A file with ``.py`` extension can be either a module or a program.
If is a module, it contains definitions that can be imported from a program or other module.
If is a program, it contains code to be executed.

Sometimes, a program also contains definitions
(for example, functions and variables)
which also may be useful from another program.
However, cannot be imported,
because by using the ``import`` statement
the full program will be executed.
What would happen in this case,
to run the second program,
also will run the first.

There is a trick to avoid this problem:
whenever there is code  being executed,
exist a variable called ``__name__``.
When is a program,
the value of this variable is ``__main__``,
while in the module,
is the module name.

Therefore, 
you can use the value of this variable to mark
the program part to be executed to run the file, 
but not to import it.

For example,
the following program converts 
measurement units of length:

.. literalinclude:: ../../_static/programs/unit_conversion.py

This program is useful by itself,
but also their four functions and 
constants ``km_per_mile`` and ``cm_per_inch``
might be useful for use in another program.

To put the body of the program inside 
of the ``if __name__ == '__main__'``,
the file can be use like a module.
If we did not do this,
whenever the other program import a function
will be executed the whole program.

Try it: `download the program`_ and run it.
Then, write another program to import some of the functions.
Next, do the same,
but removing the ``if`` statement.


.. _download the program: ../_static/programs/unit_conversion.py

Exercises
~~~~~~~~~

#. Write a module called ``lists.py``
   which contains the following functions.
   
   * A function called ``average(l)``,
     and the ``l`` parameter will be a real number list,
     and return the average of these numbers::
   
       >>> average([7.0, 3.1, 1.7])
       3.933333333333333
       >>> average([1, 4, 9, 16])
       7.5
   
   * A function called ``squares(l)``,
     which return a list with the squares of the ``l`` values::
   
       >>> squares([1, 2, 3, 4, 5])
       [1, 4, 9, 16, 25]
       >>> squares([3.4, 1.2])
       [11.559999999999999, 1.44]
   
   * A function called ``longest(words)``,
     and the ``words`` parameter is a string list,
     which return the longest string::
   
       >>> longest(['mouse', 'hippo', 'dog', 'giraffe'])
       'giraffe'
       >>> longest(['****', '**', '********', '**'])
       '********'
   
     If there are more than one longest word (with the same lenght)
     is necesary to return only one.

#. Write a module called ``my_math.py``
   wich contains the following functions.

   * A function called ``my_sin(x)``
     which calculates the sine of an ``x`` value.

     The ``sine`` function can be represented as the following infinite sum:

     .. math::
 
         \sin{x}\ =\ \frac{x^{1}}{1!} - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \frac{x^{11}}{11!} - \frac{x^{13}}{13!} + \ldots 

     The terms are getting smaller,  
     so taking only some of the first terms is possible to reach a good approximation.

     Choose an amount of terms to calculate the ``sine``.
     Compare your results with the ``sin`` function from the ``math`` module.

   * A function called ``my_cos(x)``
     which calculates the cosine of an ``x`` value.

     The ``cosine`` function can be represented as the following infinite sum:

     .. math::
 
         \cos{x}\ =\ 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \frac{x^{8}}{8!} - \frac{x^{12}}{12!} + \ldots 

     The terms are getting smaller,  
     so taking only some of the first terms is possible to reach a good approximation.

     Choose an amount of terms to calculate the ``cosine``.
     Compare your results with the ``cos`` function from the ``math`` module.

   * A function called ``exponential(x)``
     which calculate the exponential function `e^{x}`.

     The exponential function can be represented as the following infinite sum:

     .. math::
    
        e^{x} = 1 + \frac{x^{1}}{1!} + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \frac{x^{4}}{4!} + \ldots
     
     Choose an amount of terms to calcule the ``exponential function``.
     Compare your results with the ``exp`` function from the ``math`` module.
