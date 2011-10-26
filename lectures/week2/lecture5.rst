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
before he enters a value.

The input value provided by the user
is always interpreted as text,
so its type is ``str``.
If a different type is required,
we need to convert it explicitly.

For example,
in the `temperature conversion program`_,
the input is converted to a real value
by the following statement::

    f = float(raw_input('Enter temperature in Fahrenheit degrees: '))

When the program gets to this line,
the message ``Enter temperature in Fahrenheit degrees:``
is shown to the user, who must enter a value,
which is converted into a real number
and bound to the name ``f``.

.. _`temperature conversion program`: ../../_static/programs/temperature.py 

From that line onward,
variable ``f`` can be used by the program
to refer to the entered value.

The ``raw_input()`` function, that we use 
to read the input of the user,
always return a string as result.
Be careful with the type of the return
values, because you need to convert them
to the properly type.

For example,
the next program has a type incompatibility error::

    n = raw_input('Write a number:')
    square = n * n
    print('The square of n is ', square)

Output
~~~~~~

.. index:: output (program)

The **output** is the program part
in which the results are delivered to the user.

.. index:: print

The simplest way to deliver the output
is to display text on the screen.
In Python, the program output is performed by the
**print** statement.

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
for someone that needs to read the code
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


Precedence
~~~~~~~~~~
.. index:: operator precedence, brackets

The **operator precedences**
is a set of rules that specified
the order to evaluate some
operations in an expression.

The precedence is given by the next list,
in which the operators was listed in order
of precedence:

* ``or``
* ``and``
* ``not``
* ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``
* ``+``, ``-`` (sum and subtraction)
* ``*``, ``/``, ``%``
* ``+``, ``-`` (positive and negative)
* ``**``

This means, for example,
that the multiplications are evaluated before the additions,
and the comparisons are evaluated before the logic operations::

    >>> 2 + 3 * 4
    14
    >>> 1 < 2 and 3 < 4
    True

Operations inside the same level
are evaluated in the order from left to right::

    >>> 15 * 12 % 7    # is the same to (15 * 12) % 7
    5

The only exception to the previous rule are the powers,
which are evaluated from right to left::

    >>> 2 ** 3 ** 2    # is the same to 2 ** (3 ** 2)
    512

To force a different evaluation order in comparison to the previous rules,
you must use brackets::

    >>> (2 + 3) * 4
    20
    >>> 15 * (12 % 7)
    75
    >>> (2 ** 3) ** 2
    64

Another way to force the order
is saving the intermediate results in variables::

    >>> n = 12 % 7
    >>> 15 * n
    75

As an example, consider the next expression::

    15 + 59 * 75 / 9 < 2 ** 3 ** 2 and (15 + 59) * 75 % n == 1

and we will suppose that the ``n`` variable has the value 2.
Here we can see how the expression is evaluated until
arrive in the final result, that is ``False``::

    15 + 59 * 75 / 9 < 2 ** 3 ** 2 and (15 + 59) * 75 % n == 1
    #                         ↓
    15 + 59 * 75 / 9 < 2 **   9    and (15 + 59) * 75 % n == 1
    #                    ↓
    15 + 59 * 75 / 9 < 512         and (15 + 59) * 75 % n == 1
    #       ↓
    15 +  4425   / 9 < 512         and (15 + 59) * 75 % n == 1
    #            ↓
    15 +        491  < 512         and (15 + 59) * 75 % n == 1
    #                                      ↓
    15 +        491  < 512         and    74     * 75 % n == 1
    #                                            ↓
    15 +        491  < 512         and          5550  % n == 1
    #                                                   ↓
    15 +        491  < 512         and          5550  % 2 == 1
    #                                                 ↓
    15 +        491  < 512         and                0   == 1
    #  ↓
      506            < 512         and                0   == 1
    #                ↓
                    True           and                0   == 1
    #                                                     ↓
                    True           and                  False
    #                               ↓
                                  False

The operations between brackets ``(15 + 59)``
must be evaluated before the multiplication by 75,
because is necessary to know their result to be able to calculate the product.
The precise moment in which that occurs is not important.

The same thing occurs with the evaluation of the variable ``n``:
the only important thing is that it is evaluated before being used by the
modulus operator.

In the example,
both cases were evaluated immediately before their value was required.

The entire precedence rules,
including another operator that we have not seen,
can be checked in the `expressions section`_
of the official Python documentation.

.. _expressions section: http://docs.python.org/reference/expressions.html#summary

How to learn the precedence rules ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The answer is: better not to learn them.
The rules of precedence are many and not always intuitive.

A program is easier to understand if you explicitly
indicate the evaluation order using brackets or saving in variables
the intermediate results of the calculation.

A good programmer always worry about their code being easy to understand
by others and ¡even for himself in a few weeks!

