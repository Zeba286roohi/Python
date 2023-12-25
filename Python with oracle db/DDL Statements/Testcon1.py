#This program test the connection with Oracle
#Testcon1.py
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	print("\nType of con=",type(con))  #  <class 'cx_Oracle.Connection'>
	print("\nPython Program obtains connection from Oracle DB")
except cx_Oracle.DatabaseError as db:
	print("\nProblem in database:", db)