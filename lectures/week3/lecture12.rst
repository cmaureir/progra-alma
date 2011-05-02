Lecture 12 - Tuples
-------------------

.. index:: tuple

A **tuple** is a sequence of grouped values.

A tuple is used to group several related values as a single value.

The data type that represents the tuple is called ``tuple``.
The ``tuple`` type is immutable: a tuple cannot be modified once created.

.. index:: tuple literal

A tuple can be created
setting comma separated values and in round brackets.
For example,
we can create a tuple with the first-name and last-name of a person::

    >>> person = ('John', 'Smith')
    >>> person
    ('John', 'Smith')

Unpacking tuples
~~~~~~~~~~~~~~~~

.. index:: unpacking

The tuple values can be recovered assigning the tuple to the corresponding variables.
This is called **unpacking tuples**::

    >>> person = ('John', 'Smith')
    >>> name, surname = person
    >>> name
    'John'

If you try to unpack the wrong number of values,
a value error occurs::

    >>> a, b, c = person
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 2 values to unpack

Also, it is possible to extract the values using their index::

    >>> person[1]
    'Smith'

``tuple`` comparison
~~~~~~~~~~~~~~~~~~~~~~

Two tuples are the same
when they have the same size
and each of their items have the same value::

    >>> (1, 2) == (3 / 2, 1 + 1)
    True
    >>> (6, 1) == (6, 2)
    False
    >>> (6, 1) == (6, 1, 0)
    False

.. index:: lexicographic order

To determine if a tuple is smaller than other,
the rule called **lexicographic order** is used.
If the items in the first position from both tuples are different,
comparing them determines the order of the tuples::

    >>> (1, 4, 7) < (2, 0, 0, 1)
    True
    >>> (1, 9, 10) < (0, 5)
    False

The first comparison is  ``True`` because ``1 < 2``.
The second comparison is ``False`` because ``1 > 0``.
No matter the value of the following values
or if a tuple has more elements than the other.

If the first position items are the same,
then the same comparison is used with the next value::

    >>> (6, 1, 8) < (6, 2, 8)
    True
    >>> (6, 1, 8) < (6, 0)
    False

The first comparison is  ``True`` because ``6 == 6`` and ``1 < 2``.
The second comparison is ``False`` because ``6 == 6`` and ``1 > 0``.

If the respective items continue being the same,
we continue comparing with the next values.
If a tuple runs out of items to compare before the other,
then it is immediately smaller than the other::

    >>> (1, 2) < (1, 2 ,4)
    True
    >>> (1, 3) < (1, 2, 4)
    False

The first comparison is ``True`` because ``1 == 1``, ``2 == 2``
and, at this point, all the elements from the first tuple have been compared.
The second comparison is ``False`` because ``1 == 1`` and ``3 < 2``;
in this case, it does reach the outcome before any of the tuples run out of elements.

This comparison method is the same used to sort words in alphabetic order.
(for example, in directories and dictionaries)::

    >>> 'car' < 'carousel'
    True
    >>> 'car' < 'cars'
    True
    >>> 'mon' < 'month' < 'monthly'
    True


Typical tuple uses
~~~~~~~~~~~~~~~~~~

The tuples are used everytime that is needed to group values.
Usually, real world concepts are represented as tuples that
group information on them.
For example,
A football match can be represented
as a tuple of the opposing teams::

    match1 = ('Milan', 'Bayern')

To represent plane points,
is possible to use two element tuples ``(x, y)``.
For example, we can create a function called ``distance``
which receive two points and return the distance between them::

    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        return (dx ** 2 + dy ** 2) ** 0.5

When the function is called, is necesary to give two tuples::

    >>> a = (2, 3)
    >>> b = (7, 15)
    >>> distance(a, b)
    13.0

Usually the dates are represented as tuples
grouping the year, month and the day.
The advantage of use the previous order (year first)
is that the relational operation allow to know the order
of the dates::

    >>> today = (2011, 4, 19)
    >>> yesterday = (2011, 4, 18)
    >>> christmas = (2011, 12, 25)
    >>> new_year = (2012, 1, 1)
    >>> today < yesterday
    False
    >>> today < christmas < new_year
    True

A tuple can contain another tuples.
For example,
a person can be described by his name, his ID and his birth day::

    person = ('John Smith', '12345678-9', (1980, 5, 14))

In this case,
the data can be unpacking like this::

    >>> name, ID, (y, m, d) = person
    >>> m
    5

Sometimes one is interested only one of the tuple values.
To avoid create innecesary variables,
usually is possible to assign this values to the ``_`` variable.
For example, if only is necessary to know the month of the birth,
we can obtain it as follow::

    >>> _, _, (_, month, _) = person
    >>> month
    5

