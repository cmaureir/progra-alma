Lecture 32 - An extra bite of Python
-------------------------------------

As the final lecture,
I would like to give you a big picture
of other Python modules, which can simplify
a lot of your everyday work.

Remember that these modules are only a few.
You can search for another ones,
and you will certainly find some for almost
all kinds of systems and tasks.
For example, there are Python modules
for developing low-level device drivers
and for developing Facebook applications.

Argument Parser (``argparse``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a Python module which was developed under
the goal to make it easy to write command line tools.

As an example, if we like to execute our Python script
in the following way::

    $ python script.py -f my_file

One option is to use the ``sys.argv`` variable::

    import sys

    print sys.argv

Executing the script::

    $ python script.py
    ['script.py']
    $ python script.py --help
    ['script.py', '--help']
    $ python script.py -f my_file
    ['script.py', '-f', 'my_file']

So, with a list, it could be very useful.
But we will need to write some ``if`` statement
to handle when the user types an option incorrectly,
or to check the ``len(argv)``, etc.

A better idea is to use the ``argparse`` module.

So, we will create an example to use one simple option,

* ``-f``, some input file.

First,
we need to import the module::

    import argparse

Second,
we need to create a parser object,
using the class ``ArgumentParser``::

    parser = optparse.ArgumentParser()

Third,
we need to add some option to our parser,
using the ``add_option()`` method::

    parser.add_argument('-f', '--file', help='input filename', dest='file_value')

As you can see,
we can give as a parameter both a short and a long option,
a help string, to obtain a guide when the user
uses the ``--help`` or ``-h`` options::

    $ python script.py -h
    $ python script.py --help

and a ``dest`` argument,
where the value of an option will be saved,
in this case *file_value*.

Fourth,
we obtain the values of the command line
into an ``args`` variable::

    args = parser.parse_args()

Finally,
we will add a ``print`` to show the values
of the options, adding to the ``args``
the *dest* value::

    print args.file_value

Ok, so our script is::

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='input filename', dest='file_value')

    args = parser.parse_args()

    print args.file_value

Now we will execute it,
to understand the behavior::

    $ python script.py
    None
    $ python script.py  test
    usage: script.py [-h] [-f FILE_VALUE]
    script.py: error: unrecognized arguments: test
    $ python script.py  -f my_file
    my_file
    $ python script.py  --file my_file
    my_file
    $ python script.py  -a test
    usage: script.py [-h] [-f FILE_VALUE]
    script.py: error: unrecognized arguments: -a test
    $ python script.py  -h
    usage: script.py [-h] [-f FILE_VALUE]

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE_VALUE, --file FILE_VALUE
                            input filename

