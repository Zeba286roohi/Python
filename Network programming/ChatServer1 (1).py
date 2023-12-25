#ChatServer.py
import socket
#step-1
s=socket.socket()
s.bind(("localhost",11111) )
s.listen(2)
print("-"*50)
print("SSP is ready to accept any CSP request")
print("-"*50)
while(True):
	#step-2
	con,adr=s.accept()
	#step-3
	cdata=con.recv(1024).decode()
	print("Client Data at Server->{}".format(cdata))
	sdata=input("SSP Message to Client:")
	#step-4
	con.send(sdata.encode())






