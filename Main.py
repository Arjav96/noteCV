import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from constants import *
import opencv as opencv

class TextEditor(QtGui.QTextEdit) :
	# class for the main editor window
	# Inherited from QTextEdit

	def __init__(self, parent = None) :
		super(TextEditor,self).__init__(parent)

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

	def setBoldFont(self) :
		if self.fontWeight() != QFont.Black :
			self.setFontWeight(QFont.Black)
		else :
			self.setFontWeight(QFont.Normal)

	def setItalicFont(self) :
		self.setFontItalic(not self.fontItalic())

	def setUnderlineFont(self) :
		self.setFontUnderline(not self.fontUnderline())

	def setLeftAlign(self) :
		self.setAlignment(QtCore.Qt.AlignLeft)

	def setCenterAlign(self) :
		self.setAlignment(QtCore.Qt.AlignCenter)

	def setRightAlign(self) :
		self.setAlignment(QtCore.Qt.AlignRight)

	def setHighlight(self) :
		if self.textBackgroundColor() != QtGui.QColor(255,255,0) :
			self.setTextBackgroundColor(QtGui.QColor(255,255,0))
		else :
			self.setTextBackgroundColor(QtGui.QColor(255,255,255))

	def addDiagram(self) :

		loc = opencv.draw("maths", 1)
		print(loc)
		image = QtGui.QImage(loc, 'JPG')
		cursor = QtGui.QTextCursor(self.document())
		cursor.movePosition(QtGui.QTextCursor.End,QtGui.QTextCursor.MoveAnchor)
		cursor.insertImage(image, loc)
		#cursor.insertImage(QtCore.QString(loc))

	def addGraph(self) :
		loc = opencv.draw("maths", 2)
		print(loc)
		image = QtGui.QImage(loc, 'JPG')
		cursor = QtGui.QTextCursor(self.document())
		cursor.movePosition(QtGui.QTextCursor.End,QtGui.QTextCursor.MoveAnchor)
		cursor.insertImage(image, loc)
		return

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
		self.textEditor.move(STARTPOSEDITOR[0], STARTPOSEDITOR[1])
		self.textEditor.resize(WIDTH - STARTPOSEDITOR[0]-40, HEIGHT-STARTPOSEDITOR[1]-40)

	def createQuickAccessToolbar(self) :
		# Create quick access tooolbar for easy access

		# Heading button
		self.headingBtn = QtGui.QPushButton("HEADING",self)
		self.headingBtn.clicked.connect(self.textEditor.setHeadingFormat)
		self.headingBtn.move(20,STARTPOSEDITOR[1]+10)
		self.headingBtn.resize(STARTPOSEDITOR[0]-35, 40)

		# Sub Heading Button
		self.subHeadingBtn = QtGui.QPushButton("SUB HEADING",self)
		self.subHeadingBtn.clicked.connect(self.textEditor.setSubHeadingFormat)
		self.subHeadingBtn.move(20,STARTPOSEDITOR[1]+10+60)
		self.subHeadingBtn.resize(STARTPOSEDITOR[0]-35, 40)

		# Paragraph Button
		self.paragraphBtn = QtGui.QPushButton("PARAGRAPH",self)
		self.paragraphBtn.clicked.connect(self.textEditor.setParagraphFormat)
		self.paragraphBtn.move(20,STARTPOSEDITOR[1]+10+60+60)
		self.paragraphBtn.resize(STARTPOSEDITOR[0]-35, 40)

		# Bold Button
		self.boldBtn = QtGui.QPushButton("",self)
		self.boldBtn.clicked.connect(self.textEditor.setBoldFont)
		self.boldBtn.move(20,STARTPOSEDITOR[1]+10+60+60+60)
		self.boldBtn.resize(40, 40)
		self.boldBtn.setIcon(QtGui.QIcon('./images/icons/bold.png'))
		self.boldBtn.setIconSize(QtCore.QSize(35,35))

		# Italics Button
		self.italicBtn = QtGui.QPushButton("",self)
		self.italicBtn.clicked.connect(self.textEditor.setItalicFont)
		self.italicBtn.move(84,STARTPOSEDITOR[1]+10+60+60+60)
		self.italicBtn.resize(40, 40)
		self.italicBtn.setIcon(QtGui.QIcon('./images/icons/italics.png'))
		self.italicBtn.setIconSize(QtCore.QSize(20,20))


		# UnderLine button
		self.underlineBtn = QtGui.QPushButton("",self)
		self.underlineBtn.clicked.connect(self.textEditor.setUnderlineFont)
		self.underlineBtn.move(73+73,STARTPOSEDITOR[1]+10+60+60+60)
		self.underlineBtn.resize(40, 40)
		self.underlineBtn.setIcon(QtGui.QIcon('./images/icons/underline.png'))
		self.underlineBtn.setIconSize(QtCore.QSize(25,25))


		# Left alignment :)
		self.leftBtn = QtGui.QPushButton("",self)
		self.leftBtn.clicked.connect(self.textEditor.setLeftAlign)
		self.leftBtn.move(20,STARTPOSEDITOR[1]+10+60+60+60+60)
		self.leftBtn.resize(40, 40)
		self.leftBtn.setIcon(QtGui.QIcon('./images/icons/left-align.png'))
		self.leftBtn.setIconSize(QtCore.QSize(35,35))

		# Center align button
		self.centerBtn = QtGui.QPushButton("",self)
		self.centerBtn.clicked.connect(self.textEditor.setCenterAlign)
		self.centerBtn.move(84,STARTPOSEDITOR[1]+10+60+60+60+60)
		self.centerBtn.resize(40, 40)
		self.centerBtn.setIcon(QtGui.QIcon('./images/icons/center-align.png'))
		self.centerBtn.setIconSize(QtCore.QSize(34,34))

		# Right button
		self.rightBtn = QtGui.QPushButton("",self)
		self.rightBtn.clicked.connect(self.textEditor.setRightAlign)
		self.rightBtn.move(73+73,STARTPOSEDITOR[1]+10+60+60+60+60)
		self.rightBtn.resize(40, 40)
		self.rightBtn.setIcon(QtGui.QIcon('./images/icons/right-align.png'))
		self.rightBtn.setIconSize(QtCore.QSize(34,34))

		# Highlight button
		self.highlightBtn = QtGui.QPushButton("HIGHLIGHT",self)
		self.highlightBtn.clicked.connect(self.textEditor.setHighlight)
		self.highlightBtn.move(20,STARTPOSEDITOR[1]+10+60+60+60+60+60)
		self.highlightBtn.resize(STARTPOSEDITOR[0]-35, 40)


		# Add diagram button
		self.diagramBtn = QtGui.QPushButton("ADD DIAGRAM",self)
		self.diagramBtn.clicked.connect(self.textEditor.addDiagram)
		self.diagramBtn.move(20,STARTPOSEDITOR[1]+10+60+60+60+60+60+120)
		self.diagramBtn.resize(STARTPOSEDITOR[0]-35, 60)


		# Add graph button
		self.graphBtn = QtGui.QPushButton("ADD GRAPH",self)
		self.graphBtn.clicked.connect(self.textEditor.addGraph)
		self.graphBtn.move(20,STARTPOSEDITOR[1]+10+60+60+60+60+60+100+100)
		self.graphBtn.resize(STARTPOSEDITOR[0]-35, 60)

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