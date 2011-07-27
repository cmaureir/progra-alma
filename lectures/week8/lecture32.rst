Lecture 32 - An extra bite of Python
-------------------------------------

optparse
=========

from optparse import OptionParser
#Define an instance of the OptionParser Class
parser = OptionParser()
parser.add_option("-a", "--antenna", dest="antName",
metavar='AntennaName',
help="The name of the antenna")
# This actually parses the command line arguments
(options, args) = parser.parse_args()
# Check to make sure that an antenna name was specified
if options.antName == None:
print "You must specify an antenna \"-a\" option"
import sys # Just need this for the exit command
sys.exit(-1)
print “Now going to use Antenna: “ + options.antName


pyqt
====

pygtk
=====

csv
====

bluetooth
==========

python serial
=============

python game
============




http://sourceforge.net/projects/pywin32/
http://bleyer.org/pyusb/
https://sites.google.com/site/ibarona/uspp
http://pyserial.sourceforge.net/
http://videocapture.sourceforge.net/
http://www.pythonware.com/products/pil/
http://www.sqlalchemy.org/
http://sourceforge.net/projects/mysql-python/
http://pyxml.sourceforge.net/topics/


