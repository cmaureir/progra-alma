Lecture 2
=========

Program development
-------------------

A **program** is a text file that contains
code to be executed by the computer.

In the case of the Python programming language, 
the program is executed by an **interpreter**.
The interpreter is a program which execute programs.

The programs written in Python
must be contained in a file
with the ``.py`` extension.
In Windows, the program can be executed doing a double
click above the file icon.

To test this,
download the quadratic.py_ file
which allows to solve quadratic equations.

.. _quadratic.py: ../_static/programs/quadratic.py

Editing programs
~~~~~~~~~~~~~~~~
.. index:: text editor

A program is a `text file`_.
Therefore, it can be created or edited
using any `text editor`_,
like Notepad.

What can not be used
is a text processor,
like Microsoft Word.

Do the test:
open the ``quadratic.py`` program
with Notepad (or another editor)
and you will see the content.

.. _text file: http://en.wikipedia.org/wiki/Text_file
.. _text editor: http://en.wikipedia.org/wiki/Text_editor

.. index:: text editor (list)

Other text editors
(much better than Notepad)
that you can install are:

* in Windows:
  `Notepad++ <http://notepad-plus-plus.org/>`_,
  `Textpad <http://www.textpad.com/>`_;
* in Mac:
  `TextWrangler <http://www.barebones.com/products/textwrangler/>`_,
  `TextMate <http://macromates.com/>`_;
* in Linux:
  `Gedit <http://projects.gnome.org/gedit/>`_,
  `Kate <http://kate-editor.org/>`_.


Python interpreter installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. index:: interpreter (installation)

One thing is to edit the program and, another one, is to execute it.
The **interpreter** must be installed to
be able to execute the program using Python.

You can find the installer list
in the `Python download web`_
You must download the one indicated for your computer
and operating system.

.. _Python download web: http://www.python.org/download/
..

You must install the version **2.7.1**
and not 3.1.3.

Do not use the ``x86-64`` installers
unless you are sure that your computer
has a 64 bits architecture.

Program execution
~~~~~~~~~~~~~~~~~

Once the program is written and the interpreter has been installed,
it is possible to execute the programs.
The next video shows the process:

    [Video]

Console use
~~~~~~~~~~~
.. index:: interpreter (interactive), console

Executing the programs
is not the only way to use the interpreter.
If we execute Python without passing any program,
the **console** (or **interactive interpreter**) will open.

The console allows to enter a program through the command line.
It also allows to evaluate expressions and see the results immediately.
This allows, for example, using it like a calculator.

The next video shows how to use the interactive interpreter:

    [Video]

The interactive console
always shows the ``>>>`` symbol,
to indicate the possibility to enter code.
In all the books about Python
and in all these lectures,
each time an example appears using this symbol
means that it must be executed in a console
and not in a program. For example::

    >>> a = 5
    >>> a > 10
    False
    >>> a ** 2
    25

In this example, at the time the expressions are entered ``a > 10`` and ``a ** 2``,
the interactive interpreter give the results ``False`` and ``25``.

There is no reason to write the ``>>>`` symbol
in a program, because it is not part of the language syntax.


Development environment
~~~~~~~~~~~~~~~~~~~~~~~
.. index:: development environment, IDE

In general,
using a simple text editor to write programs is not
the most efficient way to work.

The  **development environments**
(also called *IDE*)
are applications that facilitate the task of writing programs.

Python comes with its own development environment, called **IDLE**.
The following video shows how to use IDLE to develop a program
and to use the interactive console:

    [Video]

Other good advanced Python development environments are:

* `PyScripter <http://code.google.com/p/pyscripter/downloads/list>`_,
* `WingIDE 101 <http://www.wingware.com/downloads/wingide-101/3.2.12-1/binaries>`_

You can test them and use the most comfortable for you.

Control statements
------------------

A program is a sequence of **statements**
being executed in order.

For example, the following program has four statements::

    n = int(raw_input('Enter n: '))
    m = int(raw_input('Enter m: '))
    sum = n + m
    print 'The sum of n and m is:', sum

The first three lines are assignments
and the last one is a function call.
Running the program,
each of these statements are executed once,
one after another.

.. index:: control statement

Besides simple statements,
which are sequentially executed,
there are **control statements**
that allow modifying the program flow,
introducing loops and conditionals.

.. index:: conditional

A **conditional** is a statement set
which can or can not be executed,
depending on the result of a condition.

.. index:: loop

A **loop** is a statement set
which is executed several times,
until one of the end condition are satisfied.

