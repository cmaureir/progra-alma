Lecture 2
=========

Script creation
---------------

PENDING

Control statements
------------------

A program is a **statement** succession
being executed sequentially.

For example, the following program has four statements::

    n = int(raw_input('Enter n: '))
    m = int(raw_input('Enter m: '))
    sum = n + m
    print 'The sum of n and m is:', sum

The first three lines are assignments,
and the last one is a function call.
Running the program,
each of these statements is executed,
one after the other, once.

.. index:: control statement

Besides the simple statements,
which are sequentially executed,
there are the **control statements**
allowing modify the program flow
introducing loops and conditionals.

.. index:: conditional

A **conditional** is a statement set
which can or can not execute,
depending of a condition result.

.. index:: loop

A **loop** is a statement set
which are executed several times,
until one of the end condition was satisfied.

.. index:: indentation

The conditionals and the loops
contains other statements.
To indicate this relation
python use the **identation**:
the contained statements
are not writed in the same column
that the control statement,
but more to the right::

    n = int(raw_input())
    m = int(raw_input())
    if m < n:
        t = m
        m = n
        n = t
    print m, n

In this example, the three asignations are
contained inside the ``if`` control statement.
The ``print m, n`` is not indented,
so is not a part of the ``if`` statement.

This program has four statements,
of which the third one is a control statement,
that contain the other three statements.

To indent,
we will use four spaces always.

if conditional
~~~~~~~~~~~~~~
.. index:: if

The **if** statement
execute the instrutions
only if a condition is satisfied.
Si la condición es falsa,
no se hace nada:

.. image:: ../diagrams/if.png
   :alt: (if flow diagram)

The syntax is as follows::

    if condition:
        statements

For example,
the following program congratulates someone
thats approved the course::

    nota = int(raw_input('Enter your grade: '))
    if grade >= 55:
        print 'Congratulations!'

Execute this program,
testing it several times with different values.

if-else conditional
~~~~~~~~~~~~~~~~~~~
.. index:: if-else

The **if-else** statement
decide what instructions execute
depending if a condition is true or false:

.. image:: ../diagrams/if-else.png
   :alt: (if-else flow diagram)

The syntax is as follows::

    if condición:
        qué hacer cuando la condición es verdadera
    else
        qué hacer cuando la condición es falsa

For example,
the following program indicates if someone is an adult (in Chile)::

    edad = int(raw_input('How old are you? '))
    if edad < 18:
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
so it is not a part of the conditional,
and will be always executed.

if-else-elif conditional
~~~~~~~~~~~~~~~~~~~~~~~~
.. index:: if-elif-else

The **if-elif-else** statement
depends on two or more conditions,
which are evaluated in order.
The first which is true
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
1000 ≤ sueldo < 2000                     5%
2000 ≤ sueldo < 4000                    10%
4000 or higher                          12%
====================== ====================

So, the program that compute the tax to pay
is as follow::

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

Always only one of the alternatives will be executed.
If one of the conditions, in order, is true,
the below conditions are not being evaluated.

Another way to write the same program
using only the ``if`` sentece is as follow::


    salary = int(raw_input('Enter salary: '))
    if salary < 1000:
        rate = 0.00
    if 1000 <= sueldo < 2000:
        rate = 0.05
    if 2000 <= sueldo < 4000:
        rate = 0.10
    if 4000 < sueldo:
        rate = 0.12
    print 'You must pay', rate * salary, 'of taxes'

This way is less clear,
because is not obvious at first look that
only one of the conditions will be true.

Loops
-----

while loop
~~~~~~~~~~~

.. index:: while

The **while** loop
execute a intruction sequence
while a condition is true:

.. image:: ../diagrams/while.png
   :alt: (while flow diagram)

.. index:: iteration

An **iteration**,
is each time which the content of the loop is executed.

The condition is evaluated before each iteration.
If the condition is initially false,
the loop will not run ever.

the syntax is as follows::

    while condition:
        statements

For example,
the next program
multiply two integer numbers
without using the ``*`` operator::

    m = int(raw_input())
    n = int(raw_input())
    p = 0
    while m > 0:
        m = m - 1
        p = p + n
    print 'The product between m and n is', p

To see the functionallity of this program,
les do a routing with the ``m`` = 4 and ``n`` = 7
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

In each iteration,
the ``m`` value decrease once.
When the value reaches the zero value,
the ``while`` condition ceases being true
so the loop ends.
Thus,
is achieved a result composed by
the sum of ``m`` times the ``n`` value.

Note that the loop do not finish exactly when ``m`` reaches zero value.
The condition is evaluated once the entire iteration is finish.

En general,
el ciclo ``while`` se utiliza cuando no es posible saber de antemano
cuántas veces será ejecutado el ciclo,
pero sí qué es lo que tiene que ocurrir
para que se termine.



for loop with counter
~~~~~~~~~~~~~~~~~~~~~~

.. index:: for, variable de control

El ciclo **for con rango**
ejecuta una secuencia de sentencias
una cantidad fija de veces.

Para llevar la cuenta,
utiliza una **variable de control**
que toma valores distintos en cada iteración.

Una de las sintaxis para usar un ``for``
con rango es la siguiente::

    for variable in range(fin):
        qué hacer para cada valor de la variable de control

En la primera iteración,
la variable de control toma el valor 0.
Al final de cada iteración,
el valor de la variable aumenta automáticamente.
El ciclo termina justo antes que la variable
tome el valor ``fin``.

Por ejemplo,
el siguiente programa muestra los cubos
de los números del 0 al 20::

    for i in range(21):
        print i, i ** 3

