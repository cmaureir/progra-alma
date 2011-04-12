Lecture 9 - Lists
-----------------

.. index:: list

A **list** is an ordered collection of values.

In Python, the data type which represents lists is called
``list``.

How to create a ``list``
~~~~~~~~~~~~~~~~~~~~~~~~

The two main ways to create a list, are:

* use a literal list, with the values in brackets, separated by commas::

    >>> ['hello ' + 'world', 24 * 7, True or False]
    ['hello world', 168, True]
    >>> primes = [2, 3, 5, 7, 11]
    >>> primes
    [2, 3, 5, 7, 11]
    >>> []
    []

* use the ``list`` function applied over an iterable::

    >>> list('hello')
    ['h', 'e', 'l', 'l', 'o']
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list()
    []

``list`` operations
~~~~~~~~~~~~~~~~~~~

* ``len(l)`` return the length of the list;
  i.e. how many elements it has::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> len(colors)
    4
    >>> len([True, True, True])
    3
    >>> len([])
    0

* ``l[i]`` return the ``i``-th value of the list.
  The ``i`` value is called **index** of the value.
  Be careful, because it starts counting from 0
  and not from 1::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> colors[0]
    'blue'
    >>> colors[3]
    'yellow'

  If the ``i`` index indicates an item which is not in the list,
  then an **index error** occurs::

    >>> colors[4]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range

  If the index is negative,
  the item counts from the end backwards::

    >>> colors[-1]
    'yellow'
    >>> colors[-4]
    'blue'

* ``l.append(x)`` adds the ``x`` item to the end of the list::

    >>> primes = [2, 3, 5, 7, 11]
    >>> primes.append(13)
    >>> primes.append(17)
    >>> primes
    [2, 3, 5, 7, 11, 13, 17]

* ``sum(x)`` returns the sum of the list values::

    >>> sum([1, 2, 1, -1, -2])
    1
    >>> sum([])
    0

* ``l1 + l2`` concatenates the lists  ``l1`` and ``l2``::

    >>> list('dog') + [2, 3, 4]
    ['d', 'o', 'g', 2, 3, 4]

* ``l * n`` repeats ``n`` times the ``l`` list::

    >>> [3.14, 6.28, 9.42] * 2
    [3.14, 6.28, 9.42, 3.14, 6.28, 9.42]
    >>> [3.14, 6.28, 9.42] * 0
    []

* ``x in l`` allows to know if the ``x`` item is in the list or not::

    >>> r = list(range(0, 20, 2))
    >>> r
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> 12 in r
    True
    >>> 15 in r
    False

* ``l[i:j]`` allows to obtain a sub-list,
  from the ``i``-th to the ``j``-th items::

    >>> x = [1.5, 3.3, 8.4, 3.1, 2.9]
    >>> x[2:4]
    [8.4, 3.1]

* ``l.count(x)`` counts how many times the ``x`` item
  is in the list::

    >>> list('millimeter').count('i')
    3

* ``l.index(x)`` returns the index of the ``x`` item::

    >>> colors = ['blue', 'red', 'green', 'yellow']
    >>> colors.index('green')
    2
    >>> colors.index('pink')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: 'pink' is not in list

* ``l.remove(x)`` removes the ``x`` item from the list::

    >>> todo = ['visit Paris','plant a tree','learn python','do skydiving']
    >>> todo.remove('learn python')
    >>> todo
    ['visit Paris', 'plant a tree', 'do skydiving']
    >>> todo.remove('learn french')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: list.remove(x): x not in list

* ``l.reverse()`` reverses a list::

    >>> palindrome = = list("No lemon, no melon")
    >>> palindrome
    ['N', 'o', ' ', 'l', 'e', 'm', 'o', 'n', ',', ' ', 'n', 'o', ' ', 'm', 'e', 'l', 'o', 'n']   
    >>> palindrome.reverse()
    >>> palindrome
    ['n', 'o', 'l', 'e', 'm', ' ', 'o', 'n', ' ', ',', 'n', 'o', 'm', 'e', 'l', ' ', 'o', 'N']
    >>> numbers = [1,2,3,4]
    >>> numbers.reverse() 
    >>> numbers
    [4, 3, 2, 1]

* ``l.sort()`` sorts the list::

    >>> numbers = [1,6,3,7,4,2,3,9,6,0]
    ->>> numbers
    [1, 6, 3, 7, 4, 2, 3, 9, 6, 0]
    >>> numbers.sort()
    >>> numbers
    [0, 1, 2, 3, 3, 4, 6, 6, 7, 9]
    >>> friends = ['John','Maria','Joseph','Aron']
    >>> friends
    ['John','Maria','Joseph','Aron']
    >>> friends.sort()
    >>> friends
    ['Aron', 'John', 'Joseph', 'Maria']

List iteration
~~~~~~~~~~~~~~
.. index:: iterable

A list is an **iterable** object.
This means that its values can be traveled using a ``for`` cycle::

    values = [6, 1, 7, 8, 9]
    for i in values:
        print i ** 2

In each iteration of the ``for`` cycle,
the ``i`` variable takes one of the list values,
so this program print the next values:

.. testcase::

    36
    1
    49
    64
    81



Exercises
~~~~~~~~~

