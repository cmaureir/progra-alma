Lecture 16 - Errors and exceptions
-----------------------------------

.. index:: error

Not always the programs that we write are correct.
There are many types of errors that may be present in a program.

Not all the errors can be detected by the computer.
For example,
the following program have one logic error quite evident::

    n = int(raw_input('Enter a number: '))
    double = 3 * n
    print 'The n double is', double

The computer will not notice the error,
because all the program's instructions are correct.
The program simply will give always the wrong answer.

There are other errors that can be detected.
When an error is detected *during* the program execution
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
indicates the file name where is located the error
and the number of the line.
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

A **syntax error** occurs when the program does not follows
the rules of language.
When this error occur,
it means that the program isn't written correctly.
The name of the error is ``SyntaxError``.

The syntax errors always happen *before*
the program run.
It means, a badly written program can not execute any instruction.
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

::

    >>> True = 1000
      File "<stdin>", line 1
    SyntaxError: assignment to keyword

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
can not multiply two strings::

    >>> 'six' * 'eight'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can't multiply sequence by non-int of type 'str'

Neither can obtained the length of a number::

    >>> len(68)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()

When occurs in type error,
usually the program is not properly designed.
Must be checked, ideally making routing 
to understand the error,
and finally fix it.

Value Error
~~~~~~~~~~~
.. index:: value error


The **value error**
occurs when the operands are of correct type,
but the operation does not make sense for that value.

The name of the exception is ``ValueError``.

For example,
the ``int`` function can convert a string to an integer,
but the string should be the representation of a integer number.
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
you have to worry about always using appropriate values.
    
Zero Division Error
~~~~~~~~~~~~~~~~~~~
.. index:: error de división por cero

The **zero division error** occurs when try to divide by zero.

The name of the exception is ``ZeroDivsionError``::

    >>> 1/0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

Overflow Error
~~~~~~~~~~~~~~
.. index:: error de desborde

The **overflow error**
occurs when the operation result is so big 
that the computer can not represent internally.

The name of the exception is ``OverflowError``::

    >>> 20.0 ** 20.0 ** 20.0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OverflowError: (34, 'Numerical result out of range')

For those interested in learning  more about exceptions,
can review the `section about exceptions`_
in the official documentation Python.

.. _section about exceptions: http://docs.python.org/library/exceptions.html

Exception handling
~~~~~~~~~~~~~~~~~~

When you are creating a program,
maybe you need to take some option when
an exceptions occurs, to avoid restart the program,
or lost some changes, etc.

Python provides a easy way to handle
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
because maybe inside the ``try`` block can occurs
more than one Error::

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
