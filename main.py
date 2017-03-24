import sys, time, MySQLdb
from PyQt4 import QtGui, QtCore
from constants1 import *
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


def createDatabase():

	db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
	connection = db.cursor()
	connection.execute("CREATE TABLE USERS(USERNAME VARCHAR(30) NOT NULL PRIMARY KEY, PASSWORD VARCHAR(30));")
	db.close()

def insertIntoDB():

	db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
	connection = db.cursor()
	connection.execute("INSERT INTO USERS(USERNAME, PASSWORD) VALUES(?,?)",("Himanshu", "Pt"))
	db.commit()
	db.close()

subjectArray = []


class Window(QtGui.QWidget):

	status = False

	def __init__(self, parent=None):

		super(Window, self).__init__(parent)
		self.initUI(parent)

	def initUI(self,parent):

		# Setting Main Widget
		self.setGeometry(STARTWINDOW[0], STARTWINDOW[1], WIDTH, HEIGHT)
		self.setWindowTitle(mainTitle)
		self.show()

		# Configuring Header Font 
		headerFont = QtGui.QFont()
		headerFont.setFamily(_fromUtf8("Sawasdee"))
		headerFont.setPointSize(32)
		headerFont.setBold(True)
		headerFont.setWeight(75)

		# Header Message Display
		self.headerMessage = QtGui.QLabel('Login To Your NoteCV Account',self)
		self.headerMessage.move(370,150)
		self.headerMessage.resize(650,50)
		self.headerMessage.setFont(headerFont)

		# UserName and Password font
		font1 = QtGui.QFont()
		font1.setFamily(_fromUtf8("Sawasdee"))
		font1.setPointSize(28)
		font1.setBold(True)
		font1.setWeight(75)

		# Display Username Label
		self.userNameLabel = QtGui.QLabel('Username',self)
		self.userNameLabel.move(425,270)
		self.userNameLabel.resize(200,50)
		self.userNameLabel.setFont(font1)

		# Display Password Label
		self.passwordLabel = QtGui.QLabel('Password',self)
		self.passwordLabel.move(425,370)
		self.passwordLabel.resize(200,50)
		self.passwordLabel.setFont(font1)

		# Configuring Input Field Fonts
		font2 = QtGui.QFont()
		font1.setFamily(_fromUtf8("Monospace"))
		font1.setPointSize(32)
		font1.setBold(True)
		font1.setWeight(75)

		# Username Input Field

		self.unameInp = QtGui.QLineEdit(self)
		self.unameInp.move(675,270)
		self.unameInp.resize(400,50)
		self.unameInp.setFont(font2)

		# Password Input Field

		self.passwdInp = QtGui.QLineEdit(self)
		self.passwdInp.move(675,370)
		self.passwdInp.resize(400,50)
		self.passwdInp.setFont(font2)
		

		# Login Button

		self.loginBtn = QtGui.QPushButton('LOGIN',self)
		self.loginBtn.move(600,500)
		self.loginBtn.resize(200,50)
		self.loginBtn.clicked.connect( lambda: self.verifyLogin(self.unameInp, self.passwdInp, parent))
		

	def verifyLogin(self, unameInp, passwdInp, parent):


		username = self.unameInp.text()
		password = self.passwdInp.text()

		db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
		connection = db.cursor()
	
		result = connection.execute("SELECT * FROM USERS WHERE USERNAME = %s AND PASSWORD = %s",(username, password))
		if(len(connection.fetchall()) > 0):
			print "User Found!"
			NewWindow = Dashboard(username)
			parent.setCentralWidget(NewWindow)

		else:
			messageBox = QtGui.QMessageBox()
			messageBox.setIcon(QMessageBox.Warning)
			messageBox.setText('Incorrect Username or Password!')
			messageBox.setWindowTitle('Login Failed')
			messageBox.exec_()
			self.status = False
	

class MainWindow(QtGui.QMainWindow):

	def __init__(self):

		super(MainWindow, self).__init__()
		self.startUI()

	def startUI(self):

		self.LoginWidget = Dashboard('Himanshu',self)
		self.move(0,0)
		self.resize(WIDTH,HEIGHT)
		self.setCentralWidget(self.LoginWidget)

class SubjectWidget(QtGui.QWidget):

	def __init__(self, ls, parent=None):

		super(SubjectWidget, self).__init__(parent)
		self.startUI(ls,parent)

	def startUI(self,ls,parent):

		self.setGeometry(10,170,200,500)
		self.layout = QtGui.QVBoxLayout()
		self.show()

		buttons = []
		for subject in ls:
			buttons.append(QtGui.QPushButton(subject,self))

		x = 0
		for btn in buttons:
			btn.resize(180,60)
			btn.move(10,x*60)
			btn.setStyleSheet('height: 50px;color: white; border: 2px SOLID black; border-radius:5px;')
			self.layout.addWidget(btn)
			btn.clicked.connect(lambda: self.showNotes(btn,parent))
			x += 1

		self.setLayout(self.layout)

	def showNotes(self, subject, parent):
		senderBtn = self.sender()
		noteWidget = NoteWidget(senderBtn.text(),parent)


