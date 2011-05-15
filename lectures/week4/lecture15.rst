Lecture 15 - Use of objects and Files
-------------------------------------

In Python, the **objects** are abstraction for data.
All the data inside a Python program is represented by objects,
or in some cases, by relations between two or more objects.
We are saying that all the basic elements like `integers`, `functions`,
`strings`, `dictionaries`, and so on, they are all objects,
notoriously they have certain things in common.

About the objects
~~~~~~~~~~~~~~~~~

The idea of this lecture is to understand
the idea behind the objects, but all the
*Object Oriented Paradigm* will be
study with more detail in the next lectures.

An *object* is an instance of a *class*,
the most simple example to understand this,
is to think in a class called ``Human``,
and all of us are instances, because we are all
human beings. In the same way, a *class* 
have several functions, called *methods*.
In our example, as Human, we can *walk*, *speak*,
*run*, etc, so we as objects, can use that
methods, because we can speak, walk, etc.

Several functions that you used,
create objects of different types,
like *bool()*, *dict()*, *float()*,
*int()*, *list()*, *set()*, *tuple()*, *str()*,
etc.

The idea of the previous methods,
is convert objects in another types,
for example::

    >>> a = 4
    >>> b =float(a)
    >>> b
    4.0
    >>> b = b + 0.3
    >>> b
    4.3
    >>> c = int(b)
    >>> c
    4
    >>> bool(c)
    True
    >>> c = c - c
    >>> c
    0
    >>> bool(c)
    False

Also between objects like, *lists*, *sets*,
*tuples* and *dictionaries*::

    >>> a = (1,2)
    >>> type(a)
    <type 'tuple'>
    >>> b = set(a)
    >>> b
    set([1, 2])
    >>> a
    (1, 2)
    >>> type(b)
    <type 'set'>
    >>> d = list(b)
    >>> d
    [1, 2]
    >>> e = dict([[1,'one'],[2,'two']])
    >>> e
    {1: 'one', 2: 'two'}
    >>> type(e)
    <type 'dict'>
    >>> set(e)
    set([1, 2])
    >>> list(e)
    [1, 2]


The object, as you saw in the previous lectures,
have several useful methods, which can be executed
as following::

    object.method()

So, the previous examples about *lists*, *sets*,
*tuples* and *dictionaries* like::

    a = [1,3,2]
    >>> a.sort()
    >>> a
    [1, 2, 3]


Files
~~~~~

Every data used by a program during it execution are in their variables,
which are stored in the RAM memory of the computer.

The RAM memory is a volatile storage element: when the program is finished,
or when the computer turn off, all the data is lost forever.

For a program can save the data permanently, is necessary to use a persistent storage medium,
which the most important is the hard-drive.

The hard-drive data is organized in files.
A file is a data sequence saved in a persistent medium, available to being used
by another program.

All the files has a name and location inside the file system
of the same Operating System.

The data file is present after the program, which write the file, is finished.

A program can save their data in files to used in a future execution,
also can read the data from data-files created by others programs.

A program can not manipulate directly the data in another file.
To use a file, a program always must open a file and allocate it to a variable,
which is called logic-file.

All the operations over a file, performed through the logic-file.

Depending of the content, there are many file-types.
We will work with the file-text,
which contain text, and can be opened and modified using
a text-editor, like Notepad.
The text-file generally has names finishing with a ``.txt``.

Work with a file is a nightmare in some programming languages,
but is very simple in Python.

First of all, you must know that an instance of a file
inside a program or script is an object (logic-file), so like all the
objects, has some very useful methods.

To explain the files behaviour in Python, we will consider
the next file, called `data.txt`_.

::

    Hello first line!
    Oh! the second line
    The next line is very boring
    1,-234.5,45.8,ok
    Final line :)

.. _`data.txt`: ../../_static/data.txt


**Opening** a file is very easy:

::

    my_file=open('data.txt','r')

Now ``my_file`` is an object that is
an instance to access to the `data.txt` file.

But, what is the *'r'* statement?
The second parameter of the **open()** method 
specify the *mode* when the file is opened.
Some useful modes are:

* *r*, ``read-only`` mode,
* *w*, ``write-only`` mode,
  if the file exist will be overwrited,
* *a*, ``append`` mode.

If you do not give any mode,
the default mode is ``read-only``.

There are different ways to **Read** a file,
but now we will focus on three methods,
``read()``, ``readline()`` and ``readlines()``.

The ``read()`` method, return the entire content
of the file, for example::

    >>> my_file=open('data.txt','r')
    >>> content = my_file.read()
    >>> print content
    Hello first line!
    Oh! the second line
    The next line is very boring
    1,-234.5,45.8,ok
    Final line :)

    >>> new_content = my_file.read()
    >>> print new_content
    
    >>>

