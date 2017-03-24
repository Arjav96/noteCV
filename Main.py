import sys, MySQLdb
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from UIconstants import *
import opencv as opencv

gSubject = None

class TextEditor(QtGui.QTextEdit) :
	# class for the main editor window
	# Inherited from QTextEdit

	def __init__(self, parent = None) :
		super(TextEditor,self).__init__(parent)
		font = self.font()
		font.setPointSize(PARAFONT)
		self.setFont(font)
		self.setFontPointSize(PARAFONT)

	# Heading format
	def setHeadingFormat(self) :
		self.setFontWeight(QFont.Black)
		self.setFontPointSize(HEADFONT)
		self.setAlignment(QtCore.Qt.AlignCenter)

	# Sub Heading format
	def setSubHeadingFormat(self) :
		self.setFontWeight(55)
		self.setFontPointSize(SUBHEADFONT)		
		self.setAlignment(QtCore.Qt.AlignLeft)

	# Paragraph format
	def setParagraphFormat(self) :
		self.setFontWeight(QFont.Normal)
		self.setFontPointSize(PARAFONT)		
		self.setAlignment(QtCore.Qt.AlignLeft)

	# Bold format
	def setBoldFont(self) :
		if self.fontWeight() != QFont.Black :
			self.setFontWeight(QFont.Black)
		else :
			self.setFontWeight(QFont.Normal)

	# Italic format
	def setItalicFont(self) :
		self.setFontItalic(not self.fontItalic())

	# Underline format
	def setUnderlineFont(self) :
		self.setFontUnderline(not self.fontUnderline())

	# Left Align format
	def setLeftAlign(self) :
		self.setAlignment(QtCore.Qt.AlignLeft)

	# Center Align format
	def setCenterAlign(self) :
		self.setAlignment(QtCore.Qt.AlignCenter)

	# Right Align format
	def setRightAlign(self) :
		self.setAlignment(QtCore.Qt.AlignRight)

	# Highlight format
	def setHighlight(self) :
		if self.textBackgroundColor() != QtGui.QColor(255,255,0) :
			self.setTextBackgroundColor(QtGui.QColor(255,255,0))
		else :
			self.setTextBackgroundColor(QtGui.QColor(255,255,255))

	# Add diagram code
	def addDiagram(self) :

		global gSubject
		loc = opencv.draw(gSubject, 1)
		print(loc)
		image = QtGui.QImage(loc, 'JPG')
		cursor = QtGui.QTextCursor(self.document())
		cursor.movePosition(QtGui.QTextCursor.End,QtGui.QTextCursor.MoveAnchor)
		cursor.insertImage(image, loc)
		#cursor.insertImage(QtCore.QString(loc))

	# Subroutine for adding graph api :: made by baba ;P
	def addGraph(self) :
		loc = opencv.draw(gSubject, 2)
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

	gParent = None

	def __init__(self, subject = None, filename = "", parent = None) :
		super(Editor, self).__init__(parent)

		global gParent, gSubject
		
		gParent = parent
		gSubject = subject
		self.filename = filename
		self.changesSaved = False
		self.makeUI()
		self.openFile(filename)

	def makeUI(self) :
		self.textWidget = Widget(self)
		self.move(0,0)
		self.resize(WIDTH, HEIGHT)
		self.setCentralWidget(self.textWidget)	
		self.show()

# def main() :
# 	app = QtGui.QApplication(sys.argv)
# 	print("Buffalo")
# 	sys.exit(app.exec_())

# # main()
		self.setCentralWidget(self.textWidget)
 
		#################################################################################
		## Defining Quick access toolbar
		## Features : Open Save Undo Redo
		## Future development : Font, Font size, color, etc
		#################################################################################

		self.actionSave = QtGui.QAction(QtGui.QIcon("./images/icons/save.png"), "", self) 
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSave.triggered.connect(self.performSave)

		self.actionOpen = QtGui.QAction(QtGui.QIcon("./images/icons/open.png"), "", self) 
		self.actionOpen.setShortcut("Ctrl+O")
		self.actionOpen.triggered.connect(self.performOpen)

		self.actionUndo = QtGui.QAction(QtGui.QIcon("./images/icons/undo.ico"), "", self) 
		self.actionUndo.setShortcut("Ctrl+Z")
		self.actionUndo.triggered.connect(self.performUndo)

		self.actionRedo = QtGui.QAction(QtGui.QIcon("./images/icons/redo.png"), "", self) 
		self.actionRedo.setShortcut("Ctrl+Y")
		self.actionRedo.triggered.connect(self.performRedo)

		self.toolbar = self.addToolBar("QuickAccessToolbar")
		self.toolbar.addAction(self.actionOpen)
		self.toolbar.addAction(self.actionSave)
		self.toolbar.addAction(self.actionUndo)
		self.toolbar.addAction(self.actionRedo)

	def changed(self) :
		self.changesSaved = False

	def closeEvent(self,event):
		if self.changesSaved:
			event.accept()
		else:
			confirmExitWindow = QtGui.QMessageBox(self)
			confirmExitWindow.setIcon(QtGui.QMessageBox.Warning)
			confirmExitWindow.setText("Changes occured!!!")

			confirmExitWindow.setInformativeText("Do you want to save your changes?")
			confirmExitWindow.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Discard)
			confirmExitWindow.setDefaultButton(QtGui.QMessageBox.Save)

			answer = confirmExitWindow.exec_()

			if answer == QtGui.QMessageBox.Save:
				self.performSave()
			elif answer == QtGui.QMessageBox.Discard:
				event.accept()
			else:
				event.ignore()


	def openFile(self,filename) :
		with open(self.filename,"rt") as file:
			self.textWidget.textEditor.setText(file.read())

	def performSave(self):

		global gSubject

		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

		if self.filename:
		    # Append extension if not there yet
			if not str(self.filename).endswith(".html"):
				self.filename += ".html"

			with open(self.filename,"wt") as file:
				file.write(self.textWidget.textEditor.toHtml())

			self.changesSaved = True

			db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
			connection = db.cursor()
			temp = connection.execute("SELECT fname,subject FROM NOTES WHERE fpath=%s and Subject=%s;",(str(self.filename),str(gSubject)))
			results = connection.fetchall()
			if len(results) == 0:

				fname = (self.filename.split('.')[0]).split('/')[-1]
				print(str(self.filename), str(fname), str(gSubject))
				connection.execute("INSERT INTO NOTES VALUES(%s, %s, %s);",(str(self.filename), str(fname), str(gSubject)))
				db.commit()

			print('Here')
			db.close()


	def performOpen(self) :
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.html)")

		if self.filename:
			with open(self.filename,"rt") as file:
				self.textWidget.textEditor.setText(file.read())

	def performUndo(self) :
		self.textWidget.textEditor.undo()		

	def performRedo(self) :
		self.textWidget.textEditor.redo()		


##############################################

# def main() :
# 	# app = QtGui.QApplication(sys.argv)
# 	editorWindow = Editor("maths")
# 	editorWindow.show()
# 	# sys.exit(app.exec_())
