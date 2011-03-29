Lecture 6 - Control statements
-------------------------------

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

.. image:: ../../diagrams/if.png
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

.. image:: ../../diagrams/if-else.png
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

.. image:: ../../diagrams/if-elif-else.png
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
by using only the ``if`` statement is as follows::


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
because it is not obvious at a first glance that
only one of the conditions will be true and all 
the conditions are evaluated.

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

.. _`1`: http://progra.usm.cl/apunte/ejercicios/1/par-o-impar.html
.. _`2`: http://progra.usm.cl/apunte/ejercicios/1/bisiestos.html
.. _`3`: http://progra.usm.cl/apunte/ejercicios/1/division.html
.. _`4`: http://progra.usm.cl/apunte/ejercicios/1/palabra-mas-larga.html
.. _`5`: http://progra.usm.cl/apunte/ejercicios/1/ordenamiento-basico.html
.. _`6`: http://progra.usm.cl/apunte/ejercicios/1/letra-o-numero.html
.. _`7`: http://progra.usm.cl/apunte/ejercicios/1/calculadora.html
.. _`8`: http://progra.usm.cl/apunte/ejercicios/1/edad.html
.. _`9`: http://progra.usm.cl/apunte/ejercicios/1/set-de-tenis.html 
.. _`10`: http://progra.usm.cl/apunte/ejercicios/1/triangulos.html
.. _`11`: http://progra.usm.cl/apunte/ejercicios/1/indice-masa-corporal.html
