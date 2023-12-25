#chatclient.py
import socket
#step-1
s=socket.socket()
#step-2
s.connect(("localhost",11111))
print("-"*50)
print("CSP got connected to  SSP")
print("-"*50)
#step-3
cdata=input("Enter Client Message:")
s.send(cdata.encode())
#step-4
sdata=s.recv(1024).decode()
print("SSP data at CSP-->{}".format(sdata))


