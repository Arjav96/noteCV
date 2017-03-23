import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from constants import *

class TextEditor(QtGui.QTextEdit) :
	# class for the main editor window
	# Inherited from QTextEdit

	def __init__(self, parent = None) :
		super(TextEditor,self).__init__(parent)

		self.resize(800,500)

		font = self.font()
		font.setPointSize(PARAFONT)
		self.setFont(font)
		self.setFontPointSize(PARAFONT)

	def setHeadingFormat(self) :
		self.setFontWeight(QFont.Black)
		self.setFontPointSize(HEADFONT)
		self.setAlignment(QtCore.Qt.AlignCenter)

	def setSubHeadingFormat(self) :
		self.setFontWeight(55)
		self.setFontPointSize(SUBHEADFONT)		
		self.setAlignment(QtCore.Qt.AlignLeft)

	def setParagraphFormat(self) :
		self.setFontWeight(QFont.Normal)
		self.setFontPointSize(PARAFONT)		
		self.setAlignment(QtCore.Qt.AlignLeft)


class Widget(QtGui.QWidget) :
	# Widget class inherited from QWidget
	# Only to create a central Widget

	def __init__(self, parent = None) :
		super(Widget, self).__init__(parent)
		self.createTextEditor()
		self.createQuickAccessToolbar()

	def createTextEditor(self) :
		# Create text editor of the 
		self.textEditor = TextEditor(self)

	def createQuickAccessToolbar(self) :
		# Create quick access tooolbar for easy access
		self.headingBtn = QtGui.QPushButton("HEADING",self)
		self.headingBtn.clicked.connect(self.textEditor.setHeadingFormat)
		self.headingBtn.move(0,500)

		self.subHeadingBtn = QtGui.QPushButton("SUB HEADING",self)
		self.subHeadingBtn.clicked.connect(self.textEditor.setSubHeadingFormat)
		self.subHeadingBtn.move(100,500)

		self.paragraphBtn = QtGui.QPushButton("PARAGRAPH",self)
		self.paragraphBtn.clicked.connect(self.textEditor.setParagraphFormat)
		self.paragraphBtn.move(200,500)

 
class Editor(QtGui.QMainWindow) :

	def __init__(self, parent = None) :
		super(Editor, self).__init__(parent)
		self.makeUI()

	def makeUI(self) :
		self.textWidget = Widget(self)
		self.move(0,0)
		self.resize(WIDTH, HEIGHT)
		self.setCentralWidget(self.textWidget)		

def main() :
	app = QtGui.QApplication(sys.argv)
	editorWindow = Editor()
	editorWindow.show()
	sys.exit(app.exec_())

main()