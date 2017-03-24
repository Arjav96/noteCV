import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
# Important Constants being used:

WIDTH = 1380
HEIGHT = 720
STARTWINDOW = (10,10)
mainTitle = 'NoteCV'


STARTPOS	=		(0,0)

HEADFONT	=		30
SUBHEADFONT	=		25
PARAFONT	=		15

STARTPOSEDITOR	=	(200,100)

# Fonts

font1 = QtGui.QFont()
font1.setFamily(_fromUtf8("Sawasdee"))
font1.setPointSize(16)
font1.setBold(True)
font1.setWeight(75)


fontCSL = QtGui.QFont()
fontCSL.setFamily(_fromUtf8("Courier 10 Pitch"))
fontCSL.setPointSize(22)
fontCSL.setBold(True)
fontCSL.setWeight(75)

fontSmall = QtGui.QFont()
fontSmall.setFamily(_fromUtf8("Sawasdee"))
fontSmall.setPointSize(12)
fontSmall.setBold(True)
fontSmall.setWeight(75)

# Dictionary

buttonToAddress = {}