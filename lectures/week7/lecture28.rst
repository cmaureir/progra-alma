Lecture 28 - Interactive matplotlib plots (part II)
---------------------------------------------------

.. Introduction
.. ~~~~~~~~~~~~
.. 
.. matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell (ala MATLAB®* or Mathematica®†), web application servers, and six graphical user interface toolkits.
.. 
.. matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc, with just a few lines of code. For a sampling, see the screenshots, thumbnail gallery, and examples directory
.. 
.. 
.. 
.. For example, using "ipython -pylab" to provide an interactive environment, to generate 10,000 gaussian random numbers and plot a histogram with 100 bins, you simply need to type
.. 
..   x = randn(10000)
..   hist(x, 100)
.. For the power user, you have full control of line styles, font properties, axes properties, etc, via an object oriented interface or via a set of functions familiar to MATLAB users. The pylab mode provides all of the pyplot plotting functions listed below, as well as non-plotting functions from numpy and matplotlib.mlab.
.. 
.. 
.. Installation
.. ~~~~~~~~~~~~
.. 
.. First of all, you need to search
.. with the package manager of your Linux distribution,
.. if *matplotlib* is in the repositories.
.. 
.. If not, you can check the `official installation guide`_,
.. and you can download the source from their `sourceforge`_
.. webpage.
.. 
.. .. _`official installation guide`: http://matplotlib.sourceforge.net/users/installing.html 
.. .. _`sourceforge`: http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0.1/
.. 
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
