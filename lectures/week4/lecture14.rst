Lecture 14 - Modules creation
-----------------------------
.. index:: module (creation)

A simple module is simply a file with Python code.
The name of the file indicates which is the module name.

For example, we can create a file named ``parity.py``
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
However, can not be imported,
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