#. Consider the next lists::   

    >>> a = [5, 1, 4, 9, 0]   
    >>> b = range(3, 10) + range(20, 23)  
    >>> c = [[1, 2], [3, 4, 5], [6, 7]]   
    >>> d = ['dog', 'cat', 'giraffe', 'elephant']   
    >>> e = ['a', a, 2 * a]   

   Without using the computer,   
   identify which is the result of the next expressions. 
   Next,   
   verify if your answers are correct (use the computer).
   
   * ``a[2]``  
   * ``b[9]``  
   * ``c[1][2]``     
   * ``e[0] == e[1]``
   * ``len(c)``
   * ``len(c[0])``   
   * ``len(e)``
   * ``c[-1]`` 
   * ``c[-1][+1]``   
   * ``c[2:] + d[2:]``     
   * ``a[3:10]``     
   * ``a[3:10:2]``   
   * ``d.index('giraffe')`` 
   * ``e[c[0][1]].count(5)``     
   * ``sorted(a)[2]``
   * ``complex(b[0], b[1])``   

#. The **arithmetic mean**  of the data set is the sum of the values,
   divided by the data amount:
   
   Write a function called ``arithmetic_mean(data)``,
   where ``data`` is a number list,  
   which returns the arithmetic mean of the data:: 
   
    >>> arithmetic_mean([6, 1, 4, 8])    
    4.75    
 
#. The **harmonic mean** of a data set is the reciprocal of the data reciprocal sum,
   multiplied by the amount of data:    

   .. math::   
  
        H = \frac{n}{ 
        \frac{1}{x_1} +   
        \frac{1}{x_2} +   
        \cdots +    
        \frac{1}{x_n} +   
            } 
   
   Write a function called ``harmonic_mean(data)``,  
   which return the harmonic mean of the data::   
   
        >>> harmonic_mean([6, 1, 4, 8])
        2.5945945945945943

#. The **median** of a real data set
   is the set value that provide the same amount of lower and greater
   values to it.
   
   More rigorously,
   the median is defined as follow:
   
   * if the data amount is odd,
     the median is the central value,
     when we order the data from lowest to highest.
   * if the data mount is even,
     the median is the average of the two central values,
     when we order he data from lowest to highest.
   
   Write a function called ``median(data)``,   
   which return the median of the data::
   
        >>> median([5.0, 1.4, 3.2])    
        3.2     
        >>> median([5.0, 1.4, 3.2, 0.1])     
        2.3     
   
   The function should not modify the receive list::
   
        >>> x = [5.0, 1.4, 3.2]   
        >>> median(x)
        3.2     
        >>> x   
        [5.0, 1.4, 3.2]    
        
#. The **mode** of a data set  
   is the most repeated value.
   
   Write a function called ``mode(data)``,     
   where ``data`` is a list, 
   which return a list with the data mode::
   
         >>> mode([5, 4, 1, 4, 3, 3, 4, 5, 0])
         [4]     
         >>> mode([5, 4, 1, 4, 3, 3, 4, 5, 3])
         [3, 4]  
         >>> mode([5, 4, 5, 4, 3, 3, 4, 5, 3])
         [3, 4, 5]

#. A polynomial_ is a mathematical function
   of the form:
   
   .. math::   
   
       p(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots + a_n x^n,   
   
   where `x` is the parameter     
   and `a_0, a_1, \dots, a_n`
   are given real numbers.     
   
   .. _polynomial: http://en.wikipedia.org/wiki/Polynomial
   
   Some polynomial examples are:
   
   * `p(x) = 1 + 2x + x^2`,
   * `q(x) = 4 - 17x`,     
   * `r(x) = -1 - 5x^3 + 3x^5`,  
   * `s(x) = 5x^{40} + 2x^{80}`. 
   
   Evaluate a polynomial    
   means replace `x` by a value
   and obtain the result.     
   For example, if we evaluate the `p` polynomial
   in the value `x = 3`,    
   we obtain the result: 
   
   .. math::   
   
       p(3) = 1 + 2\cdot 3 + 3^2 = 16   
   
   A polynomial can be represented 
   as a list with the values `a_0, a_1, \dots, a_n`.
   For example,
   the previous polynomials
   can be represented in a program as follows::
   
       >>> p = [1, 2, 1]   
       >>> q = [4, -17]    
       >>> r = [-1, 0, 0, -5, 0, 3]    
       >>> s = [0] * 40 + [5] + [0] * 39 + [2]     

   #. Write a function called ``degree(p)``
      which return the degree of a polynomial::
      
       >>> degree(r) 
       5
       >>> degree(s) 
       80     
      
   #. Write a function called ``evaluate(p, x)``   
      which evaluate a ``p`` polynomial
      (represented as a list)    
      in the ``x`` value::  
         
          >>> evaluate(p, 3)  
          16     
          >>> evaluate(q, 0.0)
          4.0    
          >>> evaluate(r, 1.1)
          -2.82347     
          >>> evaluate([4, 3, 1], 3.14)   
          23.2796
         
   #. Write a function called ``polynomial_sum(p1, p2)``    
      which return the sum of two polynomial::     
         
          >>> polynomial_sum(p, r)     
          [0, 2, 1, -5, 0, 3]
         
   #. Write a function called ``polynomial_derivative(p)`` 
      which return the polynomial derivative::
         
           >>> polynomial_derivative(r) 
           [0, 0, -15, 0, 15] 
         
   #. Write a function called ``polynomial_multiplication(p1, p2)``    
      which return the product of two polynomial::
         
           >>> polynomial_multiplication(p, q)     
           [4, -9, -30, -17]     

#. The `Josephus problem`_ is the follow:
   `m` people are in a circle, 
   and are executed in order counting each `n` people;
   the alone person at the end is the survivor.
   For example.
                                                                                                                                     
   with `m = 12` and `n = 3`,
   the survivor is the person 10:                                                                                                                                                             
   .. image:: http://img.thedailywtf.com/images/200907/Josephus.gif

   Write a function which receive the ``m`` and ``n`` parameters,
   and return as result the survivor::

       >>> survivor(12, 3)
       10 
 
   .. _Josephus problem: http://en.wikipedia.org/wiki/Josephus_problem 
