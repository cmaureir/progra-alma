Lecture 20 - Coding good practices
-----------------------------------

In every programming language (fortran, Java, C/C++, Perl, etc)
there are some proposed normative by the languages creators,
or actual maintainers, which are a good advise to new programmers
or for people who want to improve their code.

In the cases which are a very strict normative, is when you want to
send your code to some institution related with you selected programming language.

For example, the developers of the python modules
*must* achieve this norms.

For this course, the only important idea is to tell you ``how can be written`` but 
there will be ``not`` a normative, this is only for educational purpose.


The following material are some ideas extracted from
the official `Style Guide for Python Code`_ which is a adaptation from
the original Python Style Guide Essay written by the Python's creator,
`Guido van Rossum`_.

.. _`Style Guide for Python Code`: http://www.python.org/dev/peps/pep-0008/
.. _`Guido van Rossum`: http://en.wikipedia.org/wiki/Guido_van_Rossum

.. if __main__ = __name__:

Do not worry if you see some ``class`` or ``method`` reference,
because in the next lectures we will deep into the Object Oriented world!.


Code lay-out
~~~~~~~~~~~~

* **Indentation**
 
  When you are writing code, and you need to enter into a new indentation level,
  for example, in an ``if`` statement, you must use 4 spaces per each indentation
  level.
 
  Correct::
  
      if condition:
          do_some_stuff()

  Wrong::
  
      if condition:
       do_some_stuff()

  ::

      if condition:
            do_some_stuff()

  etc.

  If you have very long lines calling functions, or creating variables, etc,
  you can user more than one line to do this.

  There are two ways to write this statements with parenthesis,
  without lines in the first line, or with some parameters,
  for example.

  Correct::

      # Aligned with opening delimiter
      foo = long_function_name(var_one, var_two,
                               var_three, var_four)

      # Double code indention for hanging indent; nothing on first line
      foo = long_function_name(
              var_one, var_two, var_three,
              var_four)

  Wrong::

      # Stuff on first line forbidden
      foo = long_function_name(var_one, var_two,
          var_three, var_four)
       
      # 2-space hanging indent forbidden
      foo = long_function_name(
        var_one, var_two, var_three,
        var_four) 
 
* **Tabs or Spaces?**

  Is very important to note that the programmer will never mix tabs and spaces.

  The most popular way to indent Python code is with  spaces only.
  The second popular way, is with tabs.

  So, you can choose.

* **Maximum Line length**

  The programmer must limit all lines to a maximum of 79 characters.
  (there are several plugins for text editors to do this, do not think
  that you must count every character!) 

* **Blank Lines**

  You must use blank lines in different times:
  
   * Two blank lines, to separate top-level function and class definitions.
   * One blank line, to separate method definitions inside a class.
   * One blank line, to separate groups of related functions. 

Imports
~~~~~~~

* **Separate lines**

  In several scripts you need to import more than one Python module,
  so, What is the correct way to do this?

  Correct::

      import os
      import sys 

  Wrong::

      import os, sys

  But when you are importing just a couple of methods from a Python module
  you can use the expression with the commas::

      from subprocess import Popen, PIPE


* **Top of the file**

  The module import of any script must be at the top of the file,
  does not matter where do you use it in your code,
  and must be after any module comment and docstring,
  and before module globals and constants.

  Imports should be grouped in the following order:

  1. standard library imports, for example::

      import sys
      import os

  2. related third party imports, for example::

      import matplotlib
      import scipy

  3. local application/library specific imports, for example::

      import my_module

  Is important to note that you need to leave a blank line between each group
  of imports.

Whitespace in Expressions and Statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Avoiding whitespace**

  Is important to avoid the unnecessary whitespaces in your code,
  in the following situations:

  * Immediately inside parentheses, brackets or braces.

    Correct::
        
        spam(ham[1], {eggs: 2})

    Wrong::
   
        spam( ham[ 1 ], { eggs: 2 } )

  * Immediately before a comma, semicolon, or colon:

    Correct::
  
        if x == 4: print x, y; x, y = y, x

    Wrong::
 
        if x == 4 : print x , y ; x , y = y , x

  * Immediately before the open parenthesis that starts the argument list of a function call:

    Correct::
    
        spam(1)
 
    Wrong::

        spam (1)

  * Immediately before the open parenthesis that starts an indexing or slicing:

    Correct::

        dict['key'] = list[index]

    Wrong::
  
        dict ['key'] = list [index]

  * More than one space around an assignment (or other) operator to align it with another.

    Correct::

        x = 1
        y = 2
        long_variable = 3

    Wrong::

        x             = 1
        y             = 2
        long_variable = 3



