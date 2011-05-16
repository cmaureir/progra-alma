Lecture 16 - Errors and exceptions
-----------------------------------

.. index:: error

The programs we write aren't always correct.
There are many types of errors that may be present in a program.

Not all the errors can be detected by the computer.
For example,
the following program have one quite evident logic error::

    n = int(raw_input('Enter a number: '))
    double = 3 * n
    print 'The n double is', double

The computer will not notice the error,
because all the program's instructions are correct.
The program simply will always give the wrong answer.

There are other errors that can be detected.
When an error is detected *during* the program's execution
an **exception** occurs. 

The interpreter announced an exception
stopping the program and displaying a message describing the error.
For example,
we can create the following program
and calling it ``division.py``::

    n = 8
    m = 0
    print n / m
    print 'Ok'

When executed,
the interpreter throws an exception,
because the division by zero is an
invalid operation::

    Traceback (most recent call last):
      File "division.py", line 3, in <module>
        print n / m
    ZeroDivisionError: division by zero

The second line of the message
indicates the file name where the error is located
and the the line where this happened.
In this example,
the error is in the line 3 of ``division.py``.
The last line shows the name of the exception
(in this case ``ZeroDivisionError``)
and a message explaining what is wrong.

Errors and exceptions presented here 
are the most basics and common.

Syntax Error
~~~~~~~~~~~~
.. index:: syntax error

A **syntax error** occurs when the program does not follow
the rules of language.
When this error occurs,
it means that the program is not written correctly.
The name of the error is ``SyntaxError``.

The syntax errors always happen *before*
the program is run.
It means, a badly written program cannot execute any instruction.
Therefore, the syntax error is not an exception.

Here are a few examples of syntax errors.::

    >>> 2 * (3 + 4))               
      File "<stdin>", line 1
        2 * (3 + 4))
                   ^
    SyntaxError: invalid syntax

::

    >>> n + 2 = 7
      File "<stdin>", line 1
    SyntaxError: can't assign to operator

Name Error
~~~~~~~~~~
.. index:: name error


A **name error**
occurs when using a variable that has not been created before.

The name of the exception is ``NameError``::
    
    >>> x = 20
    >>> 5 * x
    100
    >>> 5 * y
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'y' is not defined

To resolve this error,
you must assign a value to the variable 
before using it.

Type Error
~~~~~~~~~~
.. index:: type error

In general,
all the operations in a program
can be applied on very specific type values.
A **type error** occurs when applying an operation
on operands of the wrong type.

The name of the exception is ``TypeError``.

For example,
cannot multiply two strings::

    >>> 'six' * 'eight'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can't multiply sequence by non-int of type 'str'

Neither can obtain the length of a number::

    >>> len(68)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()

When the type error occurs, it is
usually because the program is not properly designed.
It must be checked, ideally routing the program
to understand the error
and, finally fix it.

Value Error
~~~~~~~~~~~
.. index:: value error


The **value error**
occurs when the operands are of the correct type,
but the operation does not make sense for that value.

The name of the exception is ``ValueError``.

For example,
the ``int`` function can convert a string to an integer,
but the string should be the representation of an integer number.
Any other value throws a Value Error::

    >>> int('41')
    41
    >>> int('dog')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'dog'
    >>> int('forty one')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'forty one'

To fix this error,
you have to make sure to always use appropriate values.
    
Zero Division Error
~~~~~~~~~~~~~~~~~~~
.. index:: zero division error

The **zero division error** occurs when trying to divide by zero.

The name of the exception is ``ZeroDivsionError``::

    >>> 1/0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDvisionError: integer division or modulo by zero

Overflow Error
~~~~~~~~~~~~~~
.. index:: overflow error

The **overflow error**
occurs when the operation result is so big 
that the computer cannot represent it internally.

The name of the exception is ``OverflowError``::

    >>> 20.0 ** 20.0 ** 20.0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OverflowError: (34, 'Numerical result out of range')

For those interested in learning  more about exceptions,
you can review the `section about exceptions`_
in the official documentation Python.

.. _section about exceptions: http://docs.python.org/library/exceptions.html

Exception handling
~~~~~~~~~~~~~~~~~~

When you are creating a program,
maybe you need to take some action when
an exceptions occurs, to avoid restarting the program,
or loose some changes, etc.

Python provides an easy way to handle
the exceptions, using the statements ``try`` and ``except``.

For example, one of the previous examples::

    >>> int('dog')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'dog'

Can be written in this way::


    >>> try:
    ...    var = int("dog")
    ... except ValueError as error:
    ...    print "ValueError has occurred: ", error 
    ... 
    ValueError has occurred: invalid literal for int() with base 10: 'dog'


You can mix the ``try`` and ``except`` with the ``else`` statement, for example::

    >>> def invert(x):
    ...    try:
    ...       i = 1.0 / x
    ...    except:
    ...       print 'caught exception for' , x
    ...    else:
    ...       print 'reciprocal of' , x, 'is' , i
    ...
    >>> invert(1)
    reciprocal of 1 is 1.0
    >>> invert(0)
    caught exception for 0


