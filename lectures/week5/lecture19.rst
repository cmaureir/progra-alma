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

.. 
.. enumerate(sequence[, start=0])¶
.. Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration. The next() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the corresponding value obtained from iterating over iterable. enumerate() is useful for obtaining an indexed series: (0, seq[0]), (1, seq[1]), (2, seq[2]), .... For example:
.. 
.. >>> for i, season in enumerate(['Spring', 'Summer', 'Fall', 'Winter']):
.. ...     print i, season
.. 0 Spring
.. 1 Summer
.. 2 Fall
.. 3 Winter
.. 
.. 

* `reversed()` function


.. 
.. reversed(seq)¶
.. Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
.. 
.. 
..

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

>>> for i in reversed(xrange(1,10,2)):
...     print i
...
9
7
5
3
1

Use the reversed() built-in function:

>>> a = ["foo", "bar", "baz"]
>>> for i in reversed(a):
...     print i
... 
baz
bar
foo


The buil-in function called `iter()`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method next() which accesses elements in the container one at a time. When there are no more elements, next() raises a StopIteration exception which tells the for loop to terminate. This example shows how it all works::

    >>> s = 'abc'
    >>> it = iter(s)
    >>> it
    <iterator object at 0x00A1DB50>
    >>> it.next()
    'a'
    >>> it.next()
    'b'
    >>> it.next()
    'c'
    >>> it.next()
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
        it.next()
    StopIteration




Iterators from `itertools`
~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python, the iterators are very useful objects
and there is a special module for this, the `itertools`.

To work with the following iterators,
please note that you must import
the module::

    import itertools

* `chain()` function

.. itertools.chain(*iterables)¶
.. Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence. Equivalent to:
.. 
.. def chain(*iterables):
..     # chain('ABC', 'DEF') --> A B C D E F
..     for it in iterables:
..         for element in it:
..             yield element
.. 
.. 

* `count()` function

.. 
.. 
.. itertools.count(start=0, step=1)¶
.. Make an iterator that returns evenly spaced values starting with n. Often used as an argument to imap() to generate consecutive data points. Also, used with izip() to add sequence numbers. Equivalent to:
.. 
.. def count(start=0, step=1):
..     # count(10) --> 10 11 12 13 14 ...
..     # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
..     n = start
..     while True:
..         yield n
..         n += step
.. When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as: (start + step * i for i in count()).
.. 

* `cycle()` function

.. 
.. itertools.cycle(iterable)¶
.. Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely. Equivalent to:
.. 
.. def cycle(iterable):
..     # cycle('ABCD') --> A B C D A B C D A B C D ...
..     saved = []
..     for element in iterable:
..         yield element
..         saved.append(element)
..     while saved:
..         for element in saved:
..               yield element
.. Note, this member of the toolkit may require significant auxiliary storage (depending on the length of the iterable).
.. 
.. 

* `repeat()` function

.. 
.. 
.. itertools.repeat(object[, times])¶
.. Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified. Used as argument to imap() for invariant function parameters. Also used with izip() to create constant fields in a tuple record. Equivalent to:
.. 
.. def repeat(object, times=None):
..     # repeat(10, 3) --> 10 10 10
..     if times is None:
..         while True:
..             yield object
..     else:
..         for i in xrange(times):
..             yield object
.. 
.. 
.. * Without list!
.. 
