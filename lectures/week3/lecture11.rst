Lecture 11 - Dictionaries
-------------------------

.. index:: dictionary

A **dictionary** is a data type that allows to associate value pairs.

.. index:: key (dictionary), value (dictionary)

A dictionary can be seen
as a **key** collection,
each one having an associated **value**.
The keys are disordered
and there are no repeated keys.
The only way to access a value
is through their key.

How to create a ``dictionary``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main way to create a dictionary is using a literal dictionary.
The key is associated to a value using two points (colon)::

    >>> telephones = {'John': 5552437, 'Andy': 5551428, 'Shane': 5550012}

In this example,
the keys are ``'John'``, ``'Andy'`` and ``'Shane'``,
and the associated values to them are,
``5552437``, ``5551428`` and ``5550012`` respectively.

An empty dictionary can be created using ``{}`` or with a function called ``dict()``::

    >>> d = {}
    >>> d = dict()

How to use a ``dictionary``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The associated value to the ``k`` key in the ``d`` dictionary
can be obtained through ``d[k]``. ::

    >>> telephones['John']
    5552437
    >>> telephones['Andy']
    5551428

If the key is not present in the dictionary,
a **key error** (``KeyError``) occurs::

    >>> telephones['Nancy']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Nancy'

It is possible to add new keys simply assigning them to a value::

    >>> telephones['Peter'] = 4448139
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 5551428, 'Shane': 5550012}

Note that the order in which the keys are stored in the dictionary
is not necessarily the same order they were added.

If you assign a value to a key that is already present in the dictionary,
the previous value is overwritten.
Remember that a dictionary cannot have repeated keys::

    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 5551428, 'Share': 5550012}
    >>> telephones['Andy'] = 4448139
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 4448139, 'Share': 5550012}

The values can be repeated.
In the previous example, Andy and Peter have the same number.

To remove a key, you can use the statement ``del``::

    >>> del telephones['Share']
    >>> telephones
    {'John': 5552437, 'Peter': 4448139, 'Andy': 4448139}

If you use a dictionary in a ``for`` cycle, 
in each iteration a key is obtained::

    >>> for k in telephones:
    ...     print(k)
    ...
    John
    Peter
    Andy

To iterate over the keys, use ``d.values()``::

    >>> for v in telephones.values():
    ...     print(v)
    ...
    5552437
    4448139
    4448139

It is also possible to create a list of keys or values::

    >>> list(telephones)
    ['John', 'Peter', 'Andy']
    >>> list(telephones.values())
    [5552437, 4448139, 4448139]

``len(d)`` return how many key-value pairs are in the dictionary::

    >>> numbers = {15: 'fifteen', 24: 'twenty-four'}
    >>> len(numbers)
    2
    >>> len({})
    0

``k in d`` allows to know if the key ``k`` is in the dictionary ``d``::

    >>> legs = {'cat': 4, 'human': 2, 'octopus': 8, 'dog': 4, 'centipede': 100}
    >>> 'dog' in legs
    True
    >>> 'worm' in legs
    False

To know if a key *is not* in the dictionary, it
is possible to use the ``not in`` statement::

    >>> 'worm' not in legs
    True

Exercises
~~~~~~~~~~


#. Consider the following assignations::   

       >>> a = {'a': 14, 'b': 23, 'c': 88}   
       >>> b = {12: True, 55: False, -2: False}    
       >>> c = dict()
       >>> d = {1: [2, 3, 4], 5: [6, 7, 8, 9], 10: [11]} 
       >>> e = {2 + 3: 4, 5: 6 + 7, 8: 9, 10: 11 + 12}   

   Without using the computer, determine the result of the following
   expressions.
   Once you finish, verify your answers with the computer.
   
   * ``a['c']``
   * ``a[23]`` 
   * ``23 in a``     
   * ``'a' in a``    
   * ``5 in d[5]``   
   * ``sum(b)``
   * ``len(c)``
   * ``len(d)``
   * ``len(d[1])``   
   * ``len(b.values())``   
   * ``len(e)``
   * ``sum(a.values())``   
   * ``max(list(e))``
   * ``d[1] + d[5] + d[10]``     
   * ``max(map(len, d.values()))``   


#. Write a program that allow to save the age of several differente people,
   saving algo their names.
   It is recommended the use of a *dictionary*.     
   
   Once you have several ages, obtain a list with only the age of the people,
   and look for the more repeated one,
   when you obtain that age, show the name of the people
   with that age.
   
   ::    
   
       >>> add("John Smith",25)    
       >>> add("Carl Hoffmann",18)   
       >>> add("Joseph Sandler",21)     
       >>> ... 
       >>> add("Michael Jackson",18)     
       >>> repeated_age() 
       18
       >>> show(18)     
       Carl Hoffmann   
       ...     
       Michael Jackson 


