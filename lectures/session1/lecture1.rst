Lecture 1 - Algorithm elements
------------------------------

Expressions
~~~~~~~~~~~

.. index:: expression

An **expression** is a value and operation combination
which are evaluated during the algorithm execution
to obtain a certain value.
For example, :math:`2 + 3` is an expression
which, evaluating it, always return the :math:`5` value.

In the example, :math:`b^2 - 4ac` is an expression,
whose value depends on what values have
:math:`a`, :math:`b` and :math:`c`
at the evaluation moment.

Asignations
~~~~~~~~~~~

.. index:: assignation, variable, identificator

When an algorithm calculates some values,
you need to put a name to able to refer them
in the next steps. 
Is what we do in the step 2 of our algorithm,
when we calculate the discriminating and we call it :math:`A`.
This is called **assignation**,
and is represented as::

    name = expression

To the used name in an expression is called
**variable** or **identificator**.

The assignation in the previous example, will be::

    Δ = b² − 4 * a * c

An assignation must be interpreted as follows:

1. first, ``=`` right expression is evaluated,
   using the values of the variables, in that moment.
2. once the result is obtained,
   the ``=`` left variable value is replaced by this result.

Under this interpretation,
is perfectly posible an assignation like this::

    i = i + 1

First, the expression is evaluated,
and their result is the successor of the actual ``i`` value.
For example, if ``i`` has the value 15,
after the assignation will be have the value 16.
This *not* mean that 15 = 16.

Conditionals
~~~~~~~~~~~~

.. index:: conditional

Sometimes an algorithm must do different steps
under different conditions.
Is what we do in the step 3 of the example:
we say that the equation does not have solutions
only when the `Δ < 0` condition is satisfied..
This is called **conditional**.

The condition that determine what execute
is an expression, whose value must be
true or false.

Loops
~~~~~

.. index:: loop, finish condition

A **loop** ocurr when
an algorithm execute a set of instructions
several times.

As an algorithm can not get stuck,
a loop must have also a finish condition,
which value indicates if the loop must continue or finish.

The example do not have loops.

Input
~~~~~

.. index:: input, read

When an algorithm need to receive data,
is represented as::

    variable = input()

During the execution,
thi means that the data
must stay saved in the variable.

In the example, the input ocurrs in the first step,
and can be represented as::

    a = input()
    b = input()
    c = input()

Output
~~~~~~

.. index:: output, write

Once the algorithm solve the problem
for which it was designed,
must return his results like a message.
The output is represented as::

    print(menssage)

If the message is text,
goes between quotation.
If is a variable,
is just the name of the variable.

In the example, when there ir no solutions,
the output can be represented as::

    print('No solutions')

When there is an only solution,
is possible to include it in the message::

    print 'The only solution is', x
