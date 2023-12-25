#Program for Squaring of the given number coming from client side program
#ServerSquare.py
import socket
s=socket.socket()
s.bind( ("localhost",8888) )
s.listen(2)
print("Server Side Program is ready to accept any client request:")
while(True):
	try:
		clientobj,clientaddr=s.accept()
		cdata=clientobj.recv(1024).decode()
		print("Val of Client at Server={}".format(cdata))
		val=float(cdata)
		result=val**2
		clientobj.send(str(result).encode())
	except ValueError:
		clientobj.send("Don'enter strs, symbols, alpha-numerics".encode() )





