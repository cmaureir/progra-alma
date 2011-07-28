Lecture 32 - An extra bite of Python
-------------------------------------

Optparse
=========

::

    >>> from optparse import OptionParser     # Define an instance of the OptionParser Class
    >>> parser = OptionParser()
    >>> parser.add_option("-a", "--antenna", dest="antName", metavar = 'AntennaName', help = "The name of the antenna")  
    >>> (options, args) = parser.parse_args() # This actually parses the command line arguments
    >>> if options.antName == None: # Check to make sure that an antenna name was specified
    >>>     print "You must specify an antenna \"-a\" option"
    >>>     import sys # Just need this for the exit command
    >>>     sys.exit(-1)
    >>> print “Now going to use Antenna: “ + options.antName


PyQt and PySide
===============

PENDING

PyGTK
======

PENDING

CSV and XML
===========

PENDING

PySerial
=========

PENDING

Data Bases
==========

PENDING


http://sourceforge.net/projects/pywin32/
http://bleyer.org/pyusb/
https://sites.google.com/site/ibarona/uspp
http://pyserial.sourceforge.net/
http://videocapture.sourceforge.net/
http://www.pythonware.com/products/pil/
http://www.sqlalchemy.org/
http://sourceforge.net/projects/mysql-python/
http://pyxml.sourceforge.net/topics/


