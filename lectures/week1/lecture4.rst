Lecture 4 - Data types
----------------------

.. index:: Data types

(`Python standard data types official documentation`_)

.. _Python standard data types official documentation: http://docs.python.org/library/stdtypes.html

A **data type** is the property of a value
that defines its domain (possible values),
what operations can be applied to it
and how it is represented by the computer.

All the values in a program have a type.

Below we will review the Python elemental data types.
Later in this course, we will learn several other types available in Python
and, finally, we will learn how to create our own data types.


Strings
~~~~~~~

.. index:: string, text data types, str

A **string** is a value that
represents text, and whose type is **str**.

The literal strings
are represented in a program
by enclosing it in single or double quotes::

   "example 1"
   'example 2'

The advantage of having two kinds of quotes
is that we can use one of them when the other
appears in the text::

    "Let's go!"
    'She said "hello"'

The arithmetic operators can no be applied on strings,
with two exceptions:

1. The ``+`` operator, applied to two strings
   not represent the sum, but the **concatenation**,
   which means join the strings
   one after the other::

    >>> "hello " + 'world'
    'hello world'
    >>> "c" + "i" + "a" + "o" + "!!!"
    'ciao!!!'

2. The ``*`` operator applied to a string and to a number
   not represent the multiplication,
   but the **repetition**,
   i.e. the string is repeated as many times as indicated the number::

    >>> "lo" * 5
    'lololololo'
    >>> "tra" + "la" * 6
    'tralalalalalala'

**Note:** To know the string length, you can use the function ``len()``::
    >>> len('ALMA')
    4
    >>> len('Ata'+'cama')
    7

It is important to understand that strings
are not the same as the values that can be represented 
inside them::

   >>> 5 == '5'
   False
   >>> True == 'True'
   False

The strings with lower and upper case differences 
(case sensitive), or with blank spaces are not the same::

   >>> 'table' == 'Table'
   False
   >>> ' table' == 'table '
   False

You can print multiple lines in different ways,
for example using the ``\n`` symbol, that indicates a new line
you can jump to the next line::

   >>> msg = "hello\nworld"
   >>> print msg
   hello
   world

Another way is surround the strings with triple-quotes: ``"""`` or ``'''``.::

    print """
    usage: bc [options] [file ...]
      -h  --help         print this usage and exit
      -i  --interactive  force interactive mode
      -l  --mathlib      use the predefined math routines
      -q  --quiet        don't print initial banner
      -s  --standard     non-standard bc constructs are errors
      -w  --warn         warn about non-standard bc constructs
      -v  --version      print version information and exit
    """

produces the following output::

    usage: bc [options] [file ...]
      -h  --help         print this usage and exit
      -i  --interactive  force interactive mode
      -l  --mathlib      use the predefined math routines
      -q  --quiet        don't print initial banner
      -s  --standard     non-standard bc constructs are errors
      -w  --warn         warn about non-standard bc constructs
      -v  --version      print version information and exit
    
Also, you can obtain access to each character of the string with an **index**,
starting from 0.
If you want to access a sub-string of the string, you can also
obtain a sub-string from ``i`` to ``j-1`` position.::

   >>> word = "ALMA"
   >>> word[2]
   'M'
   >>> word[0]
   'A'
   >>> word[1:3] # characters from 1 to 3-1
   'LM'
   >>> word[0:] # all the characters from 0
   'ALMA'
   >>> word[:4] # first four characters
   'ALMA'

The Python strings cannot be changed, assigning another character to an indexed position::

    >>> word[0] = 'x'
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    TypeError: object does not support item assignment

You can use negative index, to display the characters from right to left::

    >>> word[-1]     # The last character
    'A'
    >>> word[-2]     # The last-but-one character
    'M'
    >>> word[-3:]    # The last three characters
    'MA'
    >>> word[:-2]    # Everything except the last two characters
    'AL'

If you want to know if a string is inside another string,
you can use the ``in`` operator. For example::

    >>> "ll" in "finally"
    True
    >>> "u" in "planet"
    False

Boolean
~~~~~~~

.. index:: bool, logic value, boolean value

The logic values ``True`` and ``False``
have type **bool**, which represents logic values.

The type ``bool`` is named after the mathematician `George Boole`_,
who created an algebraic system for binary logic.
For this reason,
the ``True`` and ``False`` values are also called
**boolean values**.
The name is not very intuitive, but we need to know it because
it is very used in computer programming.

.. _George Boole: http://en.wikipedia.org/wiki/George_Boole

The logic operations ``and`, ``or`` and ``not``
can be applied on boolean values,
and return as result a boolean value::

   >>> True and True
   True
   >>> True or False
   True
   >>> not True
   False
   >>> not True and not True
   False
   >>> not True or (True and False)
   False

The **relational operations** ``<``, ``>``, ``==``, ``!=``,
``<=``, ``>=``, ``is`` and ``is not``, can be applied on
comparable types values, but always return as result a boolean
value::

    >>> 2 + 2 == 5
    False
    >>> x = 95.4
    >>> 50 < x < 100
    True

The relational operations allow to compare string alphabetically::

    >>> "a" < "b" < "c"
    True
    >>> "a" < "d" < "c"
    False
    >>> "air" < "aircraft" < "bull" < "bullet" < "zombie"
    True

None
~~~~

.. index:: null type, None

There is a value called  **None**
which is used to represent cases
where no value is valid
or to indicate that the current value of a
variable does not make sense.

The ``None`` value has its own type,
called ``NoneType``,
which is different to all other values.

Exercises
~~~~~~~~~

1. Create a program that makes a fusion between two words.
   The idea is obtain the first-half of the first word,
   and the last-half of the second word.
   Consider only words with pair length. For example.::

       Enter word1 = `hi`
       Enter word2 = `planet`
       The Fusion is `hnet`

   ::

       Enter word1 = `orange`
       Enter word2 = `bear`
       The Fusion is `oraar`

   Remember the ``len()`` function.

2. Without using the computer, evaluate the next expressions
   and for each of them indicate the result and the type (if the expression is valid)
   or the expected error (if is not valid)::

       >>> 2 + 3      # Answer: integer type, value is 5
       >>> 4 / 0      # Answer: zero division error
       >>> 5 + 3 * 2
       >>> '5' + '3' * 2
       >>> 2 ** 10 == 1000 or 2 ** 7 == 100
       >>> len('one') == len('two')
       >>> 'hello' * 1.2
       >>> 3 < (1024 % 10) < 6
       >>> 'six' + 'eight'
       >>> 'six' * 'eight'
       >>> "yes" * 2**2
       >>> 3 in '33'
       >>> not None
       >>> "pro" in "Proceedings"
   
   Once you finish, verify your results with the computer. 

3. Write a program that receives two words,
   and verifies if the first one is in the second one::

       Enter word 1 : `hi`
       Enter word 2 : `imaginary`
       False

   ::
       
       Enter word 1: `an`
       Enter word 2: `elephant`
       True
