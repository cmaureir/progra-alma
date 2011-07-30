Lecture 29 - IPython
---------------------

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


Installation
~~~~~~~~~~~~~

There are a lot of ways to install IPython,
so, here is some alternatives:

* Using ``easy_install`` (if you are running OS X or Linux, with setuptools_ installed)::

      $ easy_install ipython[zmq, test]

.. _setuptools: http://pypi.python.org/pypi/setuptools

* Installation from source (Download the `IPython tarball file`_)::


      $ tar zxvf ipython-ipython-rel-0.10.1-0-g5d37858.tar.gz
      $ cd ipython-ipython-3583d23/
      $ python setup.py install

  .. _IPython tarball file: https://github.com/ipython/ipython/tarball/rel-0.10.1tar

  or, you can run the binary file inside called ``ipython.py``::

      $ python ipython.py

* Windows, download the `IPython exe setup`_ and follow the steps.

.. _IPython exe setup: http://ipython.scipy.org/dist/ipython-0.10.2.win32-setup.exe

If you have problems installing **IPython** please contact the course teacher or assistant.

For any installation doubt, you can visit the `IPython installation page`_
for more information.

.. _IPython installation page: http://ipython.org/ipython-doc/rel-0.10.2/html/install/install.html




IPython features
~~~~~~~~~~~~~~~~~

* **Tab completion**

  The Tab completion is a convenient way to explore any Python structure or object,
  which you are dealing with.

  You simple need to type the ``object_name.``
  and then press the :kbd:`Tab` key (↹) to view the object's attributes
  and methods.

  Besides Python objects, you can use tab completion with file and directory names.

* **Exploring your objects**

  There is a special IPython operator, which is ``?``,
  so typing ``object_name?`` you will obtain all the object details,
  including *docstrings*, *function definition lines*, *constructor details*, etc.
  
  If you want to get some specific information of an object,
  you can use some **magic commands**, like:

  * ``%pdoc <object>``, print the *docstring* for an object.
  * ``%pdef <object>``, print the *definition header* for any callable object. 
  * ``%psource <object>``, print the *source code* for an object.
  * ``%pfile <object>``, shor the entire source file where an object was defined.
 
* **Magic functions**

  IPython has a set of predefined **magic functions** that you can call with
  a command line style syntax. These include:

  * Functions that work with code: ``%run``, ``%edit``, ``%save``, ``%macro``, ``%recall``, etc.

    * Lets consider the following example::
       
          localhost~»≻ cat test.py
          print 'hello world!'  

    * ``%run <script>``::

          In [5]: %run test.py
          hello world!

    * ``%edit <file``::

          In [4]: %edit test.py
          # here we change the file.
          Editing... done. Executing edited code...
          hello world!

  * Functions which affect the shell: ``%colors``, ``%xmode``, ``%autoindent``, etc.
  * Other functions such as ``%reset``, ``%timeit`` or ``%paste``.

  You can always call these using the ``%`` prefix,
  and if you are typing one on a line by itself,
  you can omit even that::

      run thescript.py

  For more details on any magic function, call ``%somemagic?`` to read its docstring.
  To see all the available magic functions, call ``%lsmagic``.

* **History**

  IPython stores both the commands you enter, and the results they produce,
  it means, ``In [x]`` and ``Out [x]`` lines.
  
  You can easily go through previous commands with the
  :kbd:`Up` arrow (↑) and :kbd:`Down` arrow (↓) keys.

  The `Input` and `Output` history are kept in variables called ``In`` and ``Out``,
  which can both be indexed by the prompt number on which they occurred,
  e.g. ``In[4]``. The last three objects in output history are also kept
  in variables named ``_``, ``__`` and ``___``::

      In [27]: x = 21

      In [28]: x + 2
      Out[28]: 23
      
      In [29]: 5**5
      Out[29]: 3125
      
      In [30]: __
      Out[30]: 23
      
      In [31]: _
      Out[31]: 23
      
      In [32]: ___
      Out[32]: 3125

  You can also use the ``%history`` magic function to examine past input and output::

      In [33]: %history
      ...
      27: x = 21
      28: x + 2
      29: 5**5
      30: __
      31: _
      32: ___
      33: _ip.magic("history ")

  Input history from previous sessions is saved in a database,
  and IPython can be configured to save output history.

  Several other magic functions can use your input history,
  including ``%edit``, ``%rerun``, ``%recall``, ``%macro`` and ``%save``.

* **System shell commands**

  To run any command at the system shell, simply prefix it with ``!``, e.g.::
      
      In [15]: !ping www.alma.cl
      PING wwwpub01.sco.alma.cl (200.2.1.10) 56(84) bytes of data.
      64 bytes from offlinetools.osf.alma.cl (200.2.1.10): icmp_req=1 ttl=54 time=13.8 ms
      64 bytes from offlinetools.osf.alma.cl (200.2.1.10): icmp_req=2 ttl=54 time=15.6 ms
      ...

  You can capture the output into a Python list, e.g.: ``files = !ls``::

      In [1]: files = !ls

      In [2]: files
      Out[2]: SList (.p, .n, .l, .s, .grep(), .fields(), sort() available):
      0: a_folder
      1: another_file
      2: my_file
      
      In [3]: files[0]
      Out[3]: 'a_folder'
      
      In [4]: files[2]
      Out[4]: 'my_file'
      
      In [5]: ls
      a_folder/  another_file  my_file

If you want to learn more about IPython,
you can see the `official documentation`_.

.. _official documentation: http://ipython.org/ipython-doc/rel-0.10.2/html/parallel/index.html


Additional Material
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

Finnally,
if you are interested in the **Parallel Computing**,
IPython provides a lot of functionallities, which
you can see in the `parallel computing documentation`_.

.. _parallel computing documentation: http://ipython.org/ipython-doc/rel-0.10.2/html/parallel/index.html
