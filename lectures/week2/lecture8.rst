Lecture 8 - Functions
---------------------

.. index:: function

Suppose we need to write a program to compute the
`combinatorial number`_ `C(m, n)`, defined by:

.. math::

    C(m, n) = \frac{m!}{(m - n)! n!},

where `n!` (the factorial_ of `n`)
is the product of the integers from 1 to `n`:

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
is the end value of each ``for`` loop
(``m``, ``m - n`` and ``n``, respectively).

Writing the same code several times is a tedious and error-prone process.
The resulting code is harder to understand as well, since
it is not obvious what is does at first glance.

The ideal case would be to have a function called ``factorial``
to do the dirty work that we could use it as follows::

    factorial(m) / (factorial(m - n) * factorial(n))

Previously, we saw that Python provides some functions,
like ``int``, ``min`` and ``abs``.
Now we will see how to create our own functions.

Function details
~~~~~~~~~~~~~~~~
.. index:: function details

In programming,
a **function** is a section of the program that
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
Their three components are analog to the input,
the process and the program output.

In the factorial example,
the parameter is the integer number whose factorial we want to compute,
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
the function to compute the factorial
could be defined as follows::

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

In this example,
the result given by the function call
is the value that variable ``f`` has
when the last line of the function is reached.

Once created,
the function can be used as any other,
as many times it is required::

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
and are only visible inside the function,
not outside.

.. index:: global variable

Moreover,
the variables created outside some function
are called **global variables**,
and are visible from the entire program.
However, their values cannot be modified,
because an assignment would create a local variable
with the same name.

In the example, the local variables are ``n``, ``f`` e ``i``.
Once the function call ends,
these variables cease to exist::

    >>> factorial(5)
    120
    >>> f
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    NameError: name 'f' is not defined

After defining the ``factorial`` function,
we can create another function called ``comb``
to compute the combinatorial numbers::

    def comb(m, n):
        fact_m = factorial(m)
        fact_n = factorial(n)
        fact_m_n = factorial(m - n)
        c = fact_m / (fact_n * fact_m_n)
        return c

This function calls ``factorial`` three times
and later uses the results to compute its own result.
The same function can be written also in a brief way::

    def comb(m, n):
        return factorial(m) / (factorial(n) * factorial(m - n))

The entire program is the follow:

.. literalinclude:: ../../_static/programs/combinatorial.py

(You can download it here_).

.. _here: ../../_static/programs/combinatorial.py

Note that, thanks to the use of functions,
the main section of the program has only four lines
and the example is much easier to understand.

Multiple ``return`` values
~~~~~~~~~~~~~~~~~~~~~~~~~~
In Python, a function can return more than one value.

For example,
the next function
converts an amount of seconds
into hours, minutes and seconds::

    def convert_secs(secs):
        hour = secs / (60 * 60)
        minutes = (secs / 60) % 60
        secs = secs % 60
        return hours, minutes, seconds.

When calling the function,
we can assign a name to each of the returned values::

    >>> h, m, s = convert_secs(9814)
    >>> h
    2
    >>> m
    43
    >>> s
    34

Technically, the function is returning a **tuple** of values::

    >>> convert_secs(9814)
    (2, 43, 34)

Functions returning anything
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function can do several actions
without yielding a result.

For example,
when a program needs to print several times some information,
it should encapsulate this action in a function that performs the ``print`` ::

    def data_print(name, lastname, rol, day, month, year):
        print 'Name:', name, lastname
        print 'ID:', rol
        print 'Birth date:', day, '/', month, '/', year

    data_print('Perico', 'Los Palotes', '201101001-1',  3, 1, 1993)
    data_print('Yayita', 'Vinagre',     '201101002-2', 10, 9, 1992)
    data_print('John',   'Doe',         '201101003-3', 14, 5, 1990)

In this case,
each call to the ``data_print`` function
shows the data in the screen, but it does not give any result.
In programming, this kind of functions are known as
**procedures** or **subroutines**,
but in Python they are plain functions.

Technically, all functions return a value.
In the case of a function lacking the ``return`` statement,
the return value is always ``None``.
But as the function call is not put on the right-hand side of an assignment,
the value is lost and there is no effect on the program.

Exercises
~~~~~~~~~

`1`_
`2`_
`3`_
`4`_

.. _`1`: http://progra.usm.cl/apunte/ejercicios/2/numero-par.html
.. _`2`: http://progra.usm.cl/apunte/ejercicios/2/numeros-palindromos.html
.. _`3`: http://progra.usm.cl/apunte/ejercicios/2/funciones-numeros-primos.html
.. _`4`: http://progra.usm.cl/apunte/ejercicios/2/tabla-verdad.html