.. index:: indentation

The conditionals and the loops
contain other statements.
To indicate this relation
python uses the **indentation**:
the contained statements
are not written in the same column
as the control statement,
but more to the right::

    n = int(raw_input())
    m = int(raw_input())
    if m < n:
        t = m
        m = n
        n = t
    print m, n

In this example, the three assignations are
contained inside the ``if`` control statement.
The ``print m, n`` is not indented,
so it is not part of the ``if`` statement.

This program has four statements,
of which the third one is a control statement,
that contains the other three statements.

To indent,
we will always use four spaces.

``if`` conditional
~~~~~~~~~~~~~~~~~~~
.. index:: if

The **if** statement
executes the instructions
only if a condition is satisfied.
If the condition is false,
it does nothing:

.. image:: ../diagrams/if.png
   :alt: (if flow diagram)

The syntax is as follows::

    if condition:
        statements

For example,
the following program congratulates someone
that approved the course::

    grade = int(raw_input('Enter your grade: '))
    if grade >= 55:
        print 'Congratulations!'

Execute this program,
testing it several times with different values.

``if-else`` conditional
~~~~~~~~~~~+~~~~~~~~~~~
.. index:: if-else

The **if-else** statement
decide what instructions are executed
depending on whether a condition is true or false:

.. image:: ../diagrams/if-else.png
   :alt: (if-else flow diagram)

The syntax is as follows::

    if condition:
        what to do when the condition is true
    else
        what to do when the condition is false

For example,
the following program indicates if someone is an adult (in Chile)::

    age = int(raw_input('How old are you? '))
    if age < 18:
        print 'You are a minor'
    else:
        print 'You are an adult'

The next program do different actions
depending if the input number is even or odd::

    n = int(raw_input('Enter a number: '))
    if n % 2 == 0:
        print 'The number is even'
        print 'The halfnumber is', n / 2
    else:
        print 'The number is odd'
        print 'The next number is', n + 1
    print 'Ready'

The last statement is not indented,
so it is not part of the conditional
and will always be executed.

``if-else-elif`` conditional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. index:: if-elif-else

The **if-elif-else** statement
depends on two or more conditions,
which are evaluated in order.
The first one to be true
determines what instructions will be executed:

.. image:: ../diagrams/if-elif-else.png
   :alt: (if-elif-else flow diagram)

The syntax is as follow::

    if condition1:
        what to do if condition1 is true
    elif condition2:
        what to do if condition2 is true
    ...
    else:
        what to do if none of the above conditions is true

The last ``else`` is optional.

For example,
the rate of tax payable by a person according to his salary
can be given by the next table:

====================== ====================
**salary**             **tax rate**
---------------------- --------------------
less than 1000                           0%
1000 ≤ salary < 2000                     5%
2000 ≤ salary < 4000                    10%
4000 or higher                          12%
====================== ====================

So, a program that computes the tax to pay
could be as follow::

    salary = int(raw_input('Enter salary: '))
    if salary < 1000:
        rate = 0.00
    elif salary < 2000:
        rate = 0.05
    elif salary < 4000:
        rate = 0.10
    else:
        rate = 0.12
    print 'You must pay', rate * salary, 'of taxes'

Only one of the alternatives will be executed.
If one of the conditions, evaluated in order, is true,
the below conditions are not evaluated.

Another way to write the same program
using only the ``if`` sentence is as follow::


    salary = int(raw_input('Enter salary: '))
    if salary < 1000:
        rate = 0.00
    if 1000 <= salary < 2000:
        rate = 0.05
    if 2000 <= salary < 4000:
        rate = 0.10
    if 4000 < salary:
        rate = 0.12
    print 'You must pay', rate * salary, 'of taxes'

This way is less clear,
because it is not obvious at first look that
only one of the conditions will be true and all 
the conditions are evaluated.

Loops
-----

``while`` loop
~~~~~~~~~~~~~~

.. index:: while

The **while** loop
executes an instruction sequence
while a condition is true:

.. image:: ../diagrams/while.png
   :alt: (while flow diagram)

.. index:: iteration

An **iteration** is defined as each time the content
of a loop is executed.

The condition is evaluated before each iteration.
If the condition is initially false,
the loop will not run even once.

The syntax is as follows::

    while condition:
        statements

For example,
the next program
multiplies two integer numbers
without using the ``*`` operator::

    m = int(raw_input())
    n = int(raw_input())
    p = 0
    while m > 0:
        m = m - 1
        p = p + n
    print 'The product between m and n is', p

