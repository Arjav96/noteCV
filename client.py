from socket import *

HOST = '127.0.0.1'
PORT = 9999
sock=socket(AF_INET,SOCK_STREAM)
sock.connect((HOST,PORT))

def compute():
	pass

#filepath, subj = compute()
filepath = "/home/ananya/a.cpp"
subj="qwerrt"

while True: 

	message = filepath + "##" + subj 
	sock.send(message)
	print "Awaiting reply" 
	reply = sock.recv(1024)
	 # 1024 is max data that can be received 
	print "Received ", repr(reply)

sock.close()
