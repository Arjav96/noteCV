import sys, time, MySQLdb, thread
from PyQt4 import QtGui, QtCore
from UIconstants import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import Main as Main

#####################################################################################################

# Adding fromUtf8

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

#######################################################################################################


# Global method to create database
def createDatabase(passwd):

#	data_base = '"Mydb2"'
	username = 'root'
	password = passwd

	db = MySQLdb.connect(host='localhost',user='root', passwd=password)
	connection = db.cursor()
	connection.execute('SHOW DATABASES LIKE "noteCV";')
	results = connection.fetchall()
	if len(results) == 0:
		connection.execute('CREATE DATABASE IF NOT EXISTS noteCV;')
		connection.execute("CREATE TABLE noteCV.USERS (USERNAME VARCHAR(30) NOT NULL PRIMARY KEY, PASSWORD VARCHAR(30));")
		connection.execute("CREATE TABLE noteCV.NOTES (fpath VARCHAR(100), fname VARCHAR(60), subject VARCHAR(50));")
		connection.execute("CREATE TABLE noteCV.subjects (Subject VARCHAR(40) NOT NULL);")
		connection.execute("INSERT INTO noteCV.USERS VALUES('user','user');")
		db.commit()

#	db.close()

subjectArray = []
alltopics = []
allLabels = []

#########################################################################################################

# Class that defines the Main Login Window
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
		self.passwdInp.setEchoMode(QtGui.QLineEdit.Password)
		self.passwdInp.move(675,370)
		self.passwdInp.resize(400,50)
		self.passwdInp.setFont(font2)
		

		# Login Button

		self.loginBtn = QtGui.QPushButton('LOGIN',self)
		self.loginBtn.move(600,500)
		self.loginBtn.resize(200,50)
		self.loginBtn.clicked.connect( lambda: self.verifyLogin(self.unameInp, self.passwdInp, parent))
		
	# A method that verifies Login details
	def verifyLogin(self, unameInp, passwdInp, parent):


		username = self.unameInp.text()
		password = self.passwdInp.text()

		global dbPassword
		db = MySQLdb.connect("localhost", "root", dbPassword, "noteCV")
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
	
##################################################################################################################

# Class that defines Main Window of the Application
class MainWindow(QtGui.QMainWindow):

	def __init__(self):

		super(MainWindow, self).__init__()
		self.startUI()

	def startUI(self):

		# self.LoginWidget = Dashboard('Himanshu',self)
		self.LoginWidget = Window(self)
		self.setStyleSheet('background-color:white;')
		self.move(0,0)
		self.resize(WIDTH,HEIGHT)
		self.setCentralWidget(self.LoginWidget)


##########################################################################################################

# A Class that inherits QWidgets and defines the side-bar holding various Subjects
class SubjectWidget(QtGui.QWidget):

	def __init__(self, ls, parent=None):

		super(SubjectWidget, self).__init__(parent)
		self.startUI(ls,parent)

	def startUI(self,ls,parent):

		self.setGeometry(30,190,200,500)
		self.layout = QtGui.QVBoxLayout()
		self.show()

		buttons = []
		for subject in ls:
			buttons.append(QtGui.QPushButton(subject,self))

		x = 0
		for btn in buttons:
			btn.resize(180,60)
			btn.move(10,x*60)
			btn.setStyleSheet('height: 50px; border: 2px SOLID black;')
			self.layout.addWidget(btn)
			btn.clicked.connect(lambda: self.showNotes(btn,parent))
			x += 1

		self.setLayout(self.layout)

	# The onclick listener which triggers the display of previous notes of a subject
	def showNotes(self, subject, parent):
		senderBtn = self.sender()
		noteWidget = NoteWidget(senderBtn.text(),parent)

#######################################################################################################