To see the functionality of this program,
lets do a routing with ``m`` = 4 and ``n`` = 7
as input values:

   +-------+-------+-------+
   | ``p`` | ``m`` | ``n`` |
   +=======+=======+=======+
   |       |     4 |       |
   +-------+-------+-------+
   |       |       |     7 |
   +-------+-------+-------+
   |     0 |       |       |
   +-------+-------+-------+
   |       |     3 |       |
   +-------+-------+-------+
   |     7 |       |       |
   +-------+-------+-------+
   |       |     2 |       |
   +-------+-------+-------+
   |    14 |       |       |
   +-------+-------+-------+
   |       |     1 |       |
   +-------+-------+-------+
   |    21 |       |       |
   +-------+-------+-------+
   |       |     0 |       |
   +-------+-------+-------+
   |    28 |       |       |
   +-------+-------+-------+

On each iteration
the ``m`` value decrease once.
When the value reaches zero,
the ``while`` condition ceases being true
so the loop ends.
Thus, a result composed by the sum of 
``m`` times the ``n`` value is achieved.

Note that the loop does not finish exactly when ``m`` reaches zero.
The condition is evaluated once the entire iteration is finish.

In general,
the ``while`` loop is used when it is not possible to know in advance
how many times the loop will executed,
but the condition for the loop to finish.


``for`` loop with counter
~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: for, control variable

The **for loop with range**
executes a sequence of sentences
a fixed number of times.

To keep the count,
use a **loop variable**
that takes a different value on each iteration.

One of the syntaxes to use a ``for``
loop with range is the following::

    for variable in range(fin):
        what to do to each value of the control variable

In the first iteration,
the control variable takes the 0 value.
At the end of each iteration,
the variable value increases automatically.
The loop ends just before the variable takes the
``end`` value.

For example,
the next program shows the cube of the numbers
from 0 to 20::

    for i in range(21):
        print i, i ** 3

.. index:: range

A **range** is a equispaced integer number sequence.
Including the presented previously,
there are three ways to define a range::

    range(final)
    range(initial, final)
    range(initial, final, increase)

The initial value is always part of the range.
The final value is never part of the range.
The increase shows the difference between two consecutive values in the range.

If the initial value is omitted, it supposed to be 0.
If the increment is omitted, it supposed to be 1.

This will be clearer With some examples:

==================== ===================================
``range(9)``         0, 1, 2, 3, 4, 5, 6, 7, 8
``range(3, 13)``     3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
``range(3, 13, 2)``  3, 5, 7, 9, 11
``range(11, 4)``     no valor
``range(11, 4, -1)`` 11, 10, 9, 8, 7, 6, 5
==================== ===================================

It is possible to do backwards looping using a negative increment::

    for i in range(10, 0, -1):
        print i
    print 'Happy new year!'

In general,
the ``for`` loop with range
is used when the iteration number is known
before entering the loop.

Functions
---------
.. index:: function

Suppose we need to write a program which calculates the
`combinatorial number`_ `C(m, n)`,
defined by:

.. math::

    C(m, n) = \frac{m!}{(m - n)! n!},

where `n!` (the `n` factorial_)
is the product of the integer numbers from 1 to `n`:

.. math::

    n! = 1\cdot 2\cdot\cdots\cdot(n - 1)\cdot n = \prod_{i=1}^n i

.. _combinatorial number: http://en.wikipedia.org/wiki/Binomial_coefficient
.. _factorial: http://en.wikipedia.org/wiki/Factorial

The code to compute the factorial of an integer number `n`.
is simple::

    f = 1
    for i in range(1, n + 1):
        f *= i

However,
to compute the combinatorial number,
we need to do the same, three times::

    comb = 1

    # multiply by m!
    f = 1
    for i in range(1, m + 1):
        f = f * i
    comb = comb * f

    # divide by (m - n)!
    f = 1
    for i in range(1, m - n + 1):
        f = f * i
    comb = comb / f

    # divide by n!
    f = 1
    for i in range(1, n + 1):
        f = f * i
    comb = comb / f

The only difference between the three factorial computations
is the finish value of each ``for`` loop
(``m``, ``m - n`` and ``n``, respectively).

Writing the same code several times can be a tedious process and error-prone.
The resulting code can be much harder to understand as well, since
it is not obvious at first glance.

The ideal case would be to have a function called ``factorial``
to make the dirty job and we could use it as follows::


    factorial(m) / (factorial(m - n) * factorial(n))

