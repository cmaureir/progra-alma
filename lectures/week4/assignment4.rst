Assignment 4
============

#. To do this assignment,
   you must download `the module with the data`_
   that we will use.
   
   .. _the module with the data: ../../_static/programs/people.py
   
   For use the module you have to save them in the same folder
   that you will use from the pyscripter,
   and import the data as following::
   
       from people import *
  
   this module contains a list called ``people`` which contain tuples,
   which represent the data of a people.
   Each tuple has three values: name, last name and date of birth.

   The name and last name are strings,
   and the date of birth is a tuple of three values: day, month and year.

   For example, we can see the data of the first person::
 
       >>> people[0]
       ('martin', 'soto', (24, 8, 1990))

   #. Write a function which print the name of all the people.
      For these, it is necessary to pass through the list with a ``for`` statement,
      getting the name of the person and printing it using the ``print`` statement.
      The function do not need to return nothing::
      
          >>> names(people)
          martin
          gabriel
          humberto
          sebastian
          victor
          ...
          horacio
          ignacio
          nicolas
          pablo
          rolando
          ricardo
     
   #. Write a function which print the date of birth of all the people::
      
        >>> dates(people)
        August 24th, 1990
        June 2nd, 1974
        November 4th, 1973
        September 18th, 1973
        August 12th, 1992
        ...
        August 18th, 1981
        April 24th, 1972
        May 17th, 1977
        February 4th, 1972
        January 29th, 1976
   
      To do this easier, build a dictionary with the names of the months::
    
        months = {
            1: 'January',
            2: 'February',
            # ...
            12: 'December',
        }
    
   #. Do a function called *how_many_people(list)* to determinate
      the amount of people in the list.

   #. Write a function which return a list of people which has their birthday
      the same day that you have::

        >>> my_birthday(people)
        ['jonathan sepulveda']
   
   #. Do a function called *repeated_birthdays(list)* that can
      determinate the number of people in the list who have their birthday the same day.

   #. Do a function called *most_common_name(list)* capable to determinate
      the repeated name on the list of people.
   
   #. Do a function called *younger_older(list)* to determinate the younger and older people
      of the list.
