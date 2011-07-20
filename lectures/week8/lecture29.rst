Lecture 29 - iPython
---------------------

Introduction
~~~~~~~~~~~~

IPython: An Interactive Computing Environment

The goal of IPython is to create a comprehensive environment for interactive and exploratory computing. To support, this goal, IPython has two main components:

    An enhanced interactive Python shell.
    An architecture for interactive parallel computing.

All of IPython is open source (released under the revised BSD license), and it is used by a range of other projects. Have a look at the talks and presentations we have given about IPython.

IPython supports Python 2.5 to 2.7 officially. If you need to use Python 2.4, the 0.10 series probably works OK but has not been extensively tested with 2.4.


IPython’s interactive shell (ipython), has the following goals, amongst others:

    Provide an interactive shell superior to Python’s default. IPython has many features for object introspection, system shell access, and its own special command system for adding functionality when working interactively. It tries to be a very efficient environment both for Python code development and for exploration of problems using Python objects (in situations like data analysis).

    Serve as an embeddable, ready to use interpreter for your own programs. IPython can be started with a single call from inside another program, providing access to the current namespace. This can be very useful both for debugging purposes and for situations where a blend of batch-processing and interactive exploration are needed. New in the 0.9 version of IPython is a reusable wxPython based IPython widget.

    Offer a flexible framework which can be used as the base environment for other systems with Python as the underlying language. Specifically scientific environments like Mathematica, IDL and Matlab inspired its design, but similar ideas can be useful in many fields.

    Allow interactive testing of threaded graphical toolkits. IPython has support for interactive, non-blocking control of GTK, Qt and WX applications via special threading flags. The normal Python shell can only do this for Tkinter applications.

Installation
~~~~~~~~~~~~~

nstalling IPython itself¶
Given a properly built Python, the basic interactive IPython shell will work with no external dependencies. However, some Python distributions (particularly on Windows and OS X), don’t come with a working readline module. The IPython shell will work without readline, but will lack many features that users depend on, such as tab completion and command line editing. See below for details of how to make sure you have a working readline.

Installation using easy_install
If you have setuptools installed, the easiest way of getting IPython is to simple use easy_install:

$ easy_install ipython
That’s it.

Installation from source
If you don’t want to use easy_install, or don’t have it installed, just grab the latest stable build of IPython from here. Then do the following:

$ tar -xzf ipython.tar.gz
$ cd ipython
$ python setup.py install
If you are installing to a location (like /usr/local) that requires higher permissions, you may need to run the last command with sudo.

Windows
There are a few caveats for Windows users. The main issue is that a basic python setup.py install approach won’t create .bat file or Start Menu shortcuts, which most users want. To get an installation with these, you can use any of the following alternatives:

Install using easy_install.
Install using our binary .exe Windows installer, which can be found at here
Install from source, but using setuptools (python setupegg.py install).
IPython by default runs in a termninal window, but the normal terminal application supplied by Microsoft Windows is very primitive. You may want to download the excellent and free Console application instead, which is a far superior tool. You can even configure Console to give you by default an IPython tab, which is very convenient to create new IPython sessions directly from the working terminal.


Tutoria
~~~~~~~~

http://ipython.org/ipython-doc/stable/html/interactive/tutorial.html

http://ipython.org/presentation.html

http://ipython.scipy.org/moin/Cookbook