The ``content`` variable contain all the information
of the file.

But, what happened with the ``new_content`` variable?
is empty!. This is because when you open a file
a ``pointer`` is positioned at the beginning of the file,
and when you read the file, the pointer moves forward,
so with the first call of the ``read()`` method,
the pointer reach the end of the file, so in the next
call of the ``read()`` method, there is no more
content to read, that is the reason to have an
empty variable called ``new_content``.

If you want to move backwards and forwards inside a file
you need to read about the `seek()`_ method.

.. _`seek()`: http://docs.python.org/library/stdtypes.html#file.seek

The ``readline()`` method, return only one line of the file,
for example::

    >>> my_file=open('data.txt','r')
    >>> my_file.readline()
    'Hello first line!\n'
    >>> my_file.readline()
    'Oh! the second line\n'
    >>> my_file.readline()
    'The next line is very boring\n'
    >>> my_file.readline()
    '1,-234.5,45.8,ok\n'
    >>> my_file.readline()
    'Final line :)\n'
    >>> my_file.readline()
    ''
    >>> 

You can also assign a line to a variable::

    >>> my_file=open('data.txt','r')
    >>> simple_line = my_file.readline()
    >>> print simple_line
    'Hello first line!\n'

The ``readlines()`` method, return a list with all 
the lines in the file, for example::

    >>> my_file=open('data.txt')
    >>> my_file.readlines()
    ['Hello first line!\n', 'Oh! the second line\n', 'The next line is very boring\n', '1,-234.5,45.8,ok\n', 'Final line :)\n']

To obtain strings without the ``\n``,
can use the **strip** method,
which remove all the space symbols from the beginning
to the end::


   >>> s = '   Hello\n'
   >>> s.strip()
   'Hello'


So, if you remember the `list`_ lecture
you can iterate over a list to work with each element::

    >>> my_file=open('data.txt')
    >>> for line in my_file.readlines():
    ...    print line
    ... 
    Hello first line!
    
    Oh! the second line
    
    The next line is very boring
    
    1,-234.5,45.8,ok
    
    Final line :)
    
    >>> 

.. _`list`: ../week3/lecture9.html

Is very annoying to had blank lines
between each line, to avoid this
you need to add a comma to the print line,
like this::

    >>> my_file=open('data.txt')
    >>> for line in my_file.readlines():
    ...    print line,
    ... 
    Hello first line!
    Oh! the second line
    The next line is very boring
    1,-234.5,45.8,ok
    Final line :)
    >>> 


We will look two method to **Write**
a file, using the ``write()`` and the ``writelines()``
method.

The ``write()`` method allow to write a string
inside the file, for example::

    >>> my_file=open('data2.txt','w')
    >>> my_file.write('test content\n')
    >>> my_file.close()
    >>> 
    localhost~> cat data2.txt 
    test content
    


The ``writelines()`` method allow to write
several lines inside the file, this is possible
giving a list as parameter to the method,
for example ::

    >>> my_file=open('data2.txt','w')
    >>> my_list=['first line\n','second line\n','final line\n']
    >>> my_file.writelines(my_list)
    >>> my_file.close()
    >>> 
    localhost~> cat data2.txt 
    first line
    second line
    final line

If you want to *close* a file,
the function is called ``close()``.

::

    my_file.close()



