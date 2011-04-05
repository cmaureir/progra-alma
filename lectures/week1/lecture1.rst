Lecture 1 - Algorithm elements
------------------------------

Expressions
~~~~~~~~~~~

.. index:: expression

An **expression** is a combination of values and operations
which are evaluated during execution
and yields a result.
For example, :math:`2 + 3` is an expression
which, when evaluated, always returns the value 5.

In the example, :math:`b^2 - 4ac` is an expression,
whose result depends on what values
:math:`a`, :math:`b` and :math:`c` have
at evaluation time.

Assignment
~~~~~~~~~~~

.. index:: assignment, variable, ID

When an algorithm calculates some values
you need to put a name to be able to refer them
in the following steps.
This is what we do in the step 2 of our algorithm,
when we calculate the discriminant and we call it :math:`A`.
This is called an **assignment**,
and is represented as::

    name = expression

The name used in an expression is called
**variable** or **ID**.

The assignment in the previous example, will be::

    Δ = b² − 4 * a * c

An assignment must be interpreted as follows:

1. The expression at the right of the``=`` is evaluated,
   using the values that the variables have at that moment;
2. Once the result is obtained
   the variable at the left of the ``=`` takes the result as its value.

Under this interpretation,
an assignment like this is perfectly possible::

    i = i + 1

First, the expression is evaluated
and their result is the successor of the actual ``i`` value.
For example, if ``i`` has the value 15,
after the assignment it will have the value 16.
This does *not* mean that 15 = 16.

Conditionals
~~~~~~~~~~~~

.. index:: conditional

Sometimes an algorithm must do different steps
under different conditions.
This is what we do in the third step of the example:
we say that the equation does not have solutions
only when the `Δ < 0` condition is satisfied.
This is called **conditional**.

The condition that determines what to execute
is an expression, whose value must be either
true or false.

Loops
~~~~~

.. index:: loop, finish condition

A **loop** occur when
an algorithm execute a set of instructions
several times.

As an algorithm cannot get stuck,
a loop must have a finish condition. The condition is an
expression and its value indicates if the loop must continue or finish.

There are no loops in the example.

Input
~~~~~

.. index:: input, read

When an algorithm needs to receive data,
it is represented as::

    variable = input()

or::

    variable = input("example message:")

This means that the data 
will be stored in the variable
during the execution.

In the example, the input occurs in the first step,
and can be represented as::

    a = input()
    b = input()
    c = input()

Output
~~~~~~

.. index:: output, write

Once the algorithm solves the problem
for which it was designed,
it must return its results as a message.
The output is represented as::

    print(message)

If the message is text,
it has to be between quotation marks.
If it is a variable,
only the name of the variable is required.

In the example, when there are no solutions,
the output can be represented as::

    print('No solutions')

When there is only one solution,
is possible to include it in the message::

    print 'The only solution is', x

Exercises
~~~~~~~~~

1. Open a Python terminal executing ``python`` in a Linux terminal,
   or double clicking the ``Python`` icon in windows,
   and write lines to *enter your name* and display a *hello* message,
   in this way::

       Enter your name: `John`
       Hello John!

   Remember the **input()** and the **print** functions. 

2. You do not need to solve this exercise, the idea is to introduce yourself into
   the programming world, giving you a little taste of Python coding.
 
   **Problem:** Design an algorithm to determine if a natural number
   is prime or not.
    
   Remember that a prime number is a number divisible only by `1` and `itself`,
   so we can catch a clue about how our algorithm could be.
   We need to search divisors between `2` and `(n-1)`.

   Take a look of the following flow diagram, that explains a solution algorithm:

   .. image:: ../../diagrams/primes.png
      :alt: (primes flow diagram)
   
   We need to start thinking that the number is prime,
   and if we find a divisor, we modify the assumption.
   At the end, we need to verify if the assumption is
   true or false to return the correct answer.

   Try the diagram with an example, is the number `91` prime?.

   In the same way, we can describe the algorithm using `pseudocode`_.

.. _`pseudocode`: http://en.wikipedia.org/wiki/Pseudocode

   .. testcase::

        read `n`
        is_prime = true
        `for` d `from` 2 `to` n - 1:
           `if` n is divisible by d:
              is_prime = false
        `if` is_prime is true:
           write "n is prime"
        `in other case`:
           write "n is not prime"


   And finally, the Python version of the algorithm will be::

       n = int(raw_input('Enter n: '))
       is_prime = True
       for d in range(2, n):
           if n % d == 0:
               is_prime = False
           if is_prime:
               print n, 'is prime'
           else:
               print n, 'is not prime'

   Do not worry if you don understand some statements,
   the idea is to give you an approach to a Python program.
   In the next lecture, you will run this code in your computer.
