import sys, time, MySQLdb
from PyQt4 import QtGui, QtCore
from constants import *
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
		self.startUI(ls)

	def startUI(self,ls):

		self.setGeometry(10,170,200,500)
		self.layout = QtGui.QVBoxLayout()
		self.show()

		# self.listBox = QVBoxLayout(self)
		# self.setLayout(self.listBox)
		# self.scroll = QScrollArea(self)
		# self.listBox.addWidget(self.scroll)
		# self.scroll.setWidgetResizable(True)
		# self.scrollContent = QWidget(self.scroll)

		# self.scrollLayout = QVBoxLayout(self.scrollContent)
		# self.scrollContent.setLayout(self.scrollLayout)
		# self.scroll.setWidget(self.scrollContent)

		x = 0
		for subject in ls:
			self.subLabel = QtGui.QLabel(subject,self)
			self.subLabel.resize(180,50)
			self.subLabel.move(10,x*60)
			self.subLabel.setStyleSheet('color: white; border: 2px SOLID black; border-radius:5px;')
			self.layout.addWidget(self.subLabel)
			x += 1

		self.setLayout(self.layout)


class Dashboard(QtGui.QWidget):

	subjectCount = 0

	font1 = QtGui.QFont()
	font1.setFamily(_fromUtf8("Sawasdee"))
	font1.setPointSize(16)
	font1.setBold(True)
	font1.setWeight(75)

	def __init__(self,username,parent=None):

		super(Dashboard, self).__init__(parent)
		self.startUI(username)
		print(username)

	def startUI(self,username):
		self.setGeometry(10,10,400,400)
		self.setWindowTitle('Dashboard')

	#	self.dashBoardLayout = QtGui.QGridLayout()

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

	#	self.dashBoardLayout.addWidget(self.headerMessage)

		#username

		self.userNameLabel = QtGui.QLabel('Hello '+username+'!',self)
		self.userNameLabel.move(100,40)
		self.userNameLabel.resize(400,50)
		self.userNameLabel.setFont(self.font1)

	#	self.dashBoardLayout.addWidget(self.userNameLabel)

		self.subjectCount = self.displaySubjects()

		self.addNewBtn = QtGui.QPushButton('Add New Subject',self)
		self.addNewBtn.move(10,100)
		self.addNewBtn.resize(200,50)
		self.addNewBtn.clicked.connect(lambda: self.addNewSubject())

		# The button to add new note
		self.addNewNoteBtn = QtGui.QPushButton('Add New Note', self)
		self.addNewNoteBtn.move(500,400)
		self.addNewNoteBtn.resize(200,200)
		self.addNewNoteBtn.setFont(self.font1)
		self.addNewNoteBtn.clicked.connect(self.addNote)
		self.addNewNoteBtn.setStyleSheet('border: 1px SOLID black ; border-radius: 100px;')

	#	self.dashBoardLayout.addWidget(self.addNewBtn)
	#	self.setLayout(self.dashBoardLayout)


	def displaySubjects(self):

		db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
		connection = db.cursor()
		temp = connection.execute("SELECT * FROM subjects")
		result = connection.fetchall()

		x = 0
		ls = []
		for subject in result:
			ls.append(subject[0])
			# self.subLabel = QtGui.QLabel(subject[0],self)
			# self.subLabel.resize(200,50)
			# self.subLabel.move(10,170+x*60)
			
			# x += 1

		db.close()

		self.subjectWidget = SubjectWidget(ls,self)
		self.subjectWidget.setStyleSheet('background-color: red')

		# self.scrollBar = QtGui.QScrollArea(self)
		# self.scrollBar.setWidgetResizable(True)



		print(len(result))
		return len(result)
		
	def addNewSubject(self):

		newSubject, ret = QtGui.QInputDialog.getText(self, 'Input', 'Enter New Subject Name')

		if newSubject == "":
			return

		db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
		connection = db.cursor()
		connection.execute("INSERT INTO subjects VALUES(%s);",(newSubject))
		db.commit()
		db.close()
		QtGui.QApplication.processEvents()
		self.update()
		self.displaySubjects()


	def addNote(self):
		return



def main():

	mainApplication = QtGui.QApplication(sys.argv)
	LoginWindow = MainWindow()
	LoginWindow.show()
	sys.exit(mainApplication.exec_())


if __name__ == '__main__':
	main()