class NoteWidget(QtGui.QWidget):

	def __init__(self,subject,parent=None):

		super(NoteWidget, self).__init__(parent)
		self.buildUI(subject)

	def buildUI(self, subject):

		self.vertLayout = QtGui.QGridLayout()
	#	self.vertLayout.stretch(2)
		self.setGeometry(220,170,WIDTH-220,HEIGHT-170)
		self.show()
	#	self.setStyleSheet('border: 2px SOLID black;')
		print(subject)
		self.setLayout(self.vertLayout)

		# The button to add new note
		self.addNewNoteBtn = QtGui.QPushButton('Add New Note', self)
		self.addNewNoteBtn.move(300,300)
		self.addNewNoteBtn.resize(200,200)
		self.addNewNoteBtn.setFont(font1)
		self.addNewNoteBtn.clicked.connect(self.addNote)
		self.addNewNoteBtn.setStyleSheet('border: 1px SOLID black ; border-radius: 100px;')

		for i in xrange(0,5):
			self.vertLayout.setRowMinimumHeight(i,100)
			for j in xrange(0,10):
				# self.vertLayout.setColumnMinimumWidth(j,100)
				self.vertLayout.addWidget(QPushButton('btn',self), i, j, 10, 10)

		self.vertLayout.setColumnMinimumWidth(3,200)
#		self.vertLayout.setColumnStretch(4,5)

#		self.vertLayout.addWidget(self.addNewNoteBtn)

	def addNote(self):
		return


class Dashboard(QtGui.QWidget):

	subjectCount = 0
	global subjectArray

	def __init__(self,username,parent=None):

		super(Dashboard, self).__init__(parent)
		self.startUI(username)

	def startUI(self,username):
		self.setGeometry(10,10,400,400)
		self.setWindowTitle('Dashboard')

		headerFont = QtGui.QFont()
		headerFont.setFamily(_fromUtf8("Sawasdee"))
		headerFont.setPointSize(20)
		headerFont.setBold(True)
		headerFont.setWeight(75)

		# Header Message Display
		self.headerMessage = QtGui.QLabel('NoteCV',self)
		self.headerMessage.move(500,10)
		self.headerMessage.resize(650,50)
		self.headerMessage.setFont(headerFont)

		#username

		self.userNameLabel = QtGui.QLabel('Hello '+username+'!',self)
		self.userNameLabel.move(100,40)
		self.userNameLabel.resize(400,50)
		self.userNameLabel.setFont(font1)

		self.subjectCount = self.displaySubjects()

		self.addNewBtn = QtGui.QPushButton('Add New Subject',self)
		self.addNewBtn.move(10,100)
		self.addNewBtn.resize(200,50)
		self.addNewBtn.clicked.connect(lambda: self.addNewSubject())


	def displaySubjects(self):

		db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
		connection = db.cursor()
		temp = connection.execute("SELECT * FROM subjects")
		result = connection.fetchall()
		db.close()

		x = 0
		ls = []
		for subject in result:
			ls.append(subject[0])

		if len(subjectArray) > 0:
			subjectArray[0].setParent(None)
#			subjectArray[1].setParent(None)
#			subjectArray.pop(1)
			subjectArray.pop(0)

	#	self.scroll = QtGui.QScrollArea(self)
	#	self.scroll.setWidgetResizable(True)

		self.subjectWidget = SubjectWidget(ls,self)
		self.subjectWidget.setStyleSheet('background-color: red')
		subjectArray.append(self.subjectWidget)

	#	self.scrollwidget = self.subjectWidget
#		subjectArray.append(self.scrollwidget)
	#	self.scrollwidget.setGeometry(QtCore.QRect(10,200,200,400))
	#	self.scroll.setWidget(self.scrollwidget)

		print(len(result))
		return len(result)
		
	def addNewSubject(self):

		newSubject, ret = QtGui.QInputDialog.getText(self, 'Input', 'Enter New Subject Name')

		if newSubject == '' or newSubject == ' ':
			return

		db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
		connection = db.cursor()
		connection.execute("INSERT INTO subjects VALUES(%s);",(newSubject))
		db.commit()
		db.close()
		QtGui.QApplication.processEvents()
		self.update()
		self.displaySubjects()



def main():

	mainApplication = QtGui.QApplication(sys.argv)
	LoginWindow = MainWindow()
	LoginWindow.show()
	sys.exit(mainApplication.exec_())


if __name__ == '__main__':
	main()