So, the ``else`` block is executed
only if in the content of the ``try`` block,
everything is correct, error free.

You can use multiple instances of the ``except``
because inside the ``try`` block
more than one Error can occur::

    >>> values = [-1, 0, 1]
    >>> for i in range(4):
    ...  try:
    ...     r = 1.0 / values[i]
    ...     print 'reciprocal of' , values[i], 'at' , i, 'is' , r
    ...  except IndexError:
    ...     print 'index' , i, 'out of range'
    ...  except ArithmeticError:
    ...    print 'unable to calculate reciprocal of' , values[i]
    reciprocal of -1 at 0 is -1.0
    unable to calculate reciprocal of 0
    reciprocal of 1 at 2 is 1.0
    index 3 out of range

The ``raise`` statement
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to explicitly trigger an exception,
the solution is use the ``raise`` statement.

There are two basic ways to call this statement:

::

   raise <name>
   raise <name>, <data>

The first one manually trigger an exception called ``<name>``
and the second one manually trigger an exception called ``<name>``
but also, return some extra data.

::

    >>> raise TypeError
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError
    >>> raise TypeError, 'testing extra data'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: testing extra data

This is very useful, when you want to create your own exceptions
and errors, based in some new criteria.

Exercises
~~~~~~~~~

 * Write a program which check a date input by the user.
   The date must have the format YYYY-MM-DD.
   Consider a normal years, in other words, February has
   only 28 days.

   .. testcase::
      Input date: `2010-15-10`
      Incorrect month!
      Input date: `2010-12-10`
      Your date is correct!

   .. testcase::
      Input date: `2010-05-40`
      Incorrect day!
      Input date: `2010-05-hello`
      Incorrect day!
      Input date: `2010-05-01`
      Your date is correct!



 * Write a program which calculates the age of a people,
   the user must input the day, month and year of birth.

   The program can not finish without a correct answer,
   it means, you must verify if the input data is correct,
   in terms of numerical bounds. (Remember the exceptions!)

   Use the previous program implemented to do this solution.

   
   .. testcase::

      Enter year of birth: `1988`
      Enter month of birth: `10`
      Enter day of birth: `19`
      You are 22 years old.
  
   .. testcase::

      Enter year of birth: `1992`
      Enter month of birth: `15`
      Not a valid month!
      Enter month of birth: `2`
      Enter day of birth: `hello`
      Not a valid day!
      Enter day of birth: `ok`
      Not a valid day!
      Enter day of birth: `1`
      You are 19 years old.


 * Write a function which calculates the average of a set of number
   in a list, the main function must use another two functions wrote
   by you, to perform the addition of all the elements called ``sum`` 
   and another to divide the addition total by the number of elements
   called ``avg``. 
   The program must detect some input list errors.
   (Remember the exceptions!)
		
   ::
 
      >>> average([1,2,3])
      The average is: 2
      >>> average([1,2,'three'])
      Incorrect element type! (TypeError)
      >>> average([])
      Empty list! (ZeroDivisionError)

 * Write a function which allows to the user a `safe` way to open
   files in the system, it means, if the file does not exist,
   raise an exception, otherwise the reading can be done properly.

   If the ``test.txt`` file exist:

   ::

      >>> myfile = open_file('test.txt','r')
      File exist!

   If the ``test.txt`` file does not exist:

   ::

      >>> myfile = open_file('test.txt','r')
      Warning, file does not exist!

   Look in the `Python documentation`_, the Error
   for this cases, and use it.

   .. _`Python documentation`: http://www.python.org/doc/essays/stdexceptions/

.. import sys
..     
..     try:
..         f = open('myfile.txt')
..         s = f.readline()
..         i = int(s.strip())
..     except IOError, (errno, strerror):
..         print "I/O error(%s): %s" % (errno, strerror)
..     except ValueError:
..         print "Could not convert data to an integer."
..     except:
..         print "Unexpected error:", sys.exc_info()[0]
..         raise 

.. for arg in sys.argv[1:]:
..         try:
..             f = open(arg, 'r')
..         except IOError:
..             print 'cannot open', arg
..         else:
..             print arg, 'has', len(f.readlines()), 'lines'
..             f.close()



..   >>> def this_fails():
..     ...     x = 1/0
..     ... 
..     >>> try:
..     ...     this_fails()
..     ... except ZeroDivisionError, detail:
..     ...     print 'Handling run-time error:', detail
..     ... 
..     Handling run-time error: integer division or
..      modulo by zero


.. def sum( someList ):
..     """Raises TypeError"""
..     sum= 0
..     for v in someList:
..         sum = sum + v
..     return sum
.. def avg( someList ):
..     """Raises TypeError or ZeroDivisionError exceptions."""
..     try:
..         s= sum(someList)
..         return float(s)/len(someList)
..     except TypeError, ex:
..         return "Non-Numeric Data"
.. def avgReport( someList ):
..     try:
..         m= avg(someList)
..         print "Average+15%=", m*1.15
..     except TypeError, ex:
..         print "TypeError: ", ex
..     except ZeroDivisionError, ex:
..         print "ZeroDivisionError: ", ex
