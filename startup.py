#!/usr/bin/python
import os


print
print "checking for numpy"
try:
    import numpy
except ImportError:
    print "you should install numpy before continuing"
    os.system('python -m pip install numpy')
    
print "checking for cv2"
try:
    import cv2
except ImportError:
    print "you should install cv2 before continuing"
    os.system('python -m pip install cv2')
    
print "checking for PyQt4"
try:
    import PyQt4
except ImportError:
    print "you should install PyQt before continuing"
    os.system('python -m pip install PyQt4')
    
print "checking for HTMLparser"
try:
    import MySQLdb
except ImportError:
    print "you should install MySQLdb before continuing"
    os.system('python -m pip install MySQLdb')

