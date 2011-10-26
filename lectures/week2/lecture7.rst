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

One of the syntax for using a ``for``
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

A **range** is a expiates integer number sequence.
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
``range(3, 13)``     3, 4, 5, 6, 7, 8, 9, 10, 11, 12
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

#. Write a program that show the multiplication table from
   1 to 10 of a number entered bu the user:

   .. testcase::

        Enter a number: `9`
        9 x 1 = 9
        9 x 2 = 18
        9 x 3 = 27
        9 x 4 = 36
        9 x 5 = 45
        9 x 6 = 54
        9 x 7 = 63
        9 x 8 = 72
        9 x 9 = 81
        9 x 10 = 90

#. Write a program which generate all the powers of 2
   from 0 to ``n``, with ``n`` entered by the user:

   .. testcase::
   
       Enter a: `10`
       1 2 4 8 16 32 64 128 256 512 1024 

#. Write a program which ask to the user to enter two integer
   numbers, and then return the sum of all the numbers between them.
   For example, if the numbers are  1 and 7,
   must return as result ``2 + 3 + 4 + 5 + 6 = 20``.
   
   .. testcase::
   
       Enter first number: `1`
       Enter second number: `7`
       The sum is 20

#. Write a program which show a multiplication table as follow:
   
   .. testcase::
   
        1   2   3   4   5   6   7   8   9  10
        2   4   6   8  10  12  14  16  18  20
        3   6   9  12  15  18  21  24  27  30
        4   8  12  16  20  24  28  32  36  40
        5  10  15  20  25  30  35  40  45  50
        6  12  18  24  30  36  42  48  54  60
        7  14  21  28  35  42  49  56  63  70
        8  16  24  32  40  48  56  64  72  80
        9  18  27  36  45  54  63  72  81  90
       10  20  30  40  50  60  70  80  90 100
   
   The numbers must be aligned to the right.

#. Write a program which return all the divisors of an entered number:
   
   .. testcase::
   
       Enter a number: `200`
       1 2 4 5 8 10 20 25 40 50 100 200

#. A traveler must to know how much time takes a past travel.
   He has the time in minutes of each section of the trip.
   
   Develop a program which allow to enter the times of the travel sections
   and return as result the total time of the trip in the ``hours:minutes`` format.
   
   The program stop to receive the travel time when the user
   enter the number 0.
   
   .. testcase::
   
       Section time: `15`
       Section time: `30`
       Section time: `87`
       Section time: `0`
       Travel time: 2:12 horas
   
   .. testcase::
   
       Section time: `51`
       Section time: `17`
       Section time: `0`
       Travel time: 1:08 horas
   

#. Write a program which ask to the user to input
   the height and width of a rectangle and draw it
   using asterisks:

   .. testcase::
   
    Height: `3`
    Width: `5`

    *****
    *****
    *****

#. Write a program which draw a triangle of the size specified
   by the user:

   .. testcase::

    Height: `5`

    *
    **
    ***
    ****
    *****

#. Write a program which draw an hexagon, and the user must enter
   the size of the side:

   .. testcase::

       Side size: `4`

          ****
         ******
        ********
       **********
        ********
         ******
          ****

#. Develop a program to estimate the π_ value,
   using the next infinite sum:
   
   .. math::
   
      \pi = 4 \left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+ \ldots \right) 
   
   The input of the program must be an integer number `n`
   which indicates how many terms the sum will use.
   
   .. testcase::
   
      n: `3`
      3.466666666666667
   
   .. testcase::
   
      n: `1000`
      3.140592653839794
   
   .. _π: http://en.wikipedia.org/wiki/Pi
     
#. Develop a program which allow to work with the fractional powers of two, i.e.:
   
   .. math::
   
      \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \frac{1}{32}, \frac{1}{64}, \ldots
   
   in decimal form:
   
   .. math::
   
      0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, \ldots
   
   The program must show three columns which contain the next information::
   
         Power     Fraction  Sum 
         1         0.5       0.5 
         2         0.25      0.75 
         3         0.125     0.875 
         4         0.0625    0.9375 
         ...       ...       ... 
   
   The program must finish when the decimal fraction be lower or equal to 0.000001.

#. The Euler number, :math:`e \approx 2,71828`,
   can be represented as the following infinite sum:
   
   .. math::
   
       e = \frac{1}{0!} +  \frac{1}{1!} +  \frac{1}{2!} +  \frac{1}{3!} +  \frac{1}{4!} + \ldots
   
   Develop a program which return a approximate value of *e*,
   calculating this sum until the difference between two consecutive addends
   being less than 0.0001.
   
   Remember that the factorial *n*! is the product of the numbers from  1 to *n*.

#. The Collatz sequence of an integer number
   is builded as the following way:
   
   * if is a pair number, its divided by two;
   * if is odd, its multiplicated by three and add one to the result;
   * the succession ends when reach the one value.
   
   The `Collatz conjecture`_ says, starting from any numner,
   the sequence always will reach to one.
   Although an assertion is very easy,
   is not possible to show if is true or not, so far.
   
   .. _Collatz conjecture: http://en.wikipedia.org/wiki/Collatz_conjecture
   
   Using computer, has been verified that the sequence reach the one value
   staring from any natural number lower than `2^{58}`.
   
   #. Develop a program which return the Collatz sequence of an integer number:
   
      .. testcase::
   
           n: `18`
           18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
   
      .. testcase::
   
           n: `19`
           19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
   
      .. testcase::
   
           n: `20`
           20 10 5 16 8 4 2 1
   
   #. Develop a program which plot the length of the Collatz sequence
      of the positive integer numbers, lower than the number entered by the user:
   
      .. testcase::
   
           n: `20`
           1 *
           2 **
           3 ********
           4 ***
           5 ******
           6 *********
           7 *****************
           8 ****
           9 ********************
           10 *******
           11 ***************
           12 **********
           13 **********
           14 ******************
           15 ******************
           16 *****
           17 *************
           18 *********************
           19 *********************
           20 ********
  
