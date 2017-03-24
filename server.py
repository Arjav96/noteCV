from socket import *
import MySQLdb
import thread

def clientHandler(conn,addr):
	
	print addr, "is Connected"
	db = MySQLdb.connect("localhost","root","root","server" )

	# prepare a cursor object using cursor() method
	connection = db.cursor()
	while 1: 
		data = conn.recv(1024) 
		if not data: 
			break 
		print "Received Message", data
		value = data.split("##")
		#connection.execute("INSERT INTO subjects VALUES(%s);",(newSubject))
		connection.execute("INSERT INTO client(ip,filename,subject) VALUES(%s,%s,%s);",(addr[0], value[0],value[1]))

		print "yayay"
		db.commit()
	db.close()
	
HOST='127.0.0.1'
PORT=9991

sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('',PORT))
sock.listen(5)
while True:
	conn,addr=sock.accept()
	print(addr)
	thread.start_new_thread(clientHandler,(conn,addr))
