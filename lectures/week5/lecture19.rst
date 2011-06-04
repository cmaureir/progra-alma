Lecture 19 - Iterators
----------------------

In simple words,
an iterator is a type of object which has a method
to advance over a certain data type.
In almost all the cases that method is called `next()`.

The previous idea is very basic, and not entirely true,
because in Python the most of the iterators
has a lot of methods, built-in, user-defined, etc.

So, iterators objects are used in order to iterate
over an objects data.

For example,
with the content of the previous lectures,
you will now how to do this in Python using lists::

    >>> my_list = ['a',2,(0,0)]
    >>> for item in my_list:
    ...   print item
    ... 
    a
    2
    (0,0)
	
The previous code iterate over a list object
created by us, printing all the list items.

According to the previous example,
lists are iterables since you can iterate over them multiple times.

Please note that, each time you iterate over a list
you are actually using a `listiterator` iterator object
produced automatically by the list.


`for` iterators
~~~~~~~~~~~~~~~

Using the `for` loop is the easiest way
to use the *iterator* concept,
and in the previous lectures you can note
that we can iterate almost any Python data-type,
for example::


    for num in [1, 2, 3]:
        print num
    for num in (1, 2, 3):
        print num
    for key in {'foo':1, 'bar':2}:
        print key
    for char in "hello":
        print char
    for line in open("file.txt"):
        print line

But there is another very useful
methods which should be good to familiarized.

* `zip()` function

  This  function returns a list of tuples,
  taking one-by-one of each iterable given as parameter.
  
  If the sequence of iterables has differente lengths,
  the `zip()` function truncate the lenght to the shortest one.
  
  Using the `*` operator inside the iterable,
  is possible to perform a kind of `unzip` function
  over a list.
  
  Example::
  
      >>> firstnames = ['john','marie','homer']
      >>> lastnames = ['smith','curie','simpsons']
      >>> zipped = zip(firstnames,lastnames)
      >>> zipped
      [('john', 'smith'), ('marie', 'curie'), ('homer', 'simpsons')]
      >>> for i in zipped:
      ...   print i
      ... 
      ('john', 'smith')
      ('marie', 'curie')
      ('homer', 'simpsons')
      >>> fnames , lnames = zip(*zipped)
      >>> fnames
      ('john', 'marie', 'homer')
      >>> firstnames
      ['john', 'marie', 'homer']
      >>> lnames == lastnames
      False
      >>> list(lnames) == lastnames
      True

* `sorted()` function.

  This is a very simple function,
  and the main idea is to sort any element given as parameter,
  returning a sorted list.
  
  We can sort a simple list::
  
      >>> sorted([5, 2, 3, 1, 4])
      [1, 2, 3, 4, 5]
  
  And, we can sort a dictionary by the keys::
  
      >>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
      [1, 2, 3, 4, 5]
  
  
  You can include two optionals parameters, the `cmp`, `key` and `reverse`
  which specifies the following characteristics:
  
   * `cmp`: specify a custom comparison function, but with only two arguments,
     which return a negative, positive or zero number depending on the evaluation
     case. (condiering if the first argument is smaller than the second)
   * `key`: specify a function, with one argument, using to extract a comparison key.
   * `reverse`: specify a boolean value, which when is true, the comparison will be
     performed reversed.
  
  A couple of examples of the previous arguments are:
  
   * Using the `cmp` parameter::
  
       >>> def compare(i,j):
       ...   return i - j
       ... 
       >>> sorted([4,5,1,10],cmp=compare)
       [1, 4, 5, 10]
       >>> def compare(i,j):
       ...   return j - i
       ... 
       >>> sorted([4,5,1,10],cmp=compare)
       [10, 5, 4, 1]
  
   * Using the `key` parameter:
  
     Also, we can use the `sorted()` function to sort words
     in a certain phrase. The strings data types has a method
     called `split()`, which without parameters split a string
     by the empty-spaces, for example::
     
         >>> "hello world!".split()
         ['hello', 'world!']
     
     The string data types also has another method called `upper()`
     which allow to change the *case* of a entire string.
     
     So, we can use the same idea to sort some words::
     
         >>> sorted("Hello world python course!".split(), key=str.upper)
         ['course!', 'Hello', 'python', 'world']
  
  
   * Using the `reverse` parameter::
  
         >>> sorted([4,5,1,10])
         [1, 4, 5, 10]
         >>> sorted([4,5,1,10],reverse=True)
         [10, 5, 4, 1]