Objects characteristics (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every object have three main characteristics:

* An identity (unique and unchangeable), that is an integer returned by ``id(<object>)`` method.::

    >>> number = 13
    >>> id(number)
    163098656
    >>> name = 'carl'
    >>> id(name)
    3075656576L

* A type (unchangeable), that is returned by ``type(<object>)`` method::

    >>> number = 13
    >>> type(number)
    <type 'int'>
    >>> name = 'carl'
    >>> type(name)
    <type 'str'>

* A value, saved in the assignment process::

    >>> number = 13
    >>> number
    13
    >>> name = 'carl'
    >>> name
    'carl'

If you change the value of a variable, the identity will change is almost all the cases.::

    >>> number = 12
    >>> id(number)
    163098668
    >>> number += 1
    >>> id(number)
    163098656

Some objects do not allow to change their content, because are immutable like the tuples
(See lecture10_ for more details)

.. _lecture10:  ../week3/lecture10.html

The idea of the **type** of an object is know some details from it,
the methods they have, the bytes of memory that use, etc.

The **name** of an object is different,
is not a property itself, because the object
does not know their name.
An object can have several names or not have a name,
so they live only in the namespace
(Namespace, collection of name and object references pairs).

To clarify this idea,
lets see this simple line::

   >>> variable = 42

this means that we are adding the name 'variable' in our namespace,
making it refer to an integer object with the value '42'.

You can assign a new object reference to a name,
simple adding a new value in your code,
for example::

    >>> variable = 42
    >>> variable = 'hello'

First, we add the name ``variable`` to the local namespace,
making it refer to a integer object with the value 42,
and in the next line, we making it point to a string
with the value ``hello``.


Exercises
~~~~~~~~~

.. Para cada alumno en el archivo ``alumnos.txt``,
.. crear un archivo llamado ``nombre-apellido.txt``
.. que sea una carta para el alumno
.. con el siguiente contenido:
.. 
.. .. code-block:: none
.. 
..     Estimado [nombre],
..     usted ha [aprobado/reprobado]
..     con promedio [p].
.. 
.. Por ejemplo,
.. la carta para Marcelo Bielsa
.. se llamará ``marcelo-bielsa.txt``
.. y su contenido será:
.. 
.. .. code-block:: none
.. 
..     Estimado Marcelo,
..     usted ha aprobado
..     con promedio 5.7.


1. The files `a.txt`_ and `b.txt`_
   have several sorted numbers from lowest to highest.
   
   .. _a.txt: ../../_static/a.txt 
   .. _b.txt: ../../_static/b.txt 
   
   Write a program which create a file called ``c.txt``
   which contain all the numbers from ``a.txt`` and ``b.txt``
   and also is sorted.
   
   Do not save the numbers in a data structure.
   Read and write them one by one.



2. A charity institution has a register of the people which do some
   donations, in a register file called ``donors.txt``.
   
   The file is sorted by the people ID from lowest to highest.
   To simplify the problem,
   lets suppose that the ID's has five digits,
   and does not include a verification after the dash.
   
   For example,
   the file content can be the following:
   
       ====== ==================== ======
       ID     Name                 Amount
       ====== ==================== ======
       15274  Marie Curie             200
       15891  Jean Dupont             150
       16443  Erika Mustermann        400
       16504  John Smith               80
       17004  Jan Kowalski            200
       ====== ==================== ======
   
   The challenges are the following:
   
   1. Write a function which create the file, with the table data.
   2. Write a function which show the file content.
   3. Write a function which ask to the user to enter an ID,
      and show as output the donation amount by that person.
   4. Write a function which ask to the user to enter an ID,
      and remove from the file the user with that ID.
   5. Write a program which ask to the user enter the donor information
      and add them to the file.

3. The ``data1.txt`` file
   has three integer numbers in each line:
   
   .. code-block:: none
   
       45 12 98
       1 12 65
       7 15 76
       54 23 1
       65 2 84
   
   1. Write a function called ``lines_addition(filename)``
      which return a list with the addition of all the lines in the file::
   
       >>> lines_addition('data1.txt')
       [155, 78, 98, 78, 151]
   
   2. Write a function called ``column_addition(filename)``
      which return a list with the addition of the three columns of the file::
   
       >>> column_addition('data1.txt')
       [172, 64, 324]

4. A shop has their product information in a file called ``products.txt``.
   Each file line has three data:
   
   * the product code (an integer number),
   * the product name, and
   * the units number of the product
     remainder in the warehouse.
   
   The data is divided by a ``/`` symbol.
   For example,
   the next lines can be the file content:
   
   .. code-block:: none
   
       1265/Watch/26
       613/Notebook/87
       9801/Trumpet/3
       321/Pencil/12
       5413/Tomatoes/5
   
   1. Write a function called ``product_exist(code)``
      which allow to know if a product with the code
      exist or not::
   
       >>> product_exist(1784)
       False
       >>> product_exist(321)
       True
       >>> product_exist(613)
       True
       >>> product_exist(0)
       False
   
   2. Write a function called ``replenish_soon()``
      which create a new file called ``replenish_soon.txt``
      which contain all the product data of those who are less than 10 units.
   
      In this case,
      the ``replenish_soon.txt`` file
      must contain the following information:
   
   .. code-block:: none
   
       9801/Trumpet/3
       5413/Tomatoes/5

5. A Medical center has a file called ``patients.txt``
   with the personal data of their patients.
   Each file line has the ID, the name and the age of a patient,
   divided by the ``:`` symbol.
   This is the file looks like:
   
   .. code-block:: none
   
       12067539-7:Anastasia López:32
       15007265-4:Andrés Morales:26
       8509454-8:Pablo Muñoz:45
       7752666-8:Ignacio Navarro:49
       8015253-1:Alejandro Pacheco:51
       9217890-0:Patricio Pimienta:39
       9487280-4:Ignacio Rosas:42
       12393241-2:Ignacio Rubio:33
       11426761-9:Romina Pérez:35
       15690109-1:Francisco Ruiz:26
       6092377-9:Alfonso San Martín:65
       9023365-3:Manuel Toledo:38
       10985778-5:Jesús Valdés:38
       13314970-8:Abel Vázquez:30
       7295601-k:Edison Muñoz:60
       5106360-0:Andrea Vega:71
       8654231-5:Andrés Zambrano:55
       10105321-0:Antonio Almarza:31
       13087677-3:Jorge Álvarez:28
       9184011-1:Laura Andrade:47
       12028339-1:Jorge Argandoña:29
       10523653-0:Camila Avaria:40
       12187197-1:Felipe Ávila:36
       5935556-2:Aquiles Barriga:80
       14350739-4:Eduardo Bello:29
       6951420-0:Cora Benítez:68
       11370775-5:Hugo Berger:31
       11111756-k:Cristóbal Bórquez:34
   
   Also,
   each time that someone has a doctor appointment,
   the visit is registered in a file called ``appointments.txt``, 
   adding a new line with the patient ID,
   the visit date (in ``day-month-year`` format)
   and the appointment cost,
   also divided by a ``:`` symbol.
   The file looks like:
   
   
   .. code-block:: none
   
       8015253-1:4-5-2010:69580
       12393241-2:6-5-2010:57274
       10985778-5:8-5-2010:73206
       8015253-1:10-5-2010:30796
       8015253-1:12-5-2010:47048
       12028339-1:12-5-2010:47927
       11426761-9:13-5-2010:39117
       10985778-5:15-5-2010:86209
       7752666-8:18-5-2010:41916
       8015253-1:18-5-2010:74101
       12187197-1:20-5-2010:38909
       8654231-5:20-5-2010:75018
       8654231-5:22-5-2010:64944
       5106360-0:24-5-2010:53341
       8015253-1:27-5-2010:76047
       9217890-0:30-5-2010:57726
       7752666-8:1-6-2010:54987
       8509454-8:2-6-2010:76483
       6092377-9:2-6-2010:62106
       11370775-5:3-6-2010:67035
       11370775-5:7-6-2010:47299
       8509454-8:7-6-2010:73254
       8509454-8:10-6-2010:82955
       11111756-k:10-6-2010:56520
       7752666-8:10-6-2010:40820
       12028339-1:12-6-2010:79237
       11111756-k:13-6-2010:69094
       5935556-2:14-6-2010:73174
       11111756-k:21-6-2010:70417
       11426761-9:22-6-2010:80217
       12067539-7:25-6-2010:31555
       11370775-5:26-6-2010:75796
       10523653-0:26-6-2010:34585
       6951420-0:28-6-2010:45433
       5106360-0:1-7-2010:48445
       8654231-5:4-7-2010:76458
   
   Note that the date are sorted from lowest to the recently date,
   because the new lines always are added at the final of the file.
   
   1. Write a function called ``total_patient_cost(ID)``
      which contain the patient appointments total cost
      of the given ID::
   
       >>> total_patient_cost('8015253-1')
       297572
       >>> total_patient_cost('14350739-4')
       0
   
   2. Write a function called ``day_patients(day, month, year)``
      which returns a list with the patients name attended
      the given date::
   
       >>> day_patients(2, 6, 2010)
       ['Pablo Muñoz', 'Alfonso San Martín']
       >>> day_patients(23, 6, 2010)
       []
   
   3. Write a function called ``split_patients()``
      which make two different files:
   
      * ``young.txt``, with the data of the young patients with less than 30 years old;
      * ``old.txt``, with the data of all the patients with more than 60 years old.
   
      For example,
      the  ``young.txt`` file must looks like:
   
      .. code-block:: none
   
          15007265-4:Andrés Morales:26
          15690109-1:Francisco Ruiz:26
          13087677-3:Jorge Álvarez:28
          12028339-1:Jorge Argandoña:29
          14350739-4:Eduardo Bello:29
   
   4. Write a function called  ``profit_by_month()``
      which make a new file called ``profits.txt``
      which contain the total of profit for each month
      following the next format:
   
      .. code-block:: none
   
          5-2010:933159
          6-2010:1120967
          7-2010:124903
   
   
6. The grades of a subject are saved in a file called ``grades.txt``,
   which contain the following data::
   
       Pepito:5.3:3.7:6.7:6.7:7.1:5.5
       Yayita:5.5:5.2:2.0:5.6:6.0:2.0
       Fulanita:7.1:6.6:6.4:5.1:5.8:6.3
       Moya:5.2:4.7:1.8:3.5:2.7:4.5
   
   Each line has the student name and their six grades, divided by a ``:`` symbol.
   
   Write a program which make a new file called ``report.txt``,
   in which each line show if the student is approved (average ≥ 4,0) o failed (average < 4,0)::
   
       Pepito approved
       Yayita approved
       Fulanita approved
       Moya failed
   