.. index:: range, rango

Un **rango** es una sucesión de números enteros equiespaciados.
Incluyendo la presentada más arriba,
hay tres maneras de definir un rango::

    range(final)
    range(inicial, final)
    range(inicial, final, incremento)

El valor inicial siempre es parte del rango.
El valor final nunca es parte del rango.
El incremento indica la diferencia
entre dos valores consecutivos del rango.

Si el valor inicial es omitido, se supone que es 0.
Si el incremento es omitido, se supone que es 1.

Con algunos ejemplos quedará más claro:

==================== ===================================
``range(9)``         0, 1, 2, 3, 4, 5, 6, 7, 8
``range(3, 13)``     3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
``range(3, 13, 2)``  3, 5, 7, 9, 11
``range(11, 4)``     ningún valor
``range(11, 4, -1)`` 11, 10, 9, 8, 7, 6, 5
==================== ===================================

Usando un incremento negativo,
es posible hacer ciclos que van hacia atrás::

    for i in range(10, 0, -1):
        print i
    print 'Feliz anno nuevo!'

In gneral,
the ``for`` loop with range
is used when the iteration number is know
before entering the loop.

Functions
---------
.. index:: function

Suppose we need write a program which caculate the
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

The code to compute the factorial of a integer number `n`.
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

Write the same code several times is a tedious process and error-prone.
Also, the resulting code is much more harder to understand,
it is no obvious at a glance what makes.

Ideally would be that there is a function called ``factorial``
to make the dirty job, and we can use it as follows::


    factorial(m) / (factorial(m - n) * factorial(n))

Previously, we saw that Python provides some functions,
like ``int``, ``min`` and ``abs``.
No we will see how to create our owns functions.

Function details
~~~~~~~~~~~~~~~~
.. index:: function details

In programming,
a **function** is a program section thar
compute a value indepently to the rest of the program.

.. index:: parameter (of a function), result (of a function), return value

A function has three important components:

* **parameters**,
  are the input values which receives a function;
* **function code**,
  are the operations which a function do; and
* **result** (or **return value**),
  are the final value given by a function.

In essence, una function is a little program.
Their three component are analogs to the input,
the process and the program output.

In the factorial example,
the parameter is the integer number which we want to compute the factorial,
the code is the loop that makes the multiplications,
and the result is the calculated value.

Function definition
~~~~~~~~~~~~~~~~~~~
The Python functions are created through the ``def`` statement::

    def name(parameter):
        # function code

The parameters are variables in which are stored the input values.

The function contains code equals to any program.
The difference is that, when finished, must submit
their results using a ``return`` statement.

For example,
the function to compute the factorial
could be defined as follows::

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

In this example,
the given result by the function call
is the ``f`` variable value
when reach the last line of the function.

Once created,
the function can be used as any other,
all the required times::

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
are called **local variables**,
and are visibles inside the function,
not outside.

.. index:: global variable

Moreover,
the created variables outside some function
are called **global variables**,
and are visibles in the entire program.
However, their value can not be modified,
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

After define the ``factorial`` function,
we can create other function called ``comb``
to compute the combinatorial numbers::

    def comb(m, n):
        fact_m = factorial(m)
        fact_n = factorial(n)
        fact_m_n = factorial(m - n)
        c = fact_m / (fact_n * fact_m_n)
        return c

The function calls ``factorial`` three times,
and later use the results to compute its result.
La misma función puede ser escrita también de forma más sucinta::

    def comb(m, n):
        return factorial(m) / (factorial(n) * factorial(m - n))

The entire program is the follow:

.. literalinclude:: ../_static/programs/combinatorios.py

(You can download it here_).

.. _here: ../_static/programs/combinatorios.py

Note that, thnks to the functions use
the main section of the programi has four lines,
and the example is much easier to understand.

Multiple return values
~~~~~~~~~~~~~~~~~~~~~~
In Python, a function can return more than one value.

For example,
the next function
obtains an amount in seconds transformed into hours,
minutes or the same seconds.
en horas, minutos y segundos::

    def convert_secs(secs):
        hoour = secs / (60 * 60)
        minutos = (secs / 60) % 60
        secs = secs % 60
        return hours, minutes and seconds.

Calling the function,
we can assign a name to each one of the returned values::

    >>> h, m, s = convert_secs(9814)
    >>> h
    2
    >>> m
    43
    >>> s
    34

Technicaly, the functon is returning a values **tuple**:

    >>> convert_secs(9814)
    (2, 43, 34)

Functions returning anything
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function can do several actions
without delivering the result.

For example,
if a program needs to print several times some information,
should encapsukate this action in a function that perform the ``print`` ::

    def data_print(name, lastname, rol, day, month, year):
        print 'Name:', nombre, apellido
        print 'Rol:', rol
        print 'Birth date:', day, '/', month, '/', year

    data_print('Perico', 'Los Palotes', '201101001-1',  3, 1, 1993)
    data_print('Yayita', 'Vinagre',     '201101002-2', 10, 9, 1992)
    data_print('Fulano', 'De Tal',      '201101003-3', 14, 5, 1990)

In this case,
each call to the ``imprimir_dato`` function
shows the data through screen, but does not give some result.
This function type is knowed in programming like

**procedures** or **subroutines**,
but in Python are simple functions.

Technically, all the returning value are functions.
In the case of do not have a ``return`` statement,
the return value always is ``None``.
But as the function call is not on an assignment,
we lose the value, and there is no program effect.

Assignment 2
------------

PENDING