Function calls
~~~~~~~~~~~~~~
.. index:: function

(`Python built-in function official documentation`_)

.. _Python built-in function official documentation: http://docs.python.org/library/functions.html


Complementary to the previous lectures, we will take a look
at some useful functions.

The operators form a very reduced set of operations.
More commonly, the more general operations are represented
as **functions**.

.. index:: parameter, argument, function call

As in math, a function has a name,
and receive **parameters** (or **arguments**)
which are between brackets after the name.
The operation to use a function to obtain a result
is called a **function call**.

We already know the ``raw_input()`` function,
that returns as result
the text entered by the user through the keyboard.

.. index:: abs

The ``abs`` function returns the absolute value of their argument::

    >>> abs(4 - 5)
    1
    >>> abs(5 - 4)
    1

.. index:: len (of a string)

The ``len`` function receives a string and returns its length.
(you might remember from the past week lecture)::

    >>> len('hello world')
    11
    >>> len('hello' * 10)
    50

.. index:: int (function), float (function), str (function)

The names of the types are also functions,
which return the equivalent of its parameter in the corresponding type::

    >>> int(3.8)
    3
    >>> float('1.5')
    1.5
    >>> str(5 + 6)
    '11'
    >>> int('5' + '6')
    56

.. index:: min, max

The ``min`` and ``max`` functions
return the minimum or the maximum value among its arguments::

    >>> min(6, 1, 8)
    1
    >>> min(6.0, 1.0, 8.0)
    1.0
    >>> max(6, 1, 4, 8)
    8

.. index:: round

The ``round`` function rounds a real number to the closest integer::

    >>> round(4.4)
    4.0
    >>> round(4.6)
    5.0

.. index:: exp, sin, log, 

Some mathematical functions,
like the exponential, the logarithm
and the trigonometric can be used,
but first must be imported
using the ``import`` statement,
which we will look deeply in the next lectures::

    >>> from math import exp
    >>> exp(2)
    7.3890560989306504
    >>> from math import sin, cos
    >>> cos(3.14)
    -0.9999987317275395
    >>> sin(3.14)
    0.0015926529164868282

The entire mathematical function list
that can be imported is available at the `math module description`_
in the official Python documentation.

.. _math module description: http://docs.python.org/library/math.html

Later, we will also learn to create
our own functions.
But now, we only need to know how to call one.

Of course, it is
always necessary to provide arguments of appropriate type to the function call::

    >>> round('dog')
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: a float is required
    >>> len(8)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: object of type 'int' has no len()

Exercises
~~~~~~~~~

1. Write a program that receives two words, and indicates the extra
   characters of the second word in comparison the first word.

   .. testcase::

       Word 1: `building`
       Word 2: `train`
       The train word has -3 more characters than train.

   .. testcase::
   
       Word 1: `sun`
       Word 2: `parallelepiped`
       The parallelepiped word has 11 more characters than sun.

2. Write a program that receives a real number and calculates the ``sine`` and
   the ``cosine``.

   .. testcase::
       Number: `30`
       sin(30) = -0.9880316240928618
       cos(30) = 0.15425144988758405

   .. testcase::
       Number: `1.5`
       sin(1.5) = 0.9974949866040544
       cos(1.5) = 0.0707372016677029

3. Write a program that receives two numbers,
   with the greatest number, you must determinate the `e^{max\_number}`
   and with the lowest, you must determinate the `\sqrt{min\_number}`.

   .. testcase::
       Number 1: 5
       Number 2: 7
       e^7 : 1096.6331584284585
       sqrt(5) : 2.23606797749979

   .. testcase::
       Number 1: 11
       Number 2: 22
       e^22 : 3584912846.1315875
       sqrt(11) : 3.3166247903554

4. Given n-bodies with an initial position `x_i` and a velocity `v_i`, `1<=i<=N`,
   the force vector `f_{ij}` over the i-body by the gravitational attraction
   to the j-body, will be:

   .. math::
       f_{ij} = G\cdot \frac{m_i \cdot m_j}{\parallel r_{ij}\parallel^{2}} \cdot \frac{r_{ij}}{||r_{ij}||}

   with:

   * `m_i`: mass of the i-body
   * `m_j`: mass of the j-body
   * `r_{ij} = (xj-xi)`, vector between the `i` and `j` bodies.
   * `G`: gravitational constant (`6.67428*10-11 m^{3}\cdot kg^{-1}\cdot s^{-2}`)

   Write a program that receives the previous values (`x_i`, `v_i`, `m_i`) of two bodies,
   consider only a 1-dimension space and only two bodies.

   .. testcase::
      x_1 : 3
      v_1 : 2
      x_2 : -5
      v_2 : -2
      m_1 : 10
      m_2 : 8
      f_12 : -8.342850e-11
