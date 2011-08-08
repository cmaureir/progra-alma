Lecture 19 - Iterators
----------------------

In simple words
an iterator is a type of object which has a method
to advance over a certain data type.
In almost all the cases that method is called `next()`.

The previous idea is very basic and not entirely true,
because in Python most of the iterators
have a lot of methods, built-in, user-defined, etc.

So, iterator objects are used in order to iterate
over an objects data.

For example,
with the content of the previous lectures,
you will now know how to do this in Python using lists::

    >>> my_list = ['a',2,(0,0)]
    >>> for item in my_list:
    ...   print item
    ... 
    a
    2
    (0,0)
	
The previous code iterates over a list object
created by us, printing all the list's items.

According to the previous example,
lists are iterable since you can iterate over them multiple times.

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
method which should be good to be familiarized with.

* `zip()` function

  This function returns a list of tuples,
  taking one-by-one each iterable given as a parameter.
  
  If the sequence of iterable has different lengths,
  the `zip()` function truncates the length to the shortest one.
  
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
  
  
  You can include two optional parameters, the `cmp`, `key` and `reverse`
  which specifies the following characteristics:
  
   * `cmp`: specify a custom comparison function, but with only two arguments,
     which returns a negative, positive or zero number depending on the evaluation
     case. (considering if the first argument is smaller than the second)
   * `key`: specifies a function, with one argument, used to extract a comparison key.
   * `reverse`: specifies a boolean value, which if true, the comparison would be
     performed in reverse order.
  
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
     in a certain phrase. The string data type has a method
     called `split()`, which without parameters splits a string
     by the empty-spaces, for example::
     
         >>> "hello world!".split()
         ['hello', 'world!']
     
     The string data type also has another method called `upper()`
     which allows to change the *case* of an entire string.
     
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
  It is important to know that the sequence of objects must be iterable.
  
  This function returns a tuple with the number and the object,
  starting from 0, if the user does not change this starting point,
  because it is possible adding a new argument called ``start=n``
  where ``n`` is the new starting point.
  
  Look at the following examples::
  
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

  The ``reversed`` function achieves a very simple
  functionality, changes the order, reversing an object
  iterable, this means that it is a good idea to use it
  when you want to start from the end.
  
  The following examples show the function's idea::
  
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
  gives us the possibility to iterate over a certain number of Python objects,
  it does not matter if the objects are `lists`, `tuples`, `strings` etc.
  
  The following examples show their functionality::
  
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

  The idea of the ``count()`` function
  is to start counting numbers from a certain given number
  to the infinite, well, not the infinite, but the
  maximum number's capacity.
  
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
  
  for example, lets imagine we are working into solve
  a certain problem, so we use an iterative method to find the solution,
  you can imagine an infinite iteration until reaching the real solution
  or an approximated value, using different precision::
  
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

  Every programmer more than once time had
  to develop a script which compares a certain
  sequence of elements over another big sequence. In this
  case we need to iterate over a sequence
  and, once it finishes, we need to iterate again.
  The ``cycle()`` function gives us the chance
  to iterate infinite times over a sequence
  to perform any comparison or another
  statement.
  
  For example,
  imagine that you are working
  with Nitrogenous bases in the DNA (A,T, C, G),
  and you are looking for certain pattern over
  a big sequence of DNA.
  The process will be something like this::
  
      for i in cycle('ATCG'):
        do_some_biological_stuff(i)
  
  
  For example,
  lets do a simple program
  which shows the day and number of a month (August, 2011)::
  
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
  the idea is to generate a certain number of elements
  a determinate number of times.
  
  This function requires one parameter,
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

* The *sin* and *cos* mathematical functions can be represented
  using infinite sums:

  .. math::

    \text{sen}(x) =
      \frac{x^1}{1!} -
      \frac{x^3}{3!} +
      \frac{x^5}{5!} -
      \frac{x^7}{7!} +
      \cdots

  .. math::

    \text{cos}(x) =
      \frac{x^0}{0!} -
      \frac{x^2}{2!} +
      \frac{x^4}{4!} -
      \frac{x^6}{6!} +
      \cdots

  * Write the functions called *my_sin()* and *my_cos()*
    which determine the approximation using the previous series.
  
    Remember the factorial definition:
 
    .. math::

        n! = 1\cdot 2\cdot 3\cdot 4\cdot \ldots \cdot n

  * given a list of values for *x*, write a function using
    your previous *my_sin()* and *my_cos()* functions,
    which return tuples with the values `(x,sin(x))`
    (use the *zip()* function)

* You are selected to write a list of all the students of the course,
  the bad news is that the students are not in order, so you need
  to order by *lastname* and *firstname*.

  Also, the generated list must contain tuples with *(number, firstname, lastname)*
  which number is an incremental number.

  Remember the *sorted* and *enumerated* functions.

  The list with the names of the course students is::

      students = [('Lars','Nyman'),
                  ('Diego','Garcia'),
                  ('Katherine','Rivadeneira'),
                  ('Sebastian','Gonzalez'),
                  ('Bernardo','Malet'),
                  ('Rodrigo','Romero'),
                  ('Steven','Conboy'),
                  ('Danilo','Castillo'),
                  ('Jose','Cortes'),
                  ('Alvaro','Orellana'),
                  ('Fernando','Gallardo'),
                  ('Eric','Oñate'),
                  ('Felipe','Daruich'),
                  ('Cristobal','Jara'),
                  ('Leonardo','Aravena'),
                  ('Jaime','Guarda'),
                  ('Valentin','Medina'),
                  ('Sergio','Otárola'),
                  ('Alex','Delgado'),
                  ('Nicolas','Peña'),
                  ('Juan Pablo','Garcia'),
                  ('Claudio','Follert'),
                  ('Alvaro','Quintana'),
                  ('Mauricio','Morales')]

..      students = [('Ruediger','Kneissl'),
..                  ('Jose','Velasquez'),
..                  ('Hector','Alarcon'),
..                  ('Luis','Cortez'),
..                  ('Juan','Cortes'),
..                  ('Vilaro','Vila'),
..                  ('Pedro','Campana'),
..                  ('Jorge','García'),
..                  ('Alejandro','Barrientos'),
..                  ('jorge','ramirez'),
..                  ('Cristian','Lopez'),
..                  ('Leonardo','Bustos'),
..                  ('Jorge','Castillo'),
..                  ('Itziar','de Gregorio'),
..                  ('Carlos','Gonzalez'),
..                  ('Rodrigo','Guarda'),
..                  ('Lewis','Knee'),
..                  ('Fernando',Morales'),
..                  ('Edward','Ormeno'),
..                  ('German','Ortiz'),
..                  ('Matias','Radiszcz'),
..                  ('Jorge','Ramirez',
..                  ('Mark','Rawlings')]

      


  So the result must be::

      >>> student_list(students)
      (0,'Hector','Alarcon')
      (1,'Alejandro','Barrientos')
      ...  

* Write a function which return the total
  price of different elements list::

      >>> fun = {'kindle':139, 'ps3':297.30, 'led':799.99}
      >>> clothe = {'jeans':26.24, 't-shirt':14.99, 'boots':40.00}
      >>> services = {'water':20.00, 'light':42.70, 'internet':51.31}
      >>> total_price(fun,clothe,services)
      1431.53 USD

  Use the *chain()* iterator.