* `enumerated()` function

The main idea behind the enumerated function
is to be able to assign a numeration to a certain sequence of objects.
It is importat to know taht the sequence of objects must be iterable.

This function return a tuple with the number and the object,
starting from 0, if the user do not change this starting point,
because is possible adding a new argument called ``start=n``
where ``n`` is the new starting point.

Look the following examples::

    >>> for item in enumerate(['John','Marie','Joseph','Rose']):
    ...   print item
    ... 
    (0, 'John')
    (1, 'Marie')
    (2, 'Joseph')
    (3, 'Rose')
    >>> for index,name in enumerate(['John','Marie','Joseph','Rose']):
    ...   print index, name
    ... 
    0 John
    1 Marie
    2 Joseph
    3 Rose
    >>> for index,name in enumerate(['John','Marie','Joseph','Rose'], start=1):
    ...   print index,name
    ... 
    1 John
    2 Marie
    3 Joseph
    4 Rose
    >>> for index,name in enumerate(['John','Marie','Joseph','Rose'], start=-5):
    ...   print index, name
    ... 
    -5 John
    -4 Marie
    -3 Joseph
    -2 Rose
    >>> 

* `reversed()` function

The ``reversed`` function achieve a very simple
functionallity, change the order, reversing an object
iterable, this mean which is a good idea to use it
when you want to start from the end.

The following examples show the function idea::

    >>> for i in range(1,5):
    ...   print i
    ... 
    1
    2
    3
    4
    >>> for i in reversed(range(1,5)):
    ...   print i
    ... 
    4
    3
    2
    1

::

    >>> fruits = ['Apple','Orange','Apricot','Lemon']
    >>> for i in fruits:
    ...   print i
    ... 
    Apple
    Orange
    Apricot
    Lemon
    >>> for i in reversed(fruits):
    ...   print i
    ... 
    Lemon
    Apricot
    Orange
    Apple

::

    >>> vegetables = ('Peas','Carrot','Onion')
    >>> for i in vegetables:
    ...   print i
    ... 
    Peas
    Carrot
    Onion

::

    >>> name = 'John'
    >>> for i in reversed(name):
    ...   print i
    ... 
    n
    h
    o
    J
    >>> 

.. The buil-in function called `iter()`
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method next() which accesses elements in the container one at a time. When there are no more elements, next() raises a StopIteration exception which tells the for loop to terminate. This example shows how it all works::
.. 
..     >>> s = 'abc'
..     >>> it = iter(s)
..     >>> it
..     <iterator object at 0x00A1DB50>
..     >>> it.next()
..     'a'
..     >>> it.next()
..     'b'
..     >>> it.next()
..     'c'
..     >>> it.next()
..     
..     Traceback (most recent call last):
..       File "<stdin>", line 1, in ?
..         it.next()
..     StopIteration




Iterators from `itertools`
~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python, the iterators are very useful objects
and there is a special module for this, the `itertools`.

To work with the following iterators,
please note that you must import
the module::

    import itertools

* `chain()` function

The ``chain()`` function from the itertools module,
give us the possibility to iterate over a certain numbers of Python object,
does not matter if the objects are `lists`, `tuples`, `strings` etc.

The following examples show their functionallity::

    >>> from itertools import chain
    >>> word1='hello'
    >>> word2=' world'
    >>> for i in chain(word1,word2):
    ...   print i,
    ... 
    h e l l o   w o r l d