#. A telephone directory is structured using only two parameters, the
   *name* and the *telephone*.
   
   Write a program that allow the same functionallity,
   i.e., add entries, search some number, remove somo entry and
   show all the content.
   
   To do an easiest implementation, is recommendable to use
   *dictionaries* and *functions*.
   
   The behavior of the functions must be:
   
   ::    
   
       >>> add_telephone("John Smith",123456) 
       Contact added.  
       >>> view_directory()
       "John Smith" 123456     
       >>> add_telephone("Mary Poppins",912354) 
       Contact added.  
       >>> view_directory()
       "John Smith" 123456     
       "Mary Poppins" 912354
       >>> search("John Smith")
       "Fulano Perez" 123456     
       >>> buscar("John Rambo")  
       Contact not found. 

#. Write a function called  *count_initials(phrase)* 
   which return a dictionary with characters as *key* 
   and the associated value to the *key* must be the initial of each
   word:
   
   ::    
   
       >>> count_initials('The elephant is moving to Asia')   
       {'t': 2, 'e': 1, 'i':1, 'm':1, 'a': 2}  
       >>> count_initials('Several seeds see the sea')   
       {'s': 4', 't': 1}   
      
   
#. The ``countries`` dictionary associated each person
   with the set of the visited countries::
   
     countries = {    
     Peter': {'Chile', 'Argentina'},  
     Jenny': {'France', 'Switzerland', 'Chile'}, 
     John': {'Chile', 'Italy', 'Francia', 'Peru'},
     ... 
       } 
   
   Write a function called ``how_many_in_common(a, b)``, 
   which indicates how many countries in common are visited
   by the person ``a`` and ``b``::
   
       >>> how_many_in_common('Peter', 'John')
       1 
       >>> how_many_in_common('John', 'Jeny')
       2 
 
#. Write a function ``even_keys(d)``     
   which indicates if the ``d`` dictionary has some even number as key.
   
   Next, write a function called ``even_values(d)``
   which indicates if the ``d`` dictionary has some even number as value.
   
   To try your functions, use dictionaries whose keys and values are only
   integer numbers::
   
       >>> d1 = {1: 2, 3: 5}     
       >>> d2 = {2: 1, 6: 7}     
       >>> even_values(d1) 
       True    
       >>> even_values(d2) 
       False   
       >>> even_keys(d1)  
       False   
       >>> even_keys(d2)  
       True    

#. Write a function called ``max_pair(d)``     
   which return the maximum value of the sum
   between the key and the value of
   the ``d`` dictionary::
   
       >>> d = {5: 1, 4: 7, 9: 0, 2: 2}
       >>> max_pair(d)   
       11   

#. Write a function called ``invert(d)`` 
   which return a dictionary whose keys are the values of ``d``    
   and whose values are the keys::
   
       >>> invert({1: 2, 3: 4, 5: 6})
       {2: 1, 4: 3, 6: 5}  
       >>> nicknames = {
       ...   'Suazo': 'Chupete', 
       ...   'Sanchez': 'Maravilla',   
       ...   'Medel': 'Pitbull', 
       ...   'Valdivia': 'Mago', 
       ... }   
       >>> invert(nicknames)
       {'Maravilla': 'Sanchez', 'Mago': 'Valdivia', 'Chupete': 'Suazo', 'Pitbull': 'Medel'}  

 
#. Actually a widely used method to choose a password is change
   some characters of a certain word by numbers, for example: 
   
   ::    
       I like football 
   ::    
       1 l1k3 f00tb4ll
   
   Therefore, to do more easy this task, write a function that using:
   
   * una phrase.
   * un dictionary with the characters to replace.
   
   can return the password with the new characters.
   
   Remember the *replace()* function.    
   
   ::    
       phrase = "I want my password, now!"  
       d = {'a':4,'o':0,'!':'?'}   
       change(phrase,d)  
       "I w4nt my p4ssw0rd, n0w?"
   
   ::    
       phrase = "cute kitty"   
       d = {'e':3,'i':1}  
       change(phrase,d)  
       "cut3 k1tty"   
   
   Also, because we need a more secure password, change the previous functions to change the
   characters of the phrase only a certain number of times.
   
   For example::     
   
       phrase = "my house is orange"    
       d = {'a':4,'o':0,'i':1,'e':3}     
       change(phrase,d,1)     
       "my h0us3 1s or4nge"    
       change(phrase,d,2)     
       "my h0us3 1s 0r4ng3"    
