Lecture 2 - Program development
-------------------------------

A **program** is a text file that contains
code to be executed by the computer.

In the case of the Python programming language, 
the program is executed by an **interpreter**.
The interpreter is a program which execute programs.

The programs written in Python
must be contained in a file
with the ``.py`` extension.
In Windows, the program can be executed doing a double
click above the file icon.

To test this,
download the quadratic.py_ file,
which allows to solve quadratic equations.

.. _quadratic.py: ../_static/programs/quadratic.py

Editing programs
~~~~~~~~~~~~~~~~
.. index:: text editor

A program is a `text file`_.
Therefore, it can be created or edited
using any `text editor`_,
like Notepad.

What cannot be used
is a text processor,
like Microsoft Word.

Try it:
open the ``quadratic.py`` program
with Notepad (or any other editor)
and you will see its contents.

.. _text file: http://en.wikipedia.org/wiki/Text_file
.. _text editor: http://en.wikipedia.org/wiki/Text_editor

.. index:: text editor (list)

Other text editors
(much better than Notepad)
that you can install are:

* in Windows:
  `Notepad++ <http://notepad-plus-plus.org/>`_,
  `Textpad <http://www.textpad.com/>`_;
* in Mac:
  `TextWrangler <http://www.barebones.com/products/textwrangler/>`_,
  `TextMate <http://macromates.com/>`_;
* in Linux:
  `Gedit <http://projects.gnome.org/gedit/>`_,
  `Kate <http://kate-editor.org/>`_.


Python interpreter installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. index:: interpreter (installation)

One thing is to edit the program and another one is to execute it.
The **interpreter** must be installed in order to
be able to execute the program using Python.

You can find the installer list
in the `Python download web`_
You must download the one indicated for your computer
and operating system.

.. _Python download web: http://www.python.org/download/
..

You must install the version **2.7.1**,
not 3.1.3.

Do not use the ``x86-64`` installers
unless you are sure that your computer
has a 64-bit architecture.

Program execution
~~~~~~~~~~~~~~~~~

Once the program is written and the interpreter has been installed,
it is possible to execute the programs.
The next video shows the process:

    [Video]

Console use
~~~~~~~~~~~
.. index:: interpreter (interactive), console

Executing the programs
is not the only way to use the interpreter.
If we execute Python without passing any program,
the **console** (or **interactive interpreter**) will open.

The console allows to enter a program through the command line.
It also allows to evaluate expressions and see the results immediately.
This allows, for example, using it like a calculator.

The next video shows how to use the interactive interpreter:

    [Video]

The interactive console
always shows the ``>>>`` symbol,
to indicate the possibility to enter code.
In all the books about Python
and in all these lectures,
each time an example appears using this symbol
means that it must be executed in a console
and not in a program. For example::

    >>> a = 5
    >>> a > 10
    False
    >>> a ** 2
    25

In this example, at the time the expressions are entered ``a > 10`` and ``a ** 2``,
the interactive interpreter give the results ``False`` and ``25``.

There is no reason to write the ``>>>`` symbol
in a program, because it is not part of the language syntax.


Development environment
~~~~~~~~~~~~~~~~~~~~~~~
.. index:: development environment, IDE

In general,
using a simple text editor to write programs is not
the most efficient way to work.

The  **development environments**
(also called *IDE*)
are applications that facilitate the task of writing programs.

Python comes with its own development environment, called **IDLE**.
The following video shows how to use IDLE to develop a program
and to use the interactive console:

    [Video]

Other good advanced Python development environments are:

* `PyScripter <http://code.google.com/p/pyscripter/downloads/list>`_,
* `WingIDE 101 <http://www.wingware.com/downloads/wingide-101/3.2.12-1/binaries>`_

You can test them and use the most comfortable for you.

