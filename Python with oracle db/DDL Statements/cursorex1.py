#This program create an object of cursor
#cursorex1.py
import cx_Oracle
con=cx_Oracle.connect("scott/tiger@127.0.0.1/orcl")
print("\nPython Program got collection from Oracle DB:")
cur=con.cursor()
print("\nPython creates an object of cursor")
print("Type of cur=",type(cur))  # <class 'cx_Oracle.Cursor'>
