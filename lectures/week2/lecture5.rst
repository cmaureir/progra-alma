Lecture 5 - Input and output
-----------------------------

(`Python input and output official documentation`_)

.. _Python input and output official documentation: http://docs.python.org/tutorial/inputoutput.html

Input
~~~~~

.. index:: input (program)

The **input** is the program part
in which the user enters data.

.. index:: raw_input

The simplest way to enter data
is doing it through the keyboard.
The ``raw_input(message)`` function
asks the user to enter a value
that can be assigned to a variable
to be used by the program.
The ``message`` is to be displayed to the user
before that he enters a value.

The input value provided by the user
is always interpreted as text
as a value of type ``str``.
If a different type is required,
we need to convert it explicitly.

For example,
in the temperature conversion program,
the input is converted to a real value
by the following statement::

    f = float(raw_input('Enter temperature in Fahrenheit degrees: '))

When the program gets to this line,
the message ``Enter temperature in Fahrenheit degrees:``
is shown to the user, who then must enter a value,
which is converted into a real number
and bound to the name ``f``.

From that line onward,
variable ``f`` can be used by the program
to refer to the entered value.

.. La función ``input()``,
.. que usamos para leer la entrada del usuario,
.. siempre entrega como resultado un string.
.. Hay que tener la precaución
.. de convertir los valores que entrega
.. al tipo adecuado.
.. Por ejemplo,
.. el siguiente programa tiene
.. un error de incompatibilidad de tipos::
.. 
..     n = input('Escriba un número:')
..     cuadrado = n * n
..     print('El cuadrado de n es', cuadrado)



Output
~~~~~~

.. index:: output (program)

The **output** is the program part
in which the results are delivered to the user.

.. index:: print

The simplest way to deliver the output
is to display text on the screen.
In Python, the program output is performed by the
**print** sentence.

If one wants to display a single value,
the syntax is as follows::

    print value_to_print

If there are several values to be printed,
they should be separated by commas.
For example, the temperature conversion program
has the following output statement::

    print 'The Celsius degrees equivalent is:', c

In this case, the message ``The Celsius degrees equivalent is:``
is being printed and, after it, in the same line,
the value of the variable ``c``.

The quotation marks allow to represent a string but are not part of it.
When printing the string by using ``print``, the quotation marks do not appear::

    >>> 'Hello'
    'Hello'
    >>> print 'Hello'
    Hello

Comments
~~~~~~~~

.. index:: comments, #

A **comment** is a section of code
that is ignored by the interpreter.
A comment can be used by the programmer
to place messages in the code that can be useful
to someone that needs to read the code
in the future.

In Python,
any text that appears to the right of a ``#`` sign
is a comment::

    >>> 2 + 3  # This is a sum
    5
    >>> # This is ignored
    >>>

The only exception are the ``#`` signs that appear in a string::

    >>> "123 # 456" # 789
    '123 # 456'

Exercises
~~~~~~~~~

PENDING