# The class that defnes the widget for display of previous notes
class NoteWidget(QtGui.QWidget):

	def __init__(self,subject,parent=None):

		super(NoteWidget, self).__init__(parent)
		self.buildUI(subject)

	def buildUI(self, subject):

		self.setGeometry(240,190,WIDTH-220,HEIGHT-190)
		self.show()

		global dbPassword
		db = MySQLdb.connect("localhost", "root", dbPassword, "noteCV")
		connection = db.cursor()
		temp = connection.execute("SELECT fname,fpath FROM NOTES WHERE Subject=%s;",(subject))
		results = connection.fetchall()
		db.close()

		buttons = []
		fnames = []
		fpaths = []

		global alltopics, allLabels

		if len(alltopics) > 0:
			for i in alltopics:
				i.setParent(None)

		if len(allLabels) > 0:
			for i in allLabels:
				i.setParent(None)
			allLabels = []

		for result in results:

			fnames.append(result[0])
			fpaths.append(result[1])
			button = QtGui.QPushButton("",self)
			buttons.append(button)
			buttonToAddress[button] = (result[0],result[1])
			button.clicked.connect(lambda: self.openEditor(subject))


		alltopics = buttons

		x = 60
		y = 40
		i = 0
		for button in buttons:
			button.resize(50,64)
			button.move(x,y)
			button.setStyleSheet('border:None;background-image:url("./images/icons/icon1.png");')
			self.label = QtGui.QLabel(fnames[i],self)
			allLabels.append(self.label)
			self.label.move(x,y+70)
			self.label.resize(100,50)
			self.label.setWordWrap(True)
			self.label.setFont(fontSmall)
			self.label.show() # Remove previous
			button.show()
			x += 120
			if x >= 1140:
				y += 140
				x = 60
			i += 1

		# The button to add new note
		self.addNewNoteBtn = QtGui.QPushButton('', self)
		self.addNewNoteBtn.move(x,y)
		self.addNewNoteBtn.resize(70,70)
		self.addNewNoteBtn.setFont(font1)
		self.addNewNoteBtn.clicked.connect(lambda: self.addNote(subject))
		self.addNewNoteBtn.setStyleSheet('border:None;background-image:url("./images/icons/icon2.png");')
		self.addNewNoteBtn.show()
		alltopics.append(self.addNewNoteBtn)

	# Launching the editor application
	def addNote(self,subject):
		
		editorWindow = Main.Editor(subject)
#		editorWindow = Main.Editor()
		editorWindow.exec_()

	# Launching Editor Application for existing files
	def openEditor(self, subject):

		senderBtn = self.sender()
		# print (buttonToAddress[senderBtn][0])
		newEditor = Main.Editor(subject, buttonToAddress[senderBtn][1])
		newEditor.exec_()


#######################################################################################################

# The Home page of a user after logging-in
class Dashboard(QtGui.QWidget):

	subjectCount = 0
	global subjectArray

	def __init__(self,username,parent=None):

		super(Dashboard, self).__init__(parent)
		self.startUI(username)

	def startUI(self,username):
		self.setGeometry(0,0,WIDTH,HEIGHT)
		self.setWindowTitle('Dashboard')

		# Header Message Display
		self.headerMessage = QtGui.QLabel('NoteCV',self)
		self.headerMessage.move(500,30)
		self.headerMessage.resize(450,50)
		self.headerMessage.setFont(fontCSL)
		self.headerMessage.setStyleSheet('color:black;border:3px SOLID black;padding-left:150px;')

		#username

		self.userNameLabel = QtGui.QLabel('Hello '+username+'!',self)
		self.userNameLabel.move(70,40)
		self.userNameLabel.resize(400,50)
		self.userNameLabel.setFont(font1)

		self.subjectCount = self.displaySubjects()

		self.addNewBtn = QtGui.QPushButton('Add New Subject',self)
		self.addNewBtn.move(40,120)
		self.addNewBtn.setStyleSheet('width:200;height:50;background-color:black;color:white;')
		self.addNewBtn.clicked.connect(lambda: self.addNewSubject())
		self.addNewBtn.setFont(font1)

		self.searchBar = QtGui.QLineEdit(self)
		self.searchBar.setStyleSheet('width:600;height:30;border:2px SOLID black;')
		self.searchBar.move(300,140)

		self.searchBtn = QtGui.QPushButton('Search',self)
		self.searchBtn.move(910,137)
		self.searchBtn.setStyleSheet('width:200;height:30;background-color: black;color:white')
		self.searchBtn.setFont(font1)


	# A method that displays currently added subjects
	def displaySubjects(self):

		global dbPassword
		db = MySQLdb.connect("localhost", "root", dbPassword, "noteCV")
		connection = db.cursor()
		temp = connection.execute("SELECT * FROM subjects;")
		result = connection.fetchall()
		db.close()

		x = 0
		ls = []
		for subject in result:
			ls.append(subject[0])

		if len(subjectArray) > 0:
			subjectArray[0].setParent(None)
			subjectArray.pop(0)

		self.subjectWidget = SubjectWidget(ls,self)
		subjectArray.append(self.subjectWidget)

		return len(result)
		
	# A method that adds a new Subject to the Database
	def addNewSubject(self):

		newSubject, ret = QtGui.QInputDialog.getText(self, 'Input', 'Enter New Subject Name')

		if newSubject == '' or newSubject == ' ':
			return
		global dbPassword
		db = MySQLdb.connect("localhost", "root", dbPassword, "noteCV")
		connection = db.cursor()
		connection.execute("INSERT INTO subjects VALUES(%s);",(newSubject))
		db.commit()
		db.close()
		QtGui.QApplication.processEvents()
		self.update()
		self.displaySubjects()

###########################################################################################################

# The main function
def main(pw):

	createDatabase(pw)
	mainApplication = QtGui.QApplication(sys.argv)
	LoginWindow = MainWindow()
	LoginWindow.show()
	sys.exit(mainApplication.exec_())



if len(sys.argv) < 2:
	print ("Please enter python run.py <your password>")
	sys.exit()

dbPassword = sys.argv[1]
main(sys.argv[1])
