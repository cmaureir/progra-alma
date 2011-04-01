Lecture 7 - Loops
-----------------

(`Python while official documentation`_)

.. _Python while official documentation: http://docs.python.org/reference/compound_stmts.html#while


``while`` loop
~~~~~~~~~~~~~~

.. index:: while

The **while** loop
executes an instruction sequence
while a condition is true:

.. image:: ../../diagrams/while.png
   :alt: (while flow diagram)

.. index:: iteration

An **iteration** is defined as each of the times
the body of a loop is executed.

The condition is evaluated at the beginning of each iteration.
If the condition is initially false,
the loop will not be executed even once.

The syntax is as follows::

    while condition:
        statements

For example,
the following program
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
let's see what values do all its variables take
when the input is ``m`` = 4 and ``n`` = 7:

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
the ``m`` value decreases by one.
When it reaches zero,
the condition ceases being true
so the loop ends.
Thus, a result composed by the sum of 
``m`` times the ``n`` value is achieved.

Note that the loop does not finish exactly when ``m`` reaches zero.
The condition is evaluated once the entire iteration has finished.

In general,
the ``while`` loop is used when it is not possible to know in advance
how many times the loop will executed,
but the termination condition is known.


``for`` loop with counter
~~~~~~~~~~~~~~~~~~~~~~~~~

(`Python for official documentation`_)

.. _Python for official documentation: http://docs.python.org/tutorial/controlflow.html#for-statements

.. index:: for, control variable

The **for loop with range**
executes a sequence of statements
a fixed number of times.

To keep the count,
it uses a **control variable**
that takes a different value on each iteration.

One of the syntaxes for using a ``for``
loop with range is the following::

    for variable in range(end):
        what to do for each value of the control variable

In the first iteration,
the control variable takes value 0.
At the end of each iteration,
the variable value increases automatically.
The loop ends just before the control variable takes the
``end`` value.

For example,
the next program shows the cube of the numbers
from 0 to 20::

    for i in range(21):
        print i, i ** 3

.. index:: range

A **range** is a equispaced integer number sequence.
There are three ways to define a range::

    range(final)
    range(initial, final)
    range(initial, final, increase)

The initial value is always part of the range.
The final value is never part of the range.
The increase shows the difference between two consecutive values in the range.

If the initial value is omitted, it supposed to be 0.
If the increment is omitted, it supposed to be 1.

This will be clearer with some examples:

==================== ===================================
``range(9)``         0, 1, 2, 3, 4, 5, 6, 7, 8
``range(3, 13)``     3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
``range(3, 13, 2)``  3, 5, 7, 9, 11
``range(11, 4)``     no valor
``range(11, 4, -1)`` 11, 10, 9, 8, 7, 6, 5
==================== ===================================

It is possible to go backwards by using a negative increment::

    for i in range(10, 0, -1):
        print i
    print 'Happy new year!'

In general,
the ``for`` loop with range
is used when the iteration number is known
before entering the loop.

Exercises
~~~~~~~~~

`1`_
`2`_
`3`_
`4`_
`5`_
`6`_
`7`_
`8`_
`9`_
`10`_
`11`_

.. _`1`: http://progra.usm.cl/apunte/ejercicios/1/multiplos.html 
.. _`2`: http://progra.usm.cl/apunte/ejercicios/1/potencias-dos.html
.. _`3`: http://progra.usm.cl/apunte/ejercicios/1/suma-entre-numeros.html
.. _`4`: http://progra.usm.cl/apunte/ejercicios/1/tablas-de-multiplicar.html
.. _`5`: http://progra.usm.cl/apunte/ejercicios/1/divisores.html
.. _`6`: http://progra.usm.cl/apunte/ejercicios/1/tiempo-de-viaje.html
.. _`7`: http://progra.usm.cl/apunte/ejercicios/1/dibujos-asteriscos.html
.. _`8`: http://progra.usm.cl/apunte/ejercicios/1/pi.html
.. _`9`: http://progra.usm.cl/apunte/ejercicios/1/suma-fracciones.html
.. _`10`: http://progra.usm.cl/apunte/ejercicios/1/e.html
.. _`11`: http://progra.usm.cl/apunte/ejercicios/1/collatz.html