Previously, we saw that Python provides some functions,
like ``int``, ``min`` and ``abs``.
Now we will see how to create our own functions.

Function details
~~~~~~~~~~~~~~~~
.. index:: function details

In programming,
a **function** is a program section that
computes a value independently to the rest of the program.

.. index:: parameter (of a function), result (of a function), return value

A function has three important components:

* **parameters**,
  are the input values which a function receives;
* **function code**,
  are the operations which a function does; and
* **result** (or **return value**),
  is the final value returned by a function.

In essence, a function is a little program.
Their three components are analogs to the input,
the process and the program output.

In the factorial example,
the parameter is the integer number which we want to compute the factorial for,
the code is the loop that makes the multiplications
and the result is the calculated value.

Function definition
~~~~~~~~~~~~~~~~~~~
The Python functions are created through the ``def`` statement::

    def name(parameter):
        # function code

The parameters are variables in which the input values are stored.

The function contains code in the same way as any program.
The difference is that, when finished, they submit
their results using a ``return`` statement.

For example,
the function to compute the factorial numbers
could be defined as follows::

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

In this example,
the result given by the function call
is the ``f`` variable value
when the last line of the function is reached.

Once created,
the function can be used as any other,
all the times it is required::

    >>> factorial(0)
    1
    >>> factorial(12) + factorial(10)
    482630400
    >>> factorial(factorial(3))
    720
    >>> n = 3
    >>> factorial(n ** 2)
    362880

.. index:: local variable

Variables that are created inside the function
(including result and parameter)
are called **local variables**
and are visible inside the function,
not outside.

.. index:: global variable

Moreover,
the created variables outside some function
are called **global variables**,
and are visible in the entire program.
However, their values can not be modified,
because an assignation can produce a local variable
with the same name.

In the example, the local variables are ``n``, ``f`` e ``i``.
Once the function call ends,
these variables ceases to exist::

    >>> factorial(5)
    120
    >>> f
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    NameError: name 'f' is not defined

After defining the ``factorial`` function,
we can create other function called ``comb``
to compute the combinatorial numbers::

    def comb(m, n):
        fact_m = factorial(m)
        fact_n = factorial(n)
        fact_m_n = factorial(m - n)
        c = fact_m / (fact_n * fact_m_n)
        return c

The function calls ``factorial`` three times
and later uses the results to compute its own result.
The same function can be written also in a brief way::

    def comb(m, n):
        return factorial(m) / (factorial(n) * factorial(m - n))

The entire program is the follow:

.. literalinclude:: ../_static/programs/combinatorios.py

(You can download it here_).

.. _here: ../_static/programs/combinatorios.py

Note that, thanks to the use of functions,
the main section of the program has four lines
and the example is much easier to understand.

Multiple ``return`` values
~~~~~~~~~~~~~~~~~~~~~~~~~~
In Python, a function can return more than one value.

For example,
the next function
obtains an amount in seconds transformed into hours,
minutes and seconds.
in hours, minutes and seconds::

    def convert_secs(secs):
        hour = secs / (60 * 60)
        minutes = (secs / 60) % 60
        secs = secs % 60
        return hours, minutes and seconds.

Calling the function,
we can assign a name to each of the returned values::

    >>> h, m, s = convert_secs(9814)
    >>> h
    2
    >>> m
    43
    >>> s
    34

Technically, the function is returning a **tuple** of values:

    >>> convert_secs(9814)
    (2, 43, 34)

Functions returning anything
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function can do several actions
without delivering the result.

For example,
if a program needs to print several times some information,
it should encapsulate this action in a function that performs the ``print`` ::

    def data_print(name, lastname, rol, day, month, year):
        print 'Name:', name, lastname
        print 'Rol:', rol
        print 'Birth date:', day, '/', month, '/', year

    data_print('Perico', 'Los Palotes', '201101001-1',  3, 1, 1993)
    data_print('Yayita', 'Vinagre',     '201101002-2', 10, 9, 1992)
    data_print('Fulano', 'De Tal',      '201101003-3', 14, 5, 1990)

In this case,
each call to the ``data_print`` function
shows the data through screen, but does not give any result.
This function type is known in programming like

**procedures** or **subroutines**,
but in Python are simple functions.

Technically, all the returning values are functions.
In the case of a function lacking the ``return`` statement,
the return value is always ``None``.
But as the function call is not an assignment,
we loose the value and there is no program effect.

Assignment 2
------------

PENDING
