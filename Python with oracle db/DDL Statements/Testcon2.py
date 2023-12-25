#This program test the connection with Oracle
#Testcon2.py
import cx_Oracle  # step-1
try:
	con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")   # step-2
except cx_Oracle.DatabaseError as db:
	print("\nProblem in database:", db)
else:
	print("\nType of con=",type(con))  #  <class 'cx_Oracle.Connection'>
	print("\nPython Program obtains connection from Oracle DB")
finally:
	con.close()   # step-6
	print("\nConnection Closed ")
