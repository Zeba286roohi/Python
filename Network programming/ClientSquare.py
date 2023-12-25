#Program for sending a number to server side program and obtain Square of the given number coming from Server side program at client side program
#ClientSquare.py
import socket
s=socket.socket()
s.connect( ("localhost",8888))
print("Client Side Program got connection from Server Side Program")
n=input("Enter a number:")
s.send(n.encode())
sres=s.recv(1024).decode()
print("Result from Server at client={}".format(sres))

