Lecture 14 - Modules creation
-----------------------------
.. index:: module (creation)

A simple module is simply a file with Python code.
The name of the file indicates which is the module's name.

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
in the same folder as the program.

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
If it is a module, it contains definitions that can be imported from a program or other module.
If it is a program, it contains code to be executed.

Sometimes, a program also contains definitions
(for example, functions and variables)
which also may be useful for another program.
However, they cannot be imported,
because, by using the ``import`` statement
the full program would be executed.
What would happen in this case, is that
if you run the second program, then the first
program will be executed first.

There is a trick to avoid this problem:
Whenever there is code being executed,
a variable called ``__name__`` exists.
When the program is executed
the value of this variable is ``__main__``,
but when the module is imported this value
takes the module's name.

Therefore, 
you can use the value of this variable to mark
the part of the program to be executed when the
file is run, but not when it is imported.

For example,
the following program converts 
measurement units of length:

.. literalinclude:: ../../_static/programs/unit_conversion.py

This program is useful by itself,
but also its four functions and 
the constants ``km_per_mile`` and ``cm_per_inch``
might be useful for use in another program.

If the body of the program is put inside 
the ``if __name__ == '__main__'`` statement,
the file can be used like a module.
If we do not do this,
whenever the other program imports a function
the whole program would be executed.

Try it: `download the program`_ and run it.
Then, write another program to import some of the functions.
Next, do the same,
but removing the ``if`` statement.


.. _download the program: ../../_static/programs/unit_conversion.py

Exercises
~~~~~~~~~

#. Write a module called ``lists.py``
   which contains the following functions.
   
   * A function called ``average(l)``,
     where the parameter ``l`` is a list of real numbers
     and its return value is the average of these numbers::
   
       >>> average([7.0, 3.1, 1.7])
       3.933333333333333
       >>> average([1, 4, 9, 16])
       7.5
   
   * A function called ``squares(l)``,
     which returns a list with the squares of the values
     in the list ``l``::
   
       >>> squares([1, 2, 3, 4, 5])
       [1, 4, 9, 16, 25]
       >>> squares([3.4, 1.2])
       [11.559999999999999, 1.44]
   
   * A function called ``longest(words)``,
     where the ``words`` parameter is a list of strings
     and its return value is the longest string in the list::
   
       >>> longest(['mouse', 'hippo', 'dog', 'giraffe'])
       'giraffe'
       >>> longest(['****', '**', '********', '**'])
       '********'
   
     If there is a tie in length among the longest two or more words, it is
     necessary to return only one of them.

#. Write a module called ``my_math.py``
   which contains the following functions.

   * A function called ``my_sin(x)``
     which calculates the sine of the ``x`` value.

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
     which calculates the exponential function `e^{x}`.

     The exponential function can be represented as the following infinite sum:

     .. math::
    
        e^{x} = 1 + \frac{x^{1}}{1!} + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \frac{x^{4}}{4!} + \ldots
     
     Choose an amount of terms to calculate the ``exponential function``.
     Compare your results with the ``exp`` function from the ``math`` module.
