Lecture 29 - IPython (1/2)
--------------------------

Introduction
~~~~~~~~~~~~

IPython is a python interactive shell,
which offer a lot of extra functionallities
to simplify the programming, like tab completion.

As the IPython goal is create a comprehnsive environment
for exploratory and interactive computing, has two main
components:

* An enhanced interactive Python shell.
* An architecture for interactive parallel computing.

Is important to tell that IPython is Open Source,
supporting Python 2.5 to 27 officialy.

IPython is used widely in several Scientific computing projects,
Web frameworks and other systems and in teaching area,
if you are interested, you can see some projects `here`_.

.. _here: http://ipython.scipy.org/moin/About/Projects_Using_IPython

Some important functionallities:

..  Re-redactar.

* **Tab completion**

  Tab completion, especially for attributes,
  is a convenient way to explore the structure of any object you’re dealing with.
  Simply type `object_name.<TAB>` to view the object’s attributes
  (see the readline section for more).
  Besides Python objects and keywords, tab completion also works on file and directory names.

* **Exploring your objects**

  Typing `object_name?` will print all sorts of details about any object, including docstrings,
  function definition lines (for call arguments) and constructor details for classes.
  To get specific information on an object,
  you can use the magic commands `%pdoc`, `%pdef`, `%psource` and `%pfile`.

* **Magic functions**

  IPython has a set of predefined ‘magic functions’ that you can call with
  a command line style syntax. These include:

  * Functions that work with code: `%run`, `%edit`, `%save`, `%macro`, `%recall`, etc.
  * Functions which affect the shell: `%colors`, `%xmode`, `%autoindent`, etc.
  * Other functions such as `%reset`, `%timeit` or `%paste`.

  You can always call these using the % prefix, and if you’re typing one on a line by itself, you can omit even that:

  ::
  
      run thescript.py

  For more details on any magic function, call `%somemagic?` to read its docstring.
  To see all the available magic functions, call `%lsmagic`.

* **History**

  IPython stores both the commands you enter, and the results it produces.
  You can easily go through previous commands with the up- and down-arrow keys,
  or access your history in more sophisticated ways.

  Input and output history are kept in variables called In and Out,
  which can both be indexed by the prompt number on which they occurred,
  e.g. `In[4]`. The last three objects in output history are also kept
  in variables named `_`, `__` and `___`.

  You can use the `%history` magic function to examine past input and output.
  Input history from previous sessions is saved in a database,
  and IPython can be configured to save output history.

  Several other magic functions can use your input history,
  including `%edit`, `%rerun`, `%recall`, `%macro`, `%save` and `%pastebin`.
  You can use a standard format to refer to lines:

  ::
  
      %pastebin 3 18-20 ~1/1-5

  This will take line 3 and lines 18 to 20 from the current session,
  and lines 1-5 from the previous session.

* **System shell commands**

  To run any command at the system shell, simply prefix it with !, e.g.:

  ::

      !ping www.bbc.co.uk

  You can capture the output into a Python list, e.g.: `files = !ls`.
  To pass the values of Python variables or expressions to system commands,
  prefix them with $: `!grep -rF $pattern ipython/*`.


Installation
~~~~~~~~~~~~~

There are a lot of ways to install IPython,
so, here is some alternatives:

* Using `easy_install`: (If you are running OS X or Linux, with `setuptools`_ installed)

  ::
  
      $ easy_install ipython[zmq, test]

.. _setuptools: http://pypi.python.org/pypi/setuptools

* Installation from source (Download the `ipython tarball file`_) 

.. _ipython tarball file: https://github.com/ipython/ipython/tarball/rel-0.10.1tar

  ::
  
      $ tar zxvf ipython-ipython-rel-0.10.1-0-g5d37858.tar.gz
      $ cd ipython-ipython-3583d23/
      $ python setup.py install
  
  or, you can run the binary file inside called `ipython.py`
  
  ::
  
      $ python ipython.py


* Windows, download the `ipython exe setup`_ and follow the steps.

.. _`ipython exe setup`: http://ipython.scipy.org/dist/ipython-0.10.2.win32-setup.exe

If you have some problem installing **IPython** please contact the course teacher or assistant.

Tutoria
~~~~~~~~

http://ipython.org/ipython-doc/rel-0.10.2/html/

http://ipython.scipy.org/moin/Cookbook

Additional Tutorials
~~~~~~~~~~~~~~~~~~~~

If you are more confortable with screencasts,
you can see the following links, with a lot
of useful video tutorials.

* `ShowMeDo IPython tutorials`_

.. _`ShowMeDo IPython tutorials`: http://showmedo.com/videotutorials/ipython

You can also view some presentations slides
performed in different conferences in the following link:

* `IPython presentations`_

.. _`IPython presentations`: http://ipython.org/presentation.html
