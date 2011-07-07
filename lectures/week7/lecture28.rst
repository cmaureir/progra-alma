Lecture 28 - Interactive matplotlib plots (part II)
---------------------------------------------------

At this point in the course,
you could think that Python is a programming language
wich provide an good environment to develop
applications, and numerical algorithms,
but that is only the main idea of Python,
there are a lot of modulos that you can use
in different areas, from programming GUIs to
interact with an Arduino through an USB or Bluetoot conection.

In this lecture, we will introduce a very useful
Python module, called `Matplotlib`_, as its name says,
is a *plotting library* for Python and NumPy.

.. image: http://matplotlib.sourceforge.net/_static/logo2.png

The *Aplication Programming Inteface (API)* is based
on the object-oriented paradigm, providing functionalities
to embedded plots in graphical applications,
or saving it in images.

You can use generic GUI toolkits,
like `Qt`_, `GTK`_ or `wxPython`_.

.. _`Qt`: http://qt.nokia.com/ 
.. _`GTK`: http://www.gtk.org/
.. _`wxPython`: http://www.wxpython.org/
.. _`Matplotlib`: http://matplotlib.sourceforge.net/

If you found examples which use a module called **pylab**
do not think that is an alternative, because is an interface
based on Matplotlib distributed under a BSD-style license,
and has the feature that combines **pyplot** and **NumPy**
modules in the same namespace.

The main advantage to Python programmers,
is that **Matplotlib** provide an environment very
similar to MATLAB, with some advantages,
like:

* Compatible with Python (and all the Python modules)
* An object-oriented environment to work.
* Open Source and Free
* etc

**Matplotlib** is focused in 2D plotting,
giving the tools to produce publication quality figures
in different formats, but also you can obtain 3D plots.

For example,

.. image:: http://matplotlib.sourceforge.net/_images/date_demo.png

.. image:: http://matplotlib.sourceforge.net/_images/subplot3d_demo.png

In **Matplotlib** you can generate with a few lines of code, plots,
histograms, power spectra, bar charts, errorcharts, scatterplots, etc.

You can find several useful examples in `this page`_.

.. _`this page`: http://matplotlib.sourceforge.net/gallery.html

Installation
~~~~~~~~~~~~

First of all, you need to search
with the package manager of your Linux distribution,
if *matplotlib* is in the repositories.

If not, you can check the `official installation guide`_,
and you can download the source from their `sourceforge`_
webpage.

.. _`official installation guide`: http://matplotlib.sourceforge.net/users/installing.html 
.. _`sourceforge`: http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0.1/
 
.. Concepts
.. ~~~~~~~~
.. 
.. 
.. http://shreevatsa.wordpress.com/2010/03/07/matplotlib-tutorial/
.. 
.. http://matplotlib.sourceforge.net/users/artists.html
.. http://matplotlib.sourceforge.net/users/image_tutorial.html
.. 
.. http://www.scipy.org/Plotting_Tutorial
.. http://www.scipy.org/Cookbook/Matplotlib