A data table usually is represented as a tuple list.
For example,
the student information from a course,
can be represented as follow::

    students = [
        ('James', 'Smith', '201199001-5', 'Civil'),
        ('Joseph', 'Jones',      '201199002-6', 'Electrical'),
        ('Joseph', 'Jones',      '201199003-7', 'Mechanics'),
    ]

In this case, the tuple can be unpacked automatically iterating
the list with a ``for`` cycle::

    for firstname, lastname, ID, carrer in students:
        print firstname, 'study', carrer

Is possible to create tuples of a fixed length,
for example one, leaving only the comma next to the unique value::

    >>> t = (12,)
    >>> len(t)
    1

In other languages, the tuples receive
the name of **register**.
This name is common, so is convenient to know it.

Tuples iteration
~~~~~~~~~~~~~~~~

Like the lists, the tuples are iterables::

    for value in (6, 1):
        print value ** 2

Furthermore,
is possible to convert a tuple in a list
using the ``list`` function,
and is possible to convert a list in a tuple using the
``tuple`` function::

    >>> a = (1, 2, 3)
    >>> b = [4, 5, 6]
    >>> list(a)
    [1, 2, 3]
    >>> tuple(b)
    (4, 5, 6)

Exercises
~~~~~~~~~

#. In the card games, a card has two attributes:
   a value (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q o K) and
   a suit (♥, ♠, ♦ o ♣).     
     
   In a program, a card can be represented as a tuple
   of two elements: the value and the suit.
   The value is a number from 1 to 13, and the suit is a string ('H', 'C', 'S' or 'D').
     
   A hand can be represented as a set of cards.
   For example, we can represented the hand 5♣ 2♥ 1♠ Q♥ K♣ as the next way:
     
   ::   
     
       hand = {(5, 'C'), (2, 'H'), (1, 'S'), (12, 'H'), (13, 'C')}  
     
   In the `Carioca`_ a straight is a hand with four cards which have the same suit and have consecutive values.
     
   .. _Carioca: http://en.wikipedia.org/wiki/Carioca_(card_game)

   For example:     
     
   * 3♥ 6♥ 5♥ 4♥ is a straight, because all the card have the suit ♥ and their consecutive values
     are from 3 to 6.
   * 3♣ 6♦ 5♦ 4♥ is not a straight, because the cards have different suits.  
   * 3♣ A♣ J♣ 5♣ is not a straight, because the values are not consecutive.
   * 3♠ 4♠ 5♠ is not a straight, because the hand does not have four cards.
     
     
   Write a function called *is_straight(hand)* which indicates if the hand is or not a straight.
  
   ::   
   
        >>> is_straight({(3,'C'), (6, 'C'), (5, 'C'), (4, 'C')})  
        True    
        >>> is_straight({(3,'T'), (6, 'D'), (5, 'D'), (4, 'C')})  
        False   
        >>> is_straight({(3,'T'), (1, 'T'), (11, 'T'), (5, 'T'))  
        False   
        >>> is_straight({(3,'C'), (4, 'C'), (5, 'C')})
        False    

#. In the card games, a card have two attributes:
   a value (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)     
   and a suit (♥, ♦, ♣, ♠).     
   
   In a program, the value can be represented by a number between 1 and 13,
   and the suit like a string:    
   ♥ → ``'H'``,
   ♦ → ``'D'``,
   ♣ → ``'C'`` and     
   ♠ → ``'S'``.
   
   A card can be represented as a tuple of two elements, the value and the suit::
 
      card1 = (5, 'C')   
      card2 = (10, 'D')  
   
   To simplify, the ace can be represented as the number 1, 
   and the J, Q and K cards as  11, 12 and 13:: 
   
      # ace of spades and heart queen    
      card3 = (1, 'S')   
      card4 = (12, 'H')  
   
   In the poker game,
   a hand have five cards,
   which in a program could be a set of five tuples::
   
       hand = {(1, 'S'), (1, 'H'), (1, 'C'), (13, 'D'), (12, 'S')}   
   
   #. A *full* is a hand in which three cards must have a common value,
      and the other two cards has another common value.
      Write a function which indicates if the hand is or not a full::
         
          >>> hand_1 = {(1, 'S'), (1, 'H'), (6, 'C'), (1, 'D'), (6, 'D')}     
          >>> hand_2 = {(2, 'C'), (1, 'H'), (12, 'H'), (1, 'D'), (6, 'D')}    
          >>> is_full(hand_1) 
          True     
          >>> is_full(hand_2) 
          False   
   
   #. A *color* is a hand in which all the cards have the same suit.
      Write a function which indicates if the hand is a color or not::
         
       >>> hand_1 = {(8, 'S'), (13, 'S'), (4, 'S'), (9, 'S'), (2, 'S')}
       >>> hand_2 = {(12, 'C'), (1, 'H'), (5, 'H'), (2, 'H'), (2, 'D')}
       >>> is_color(hand_1)
       True    
       >>> is_color(hand_2)
       False   
   
   #. A *straight* is a hand in which the cards have consecutive values
      (for example: 5, 6, 7, 8 y 9).   
      Write a function which indicates if the hand is or not a straight::   
         
       >>> hand_1 = {(4, 'S'), (7, 'H'), (3, 'H'), (6, 'C'), (5, 'C')}     
       >>> hand_2 = {(12, 'C'), (7, 'H'), (3, 'H'), (12, 'H'), (5, 'C')}   
       >>> is_straight(hand_1)   
       True    
       >>> is_straight(hand_2)   
       False   
   
#. The dates can be represented as tuples ``(year, month, day)``.    
   
   To associate each person with his birth day,   
   you can use a dictionary::
   
        >>> n = {     
        ...     'Peter': (1990, 10, 20),     
        ...     'Anna': (1992, 3, 3), 
        ...     'Fran': (1989, 10, 20),   
        ...     'Alice': (1989, 12, 8),
        ...     'Joan': (1991, 2, 14),    
        ... }   
   
   #. Write a function called ``same_day(date1, date2)``     
      that indicates if both dates occur the same day of the year
      (consider different years)::   
      
          >>> same_day((2010, 6, 11), (1990, 6, 11)) 
          True    
          >>> same_day((1981, 8, 12), (1981, 5, 12)) 
          False   
   
   #. Write a function called ``older(n)``
      that indicates how is the older person,
      verifying the birth day in the ``n`` dictionary::
   
          >>> older(n)    
          'Fran'    
   
   #. Write a function called ``first_birthday(n)``  
      which indicates how is the person that have the first birthday
      of the year::
   
          >>> first_birthday(n)
          'Joan'    

#. A line (or straight line) in the Euclidean plane is described by the equation:
   
   .. math::   
   
       y = mx + b,   
   
   where `m` is the *slope* (or gradient)  
   and `b` is the *y-intercept*.     
   All the line points satisfied the equation.
   
   In a program,   
   a line can be represented as a tuple ``(m, b)``.    
   
   The algorithms to solve the next equation are very simple,
   if you do not remember,,     
   you can search it in your favorite math book or in internet.
   
   #. Write a function called ``point_in_line(p, r)`` 
      which indicates if the ``p`` point is in the ``r`` line::   
         
          >>> line = (2, -1) 
          >>> point_in_line((2, 3), line)     
          True    
          >>> point_in_line((0, -1), line)    
          True    
          >>> point_in_line((1, 2), line)     
          False   
   
   #. Write a function called ``are_parallel(r1, r2)``
      which determine if two lines ``r1`` and ``r2`` are parallel,
      i.e., do not intersect at any point. 
   
   #. Write a function called ``line_through(p1, p2)`` 
      which return the line that through the ``p1`` and ``p2`` points::
   
          >>> line_through((-2, 4), (4, 1))     
          (-0.5, 3.0)   
   
      You can verify if the function is correct with the previous function ``point_in_line(p,r)``::
   
           >>> p1 = (-2, 4)    
           >>> p2 = (4, 1)     
           >>> r = line_through(p1, p2)    
           >>> point_in_line(p1, r) 
           True    
           >>> point_in_line(p2, r) 
           True    
   
   #. Write a function called ``point_of_intersection(r1, r2)``    
      which return the point where the two lines intersect:: 
         
          >>> r1 = (2, 1)     
          >>> r2 = (-1, 4)    
          >>> point_of_intersection(r1, r2)     
          (1.0, 3.0)    
         
      If the lines are parallel,
      the function must return ``None``.

  
#. For this problem, consider the following characteristics of a person:

   * Name,
   * Sex (male or female),
   * Age,
   * Favorite music, and
   * zodiacal sign.                                                                                                                  
   
   In the program to do, a person will be represented as a tuple::
   
       person_1 =    ('Peter', 'M', 27, 'rock', 'leo') 
       person_2 =    ('Anna', 'F', 23, 'cumbia', 'virgo')                                                                                                                   
   
   Two  people are compatible if:
   
   * Are of opposite sex (man and women),
   * under 10 years of age difference,
   * like the same music, and
   * their zodiac sign are compatible.
      
   To find out which signs are compatible,
   there is a set ``compatible_signs``
   tuples having ``(woman_sign,men_sign)``,
   that `you can download here`_.
   If a tuple is in the set, means that the signs are compatible.
   
       >>> ('aries', 'taurus') in compatible_signs
       True
   
   #. means that Aries women
   #. is compatible with Taurus man.                                                                                                                                          
   
       >>> ('capricorn', 'libra') in compatible_signs
       False
   
   #. It means that women Capricorn
   #. is not compatible with free men. 
   
   Write a function ``compatibles(p1, p2)``, to indicate
   if two people are compatible or not.
    
      .. _you can download here: ../../_static/programs/signs.py