::

    >>> my_list=['blue','red','yellow']
    >>> my_name='John'
    >>> for i in chain(my_list,my_name):
    ...   print i,
    ... 
    blue red yellow J o h n
    >>> my_tuple=(19,05,1988)
    >>> for i in chain(my_list,my_name,my_tuple):
    ...   print i,
    ... 
    blue red yellow J o h n 19 5 1988



* `count()` function

The idea of the ``count()``  function,
if to start counting numbers from a certain given number
to the infinite, well, not the infinite, but yes to the
maximum number capacity.

The default call to the function,
start counting numbers one-by-one,
for example
(Be careful! prepare to receive a tons of numbers in your screen,
you can break it pressing `Ctrl + C` in Linux and MacOS, in Windows you can close the ``cmd`` window.) ::

    >>> for i in count(1):
    ...   print i
    ...
    1
    2
    3
    4
    5
    6
    ...

But you can give the `step parameter`,
to move n-by-n, for example::

    >>> for i in count(1,3):
    ...   print i
    ...
    1
    4
    7
    10
    13
    ...

You can use, ``break`` statement, to terminate the loop,
so you do not receive a lot of numbers on your screen,

for example, lets imagine which we are working into solve
a certain problem so, we use a iterative method to find the solution,
you can imagine an infinite iteration until reach the real solution
or an approximated value, using different precission::

    >>> from itertools import count
    >>> solution = 1.45
    >>> initial_solution = 0.3
    >>> for i in count(0.3,0.001):
    ...   if i >= solution:
    ...     print i
    ...     break
    ... 
    1.451
    >>> for i in count(0.3,0.000001):
    ...   if i >= solution:
    ...     print i
    ...     break
    ... 
    1.45000099997
    >>> 

* `cycle()` function

Every programmer has more than once time
to develop a script which compare a certain
sequence of elements over an another big sequence,
so is needed to iterate over a sequence,
and once it finished, we need to iterate again,
the ``cycle()`` function give us the chance
to iterate infinite times over a sequence
to perform any comparison or another
statement.

For example,
image that you are working
with Nitrogenous bases in the DNA (A,T, C, G),
and you are looking for certain pattern over
a big sequence of DNA.
The process will be something like this::

    for i in cycle('ATCG'):
      do_some_biological_stuff(i)


For example,
lets do a simple program
which show the day and number of a month (August, 2011)::

    >>> from itertools import cycle
    >>> august = 31
    >>> days = ['Lu','Tu','We','Th','Fr','Sa','Su']
    >>> count = 1
    >>> for i in cycle(days):
    ...   print i, count
    ...   if count >= january:
    ...     break
    ...   count = count + 1
    ... 
    Lu 1
    Tu 2
    We 3
    Th 4
    Fr 5
    Sa 6
    Su 7
    Lu 8
    Tu 9
    We 10
    Th 11
    Fr 12
    Sa 13
    Su 14
    Lu 15
    Tu 16
    We 17
    Th 18
    Fr 19
    Sa 20
    Su 21
    Lu 22
    Tu 23
    We 24
    Th 25
    Fr 26
    Sa 27
    Su 28
    Lu 29
    Tu 30
    We 31

* `repeat()` function

As the name of this function says,
the idea is to generate a certain numbers of elements
a determinated number of times.

This function require one parameter,
to repeat it indefinite times
the object given as parameter.::

    >>> from itertools import repeat
    >>> for i in repeat(10):
    ...   print i
    ...
    10
    10
    10
    10
    10
    10
    ...

You can give another parameter, to establish
the number of times to repeat the object::

    >>> for i in repeat('hello',5):
    ...   print i
    ... 
    hello
    hello
    hello
    hello
    hello

Exercises
~~~~~~~~~

* PENDING 
* PENDING 
* PENDING 
