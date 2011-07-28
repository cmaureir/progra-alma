Lecture 29 - IPython (1/2)
--------------------------

Introduction
~~~~~~~~~~~~

IPython is a Python interactive shell,
which offers a lot of extra functionalities
to simplify development, like tab completion.

As IPython's goal is to create a comprehensive environment
for exploratory and interactive computing, it has two main
components:

* An enhanced interactive Python shell.
* An architecture for interactive parallel computing.

Is important to mention that IPython is Open Source,
supporting Python 2.5 to 2.7 officialy.

IPython is widely used for scientific computing projects,
web frameworks and other systems, and also for teaching purposes.
If you are interested, you can check `some of those projects`_.

.. _some of those projects: http://ipython.scipy.org/moin/About/Projects_Using_IPython

Some important features:

..  Re-redactar.

* **Tab completion**

  Tab completion, especially for attributes,
  is a convenient way to explore the structure of any object you’re dealing with.
  Simply type ``object_name.`` and then press the :kbd:`Tab` key (↹) to view the object’s attributes
  (see the readline section for more).
  Besides Python objects and keywords, tab completion also works on file and directory names.

* **Exploring your objects**

  Typing ``object_name?`` will print all sorts of details about any object, including docstrings,
  function definition lines (for call arguments) and constructor details for classes.
  To get specific information on an object,
  you can use the magic commands ``%pdoc``, ``%pdef``, ``%psource`` and ``%pfile``.

* **Magic functions**

  IPython has a set of predefined ‘magic functions’ that you can call with
  a command line style syntax. These include:

  * Functions that work with code: ``%run``, ``%edit``, ``%save``, ``%macro``, ``%recall``, etc.
  * Functions which affect the shell: ``%colors``, ``%xmode``, ``%autoindent``, etc.
  * Other functions such as ``%reset``, ``%timeit`` or ``%paste``.

  You can always call these using the ``%`` prefix, and if you’re typing one on a line by itself, you can omit even that::

      run thescript.py

  For more details on any magic function, call ``%somemagic?`` to read its docstring.
  To see all the available magic functions, call ``%lsmagic``.

* **History**

  IPython stores both the commands you enter, and the results they produce.
  You can easily go through previous commands with the up- and down-arrow keys,
  or access your history in more sophisticated ways.

  Input and output history are kept in variables called In and Out,
  which can both be indexed by the prompt number on which they occurred,
  e.g. ``In[4]``. The last three objects in output history are also kept
  in variables named ``_``, ``__`` and ``___``.

  You can use the ``%history`` magic function to examine past input and output.
  Input history from previous sessions is saved in a database,
  and IPython can be configured to save output history.

  Several other magic functions can use your input history,
  including ``%edit``, ``%rerun``, ``%recall``, ``%macro``, ``%save`` and ``%pastebin``.
  You can use a standard format to refer to lines::

      %pastebin 3 18-20 ~1/1-5

  This will take line 3 and lines 18 to 20 from the current session,
  and lines 1-5 from the previous session.

* **System shell commands**

  To run any command at the system shell, simply prefix it with ``!``, e.g.::

      !ping www.bbc.co.uk

  You can capture the output into a Python list, e.g.: ``files = !ls``.
  To pass the values of Python variables or expressions to system commands,
  prefix them with ``$``::

    !grep -rF $pattern ipython/*


Installation
~~~~~~~~~~~~~

There are a lot of ways to install IPython,
so, here is some alternatives:

* Using ``easy_install`` (if you are running OS X or Linux, with setuptools_ installed)::

      $ easy_install ipython[zmq, test]

.. _setuptools: http://pypi.python.org/pypi/setuptools

* Installation from source (Download the `ipython tarball file`_)::


      $ tar zxvf ipython-ipython-rel-0.10.1-0-g5d37858.tar.gz
      $ cd ipython-ipython-3583d23/
      $ python setup.py install

  .. _ipython tarball file: https://github.com/ipython/ipython/tarball/rel-0.10.1tar

  or, you can run the binary file inside called ``ipython.py``::

      $ python ipython.py

* Windows, download the `ipython exe setup`_ and follow the steps.

.. _ipython exe setup: http://ipython.scipy.org/dist/ipython-0.10.2.win32-setup.exe

If you have problems installing **IPython** please contact the course teacher or assistant.

Tutorial
~~~~~~~~

http://ipython.org/ipython-doc/rel-0.10.2/html/

http://ipython.scipy.org/moin/Cookbook

Additional Tutorials
~~~~~~~~~~~~~~~~~~~~

If you are more comfortable with screencasts,
you can see the following links, with a lot
of useful video tutorials.

* `ShowMeDo IPython tutorials`_

.. _ShowMeDo IPython tutorials: http://showmedo.com/videotutorials/ipython

You can also check some slides_
from presentations on IPython
presented in various conferences.

.. _slides: http://ipython.org/presentation.html