* **Other recommendations**

  Another situations when you must be careful, are the following:

  * Use spaces around arithmetic operators:

    Correct::

        i = i + 1
        submitted += 1
        x = x * 2 - 1
        hypot2 = x * x + y * y
        c = (a + b) * (a - b)

    Wrong::

        i=i+1
        submitted +=1
        x = x*2 - 1
        hypot2 = x*x + y*y
        c = (a+b) * (a-b)

  * Don't use spaces around the '=' sign when used to indicate a
    keyword argument or a default parameter value.

    Correct::

        def complex(real, imag=0.0):
            return magic(r=real, i=imag)

    Wrong::

        def complex(real, imag = 0.0):
            return magic(r = real, i = imag)

  * Compound statements (multiple statements on the same line) are
    generally discouraged.

    Correct::

        if foo == 'blah':
            do_blah_thing()
        do_one()
        do_two()
        do_three()

    Wrong::

        if foo == 'blah': do_blah_thing()
        do_one(); do_two(); do_three()

  * While sometimes it's okay to put an if/for/while with a small
    body on the same line, never do this for multi-clause
    statements.  Also avoid folding such long lines!

    Rather not::

        if foo == 'blah': do_blah_thing()
        for x in lst: total += x
        while t < 10: t = delay()

    Definitely not::

        if foo == 'blah': do_blah_thing()
        else: do_non_blah_thing()

        try: something()
        finally: cleanup()

        do_one(); do_two(); do_three(long, argument,
                                     list, like, this)

        if foo == 'blah': one(); two(); three()

Comments
~~~~~~~~

The comments are the main component of a code,
to understand the programmer thought,
so is very important to keep it simple and updated.

There are two types of comments:

* **Block comments**

  Block comments generally apply to some (or all) code that follows them,
  and are indented to the same level as that code.

  Each line of a block comment starts with a # and a single space (unless it
  is indented text inside the comment).

  Paragraphs inside a block comment are separated by a line containing a
  single #.

  For example::

      # This is my comment first line
      # and this is the second line.
      # 
      # This is a new paragraph.

* **Inline comments**

  Is fundamental to use inline comments sparingly.

  Inline comments should be separated by at least two spaces from the statement.
  They should start with a # and a single space.

  Inline comments are unnecessary and in fact distracting if they state
  the obvious.

  Avoid obvious comments:

  Wrong::

      x = x + 1                 # Increment x

  Correct::

      x = x + 1                 # Compensate for border

Documentation Strings
~~~~~~~~~~~~~~~~~~~~~

The documentation process for some programmers
is a very terrible situation, however is a vital
process, because the first approximation of an external
person to a programming project is their documentation.

In big words, the user must write docstrings for the following
situations:

* Public modules,
* Functions,
* Classes,
* Methods, 

The docstring must appear after the ``def`` line.

The structure of a docstring is very simple::

    """ This is a one-line docstring """

::

    """
   
    This is a multiline docstring

    """

And the general way to do this is as follows::

    def my_function():
        """ function which do some stuff """
         
        do_some_stuff()
        
For more information about the docstring conventions,
please take a look of the `official document`_.

.. _`official document`: http://www.python.org/dev/peps/pep-0257/

Version bookkeeping
~~~~~~~~~~~~~~~~~~~

Some development projects use software version control,
like SVN, CVS, Git, Bazaar, Mercurial, etc, so is important
to show the version inside the files.

The properly way to do this is, as follows::

    __version__ = "$Revision: 864b604d3742 $"
    # $Source$

You must include the previous lines after the module's docstring,
and before any other code, using a blank line above and below
to separate it.

Naming Conventions
~~~~~~~~~~~~~~~~~~

The naming conventions is a very discussed section
into the standard of Python, so there is now such thing
like a gold rule, but there is a lot of recommendations.

It does not matter what style you use, the important
thing is that you must be consistent.

* **Descriptive:** *Naming Styles*

  The following naming styles are commonly distinguished:

  * b (single lowercase letter)
  * B (single uppercase letter)
  * lowercase
  * lower_case_with_underscores
  * UPPERCASE
  * UPPER_CASE_WITH_UNDERSCORES
  * CapitalizedWords (or `CamelCase`_)
  * mixedCase (differs from CapitalizedWords by initial lowercase
    character!)
  * Capitalized_Words_With_Underscores (ugly!)

  In addition, the following special forms using leading or trailing
  underscores are recognized (these can generally be combined with any case
  convention):

  * ``_single_leading_underscore``: weak "internal use" indicator.
  * ``single_trailing_underscore_``: used by convention to avoid conflicts with
    Python keyword, for example ``class`` is protected, so we will use ``class_``
  * ``__double_leading_and_trailing_underscore__``: attributes that live in user-controlled namespaces.

  .. _`CamelCase`: http://en.wikipedia.org/wiki/CamelCase

* **Prescriptive**

  * **Names to avoid**

    Never use the characters which are indistinguishable,
    from the numerals one and zero, or if are used for another things.

    * `l` (lowercase letter el),
    *  `O` (uppercase letter oh),
    * `I` (uppercase letter eye)

  * **Module names**

    Modules should have short, all-lowercase names.
    Underscores can be used only if it improves readability.

  * **Class names**

    Almost without exception, class names use the CapWords convention.
    Classes for internal use have a leading underscore in addition.

  * **Global variable names**

    The conventions are about the same as those for functions.

  * **Functions names**

    Function names should be lowercase, with words separated by underscores
    as necessary to improve readability.

  * **Method arguments**

    Always use 'self' for the first argument to instance methods.

  * **Constants**

    Constants are usually defined on a module level and written in all
    capital letters with underscores separating words, for example::

        MAX_OVERFLOW = 0.4523
        TOTAL = 100
