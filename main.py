import sys, time, MySQLdb
from PyQt4 import QtGui, QtCore
from constants import *

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

	def __init__(self):

		super(Window, self).__init__()
		self.initUI()

	def initUI(self):

		# Setting Main Window
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
		headerMessage = QtGui.QLabel('Login To Your NoteCV Account',self)
		headerMessage.move(370,150)
		headerMessage.resize(650,50)
		headerMessage.setFont(headerFont)
		headerMessage.show()

		# UserName and Password font
		font1 = QtGui.QFont()
		font1.setFamily(_fromUtf8("Sawasdee"))
		font1.setPointSize(28)
		font1.setBold(True)
		font1.setWeight(75)

		# Display Username Label
		userNameLabel = QtGui.QLabel('Username',self)
		userNameLabel.move(425,270)
		userNameLabel.resize(200,50)
		userNameLabel.setFont(font1)
		userNameLabel.show()

		# Display Password Label
		passwordLabel = QtGui.QLabel('Password',self)
		passwordLabel.move(425,370)
		passwordLabel.resize(200,50)
		passwordLabel.setFont(font1)
		passwordLabel.show()

		# Configuring Input Field Fonts
		font2 = QtGui.QFont()
		font1.setFamily(_fromUtf8("Monospace"))
		font1.setPointSize(32)
		font1.setBold(True)
		font1.setWeight(75)

		# Username Input Field

		unameInp = QtGui.QLineEdit(self)
		unameInp.move(675,270)
		unameInp.resize(400,50)
		unameInp.setFont(font2)
		unameInp.show()

		# Password Input Field

		passwdInp = QtGui.QLineEdit(self)
		passwdInp.move(675,370)
		passwdInp.resize(400,50)
		passwdInp.setFont(font2)
		passwdInp.show()
		

		# Login Button

		loginBtn = QtGui.QPushButton('LOGIN',self)
		loginBtn.move(600,500)
		loginBtn.resize(200,50)
		loginBtn.show()
		loginBtn.clicked.connect( lambda: self.verifyLogin(unameInp, passwdInp))

	def verifyLogin(self, unameInp, passwdInp):


		username = unameInp.text()
		password = passwdInp.text()

		db = MySQLdb.connect("localhost", "root", "mosfet", "noteCV")
		connection = db.cursor()
	#	insertIntoDB()
		result = connection.execute("SELECT * FROM USERS WHERE USERNAME = %s AND PASSWORD = %s",(username, password))
		if(len(connection.fetchall()) > 0):
			print "User Found!"
		else:
			print('kjlksf')
		




def main():

#	createDatabase()
	mainApplication = QtGui.QApplication(sys.argv)
	LoginWindow = Window()
	sys.exit(mainApplication.exec_())


if __name__ == '__main__':
	main()