Lecture 6 - Control statements
-------------------------------

(`Python control flow official documentation`_)

.. _Python control flow official documentation: http://docs.python.org/tutorial/controlflow.html#if-statements


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
which can or cannot be executed,
depending on the result of a condition.

.. index:: loop

A **loop** is a statement set
which is executed several times,
until one of the end conditions are satisfied.

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

In this example, the three assignments are
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
~~~~~~~~~~~~~~~~~~~~~~~
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

The next program does different actions
depending if the input number is even or odd::

    n = int(raw_input('Enter a number: '))
    if n % 2 == 0:
        print 'The number is even'
        print 'The half-number is', n / 2
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

So, a program that computes how much taxes you should pay
could be as follows::

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
only one of the conditions will be true and has the 
drawback that all the conditions will be evaluated.

Exercises
~~~~~~~~~

1. When the earth completes an orbit around the Sun,
   it has made exactly 365 rotations on itself,
   but a little more.
 
   More precisely, the difference is about a quarter of a day.
   
   To avoid an offset between the seasons and the calendar,
   the Julian calendar introduced a rule
   that adds an additional day in the years that are divisible by 4
   (called a `leap year`_),
   to take into consideration the four quarter of a day.
   
   However, even using this rule, there is still a leap,
   that is about 3/400 of a day.
   
   To fix this leap, in the year 1582
   the Pope Gregory XIII introduced a new calendar,
   in which the last year of each century was no longer a leap year,
   unless it was divisible by 400.
   
   Write a program that returns if a year is a leap year or not,
   remembering the current calendar in that year:
   
   .. _`leap year`: http://en.wikipedia.org/wiki/Leap_year 
   
   .. testcase::
   
   	Enter a year: `1988`
   	1988 is a leap year
   
   .. testcase::
   
   	Enter a year: `2011`
        2011 is not a leap year
   
   .. testcase::
   
   	Enter a year: `1700`
        1700 is not a leap year
   
   .. testcase::
   
   	Enter a year: `1500`
        1500 is a leap year
   
   .. testcase::
   
   	Enter a year: `2400`
        2400 is a leap year

2. Write a program that requires two integer numbers and
   calculates the division, indicating if the division is exact or not.
   
   .. testcase::
   
       Dividend: `14`
       Divisor: `5`
   
       not exact division.
       Quotient: 2
       Remainder: 4
   
   .. testcase::
   
       Dividend: `100`
       Divisor: `10`
       
       The exact division.
       Quotient: 10
       Remainder: 0

3. Write a program that requires two numbers,
   then shows it ordered lowest to highest:
   
   .. testcase::
   
   	Enter a number: `51`
   	Enter a number: `24`
        24 51
   
   Next,
   do the same with three numbers:
   
   .. testcase::
   
   	Enter a number: `8`
   	Enter a number: `1`
   	Enter a number: `4`
        1 4 8
   
   Finally,
   do the same with four numbers:
   
   .. testcase::
   
   	Enter a number: `7`
   	Enter a number: `0`
   	Enter a number: `6`
   	Enter a number: `1`
        0 1 6 7
   
   Remember that your program must return the correct answer
   to know the number of combinations,
   not only for the examples showed previously.

4. Write a program that determines if an input character is a character,
   a number or neither.
   In the case that it is a character, determine if it is upper or lower case.
   
   .. testcase::
   
       Enter character: `9`
       Is number.
   
   .. testcase::
   
       Enter character: `A`
       upper-case character.
   
   .. testcase::
   
       Enter character: `f`
       lower-case character.
   
   .. testcase::
   
       Enter character: `#`
       Is not a character or number.


5. Write a program that simulates a basic calculator,
   this can be done using the sum, substraction, multiplication and division operators.
  
   The program must receive as input, two real numbers and one operator,
   that can be ``+``, ``-``, ``*`` or ``/``.
   
   The output of the program must be the operation result:
   
   .. testcase::
   
       Operating: `3`
       Operator: `+`
       Operating: `2`
       3 + 2 = 5
   
   .. testcase::
   
       Operating: `6`
       Operator: `-`
       Operating: `7`
       6 - 7 = -1
   
   .. testcase::
   
       Operating: `4`
       Operator: `*`
       Operating: `5`
       4 * 5 = 20
   
   .. testcase::
   
       Operating: `10`
       Operator: `/`
       Operating: `4`
       10 / 4 = 2.5
   
   .. testcase::
   
       Operating: `-1`
       Operator: `**`
       Operating: `4`
       -1 ** 4 = 1


6. Write a program that returns the user age,
   starting from the date of birth:
   
   .. testcase::
   
       Enter you birth date.
       Day: `14`
       Month: `6`
       Year: `1948`
       You are 62 years old
   
   Of course, the return result depends on the day
   your program is executed.
   
   To obtain the actual date,
   you can use the ``localtime`` function,
   that is provided by the time_ module.
   The values are obtained in the following way
   (suppose today is April 1st, 2011)::
   
       >>> from time import localtime
       >>> t = localtime()
       >>> t.tm_mday
       1
       >>> t.tm_mon
       4
       >>> t.tm_year
       2011
   
   The program must consider if the birthday
   occurred or does not happened in this year.
   
   .. _time: http://docs.python.org/library/time.html



   
7. The risk for a person to suffer coronary diseases
   depends on his age and his body mass index (BMI):
   
     +----------------+---------------+---------------+
     |                | age < 45      | age ≥ 45      |
     +================+===============+===============+
     | **BMI < 22.0** | lower         | middle        |
     +----------------+---------------+---------------+
     | **BMI ≥ 22.0** | middle        | high          |
     +----------------+---------------+---------------+
   
   The BMI is the quotient between the weight (kg) and the
   square of his height (m).
   
   Write a program that receives 
   the height, the weight and the age of a person as input,
   and show the risk condition.
   
   .. [Camp09] Jennifer Campbell et al.
               *Practical Programming:
               An Introduction to Computer Science Using Python*.
               Pragmatic Bookshelf, 2009.