Comma-Separated Values (CSV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CSV file formats is used
to store data in plain-text
that can be easily written an read in any text editor,
using as a delimiter a special symbol (``,``, ``;``, etc.).

Each line in a CSV file represent rows in a table,
being the commas the column separation.

So, a simple example of a CSV file could be::

    Jill, Valentine, 555-3000
    Claire, Redfield, 555-4000
    Leon, Kennedy, 555-5000

One benefit,
is that in a lot of spreadsheets programs,
like `OpenOffice`_ and `Microsoft Excel`_
you can export tables into CSV format,
so you can easily manipulate it
with Python.

.. _OpenOffice: http://www.openoffice.org/
.. _Microsoft Excel: http://office.microsoft.com/en-us/excel/

Python provides a module called ``csv``,
which you can easily import like this::

    import csv

Now, we will review the two basic actions
that we need to work with a CSV file,
write and read.

Writer
'''''''

First of all,
we need to create an associated file,
which we will open same as we learn in the
`lecture 15`_, using the ``open`` function,
but inside of a CSV module function,
called ``writer``.

.. _lecture 15: ../week4/lecture15.html

::

    import csv
    
    writer = csv.writer(open('test.csv', 'w'))

Finally,
we need to write some content
inside the file, in which case
we can use a CSV module function,
called ``writerows`` which receive
as parameter a list of tuples.
Each tuple element, represents a
column in the row::

    writer.writerows([
        ('John',   'Smith',    12345),
        ('Alexia', 'Ashford',   98765),
        ('Chris',  'Redfield', 99123)
    ])

And that is it,
very simple.

The whole code looks like::

    import csv
    
    writer = csv.writer(open('test.csv', 'w'))
    writer.writerows([
        ('John',   'Smith',    12345),
        ('Alexia', 'Ashford',   98765),
        ('Chris',  'Redfield', 99123)
    ])

Looking inside the file::

    $ cat test.csv 
    John,Smith,12345
    Alexia,Ashford,98765
    Chris,Redfield,99123


Reader
''''''

Reading a CSV file,
is very similar to read a simple file,
the only difference is that we will
use a CSV module function to obtain
the reference to the file,
called ``reader``::

    import csv
    
    reader = csv.reader(open('test.csv', 'r'))

The ``reader`` reference,
will contain all the file data,
and we can access it easily,
using a `for` statement::


    for first, last, value in reader:
            print first, last, value


All the code together looks like::

    import csv
    
    reader = csv.reader(open('test.csv', 'r'))
    for firstname, lastname, value in reader:
            print firstname, lastname, value

And the output is::

    $ python csv-reader.py
    John Smith 12345
    Alexia Ashford 98765
    Chris Redfield 99123


Extensible Markup Language (XML)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The XML format is a set of rules,
for encoding document
in a machine-readable form.

The XML design goals are, *simplicity*, *generality*, and *usability*
over the Internet, because is use also to
represent some web service.

A lot of Application Programming Interfaces (APIs),
have been developed using it,
and is a widely used schema to the software configuration files.

There is a Python module called ``xml.dom.minidom``,
to interact with XML files.

The main idea,
previous to start to work with XML files,
is the tree notion schema.
Every new tag is a ``node``,
and each node can has a ``child node``.
Each node, has a ``name`` and a ``value``.

Parsing XML
''''''''''''

You can parse an XML file
of an XML string using two
methods of this module,
called ``parse`` and ``parseString``::


    from xml.dom.minidom import parse, parseString
    
    dom1 = parse( "test.xml" )   # parse an XML file
    dom2 = parseString( "<myxml>Some data <empty/> some more data</myxml>" )
    print dom1.toxml()
    print dom2.toxml()


The content of the ``test.xml`` file is::

    <tag>hello</tag>

And the output of the script is::

    $ python xml-example.py
    <?xmlversion="1.0"?>
    <tag>hello</tag>
    <?xmlversion="1.0"?>
    <myxml>Somedata<empty/>somemoredata</myxml>


You have another functionality
to obtain data from each node,
like:

* node.nodeName
* node.nodeValue
* node.childNodes

Lets consider the next file::

    $ cat test.xml                                                                                                                                         
    <tag>
        test content
        <name>hello</name>
        <name>world</name>
    </tag>

Now, we will obtain some of the file values,
with the following script::

    from xml.dom.minidom import parse, parseString
    
    dom1 = parse( "test.xml" )   # parse an XML file
    first = dom1.getElementsByTagName('tag')[0]

    print first.childNodes[0].nodeValue
    print first.childNodes[1].toxml()
    print first.nodeName    

The output will be::
                                                                                                                                                             
    test content
    <name>hello</name>                                                                                                                                           tag


Finding elements
'''''''''''''''''

If you want to walk through the ``childNodes`` tree
you need to use the ``getElementsByTagName``,
inside a for statement::

    from xml.dom.minidom import parse
    dom = parse('test.xml')
    for node in dom.getElementsByTagName('tag'):  # visit every node <tag/>
        print node.toxml()

The ``getElementsByTagName`` finds all children of a given name,
no matter how deep, thus working recursively.

Adding an empty element
''''''''''''''''''''''''

Another functionality is be able to add
new nodes in the XML structure,
for example if we want to add an empty ``<new tag />``
it is necessary to do the following::

    from xml.dom.minidom import parse
    dom = parse('test.xml')
    x = dom.createElement('new tag')  # creates <new tag />
    dom.childNodes[0].appendChild(x)  # appends at end of 1st child's children
    print dom.toxml()

New ``test.xml`` file::

    <?xml version="1.0" ?>
    <tag>
        test content
        <name>hello</name>
        <name>world</name>
    <new tag/></tag>

Adding an element with text inside
'''''''''''''''''''''''''''''''''''

If you want to create a new node,
but adding text inside, or example::

    <new>my content</new>

You need to create the following script::

    from xml.dom.minidom import parse
    dom = parse('test.xml')

    x = dom.createElement('new')  # creates <new />
    txt = dom.createTextNode('my content')  # creates 'my content'
    x.appendChild(txt)  # results in <new>my content</new>

    dom.childNodes[0].appendChild(x)  # appends at end of 1st child's children
    print dom.toxml()

The new content of the file::

    <?xml version="1.0" ?>
    <tag>
        test content
        <name>hello</name>
        <name>world</name>
    <new>my content</new></tag>

More interesting modules
~~~~~~~~~~~~~~~~~~~~~~~~

Serial Port Development (PySerial)
'''''''''''''''''''''''''''''''''''

In computing,
a serial port is a serial communication physical interface
through which information transfers in or out one bit at a time
(contrast parallel port).

Modern computers without serial ports may require serial-to-USB
converters to allow compatibility with RS 232 serial devices.

Serial ports are still used in applications such as industrial automation systems,
scientific instruments, shop till systems and some industrial and consumer products.

A serial port requires very little supporting software from the host system.

`PySerial`_ is one of the Python modules to work with
the serial port and devices.

To install this Python module,
please check the official `PySerial installation`_ instructions.

.. _PySerial installation: http://pyserial.sourceforge.net/pyserial.html
.. _PySerial: http://pyserial.sourceforge.net/


An example which open a named port at ``19200,8,N,1``, with1s timeout::

    >>> ser = serial.Serial('/dev/ttyS1', 19200, timeout=1)
    >>> x = ser.read()          # read one byte
    >>> s = ser.read(10)        # read up to ten bytes (timeout)
    >>> line = ser.readline()   # read a '\n' terminated line
    >>> ser.close()


SQLite Development (PySQLite)
''''''''''''''''''''''''''''''

SQLite is an embedded relational database management system.
In difference to other data base (DB) management systems,

SQLite is not a separate process that is accessed from the client application,
but is a part of it, in other words, SQLite does not require to access a DB
server, because creates a local ``db`` file, with all the DB content.

To download and install this module,
you can visit the `PySQLite download page`_.

.. _PySQLite download page: http://code.google.com/p/pysqlite/downloads/list

The following example show
how to interact with a `PySQLite`_.

If we need to connect to a database file ``mydb``::

    >>> from pysqlite2 import dbapi2 as sqlite
    >>> con = sqlite.connect("mydb")

For the following example,
we will consider a created data base,
with the following ``table`` and ``content``,
SQL code::

    create table people
    (
      name_last      varchar(20),
      age            integer
    );

    insert into people (name_last, age) values ('Yeltsin',   72);
    insert into people (name_last, age) values ('Putin',     51);

This example shows the simplest way to print the entire contents of the people table::

    >>> from pysqlite2 import dbapi2 as sqlite
    >>> con = sqlite.connect("mydb") # Create a connection to the database file "mydb"
    >>> cur = con.cursor() # Get a Cursor object that operates in the context of Connection con
    >>> cur.execute("select * from people order by age") # Execute the SELECT statement
    >>> print cur.fetchall() # Retrieve all rows as a sequence and print that sequence

Sample output::

    [(u'Putin', 51), (u'Yeltsin', 72)]

To apply the changes into the data base you need to committed explicitly::

    >>> con.commit()


.. _PySQLite: http://code.google.com/p/pysqlite/

Python Imaging Library (PIL)
'''''''''''''''''''''''''''''

The `Python Imaging Library`_ (PIL)
adds image processing capabilities to your Python interpreter.

This library supports many file formats,
and provides powerful image processing and graphics capabilities.

The ``Image`` class
is the most important class in PIL.

To load an image from a file,
use the open function in the Image module,
we will use the widely know `lena.ppm`_.

.. _lena.ppm: ../../_static/images/lena.ppm

.. image::  ../../_static/images/lena.png
   :alt: lena
   :width: 300px

The code will be::

    >>> import Image
    >>> im = Image.open("lena.ppm")

If successful,
this function returns an ``Image object``.
You can now use instance attributes to examine the file contents::

    >>> print im.format, im.size, im.mode
    PPM (512, 512) RGB

.. _Python Imaging Library: http://www.pythonware.com/library/pil
