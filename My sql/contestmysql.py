#This program obtains connection MySQL DB
#contestmysql.py
import mysql.connector
conobj=mysql.connector.connect(host="localhost",
                               user="root",
                               password="Zeba@123")
																												
print("type of conobj=",type(conobj))#<class 'mysql.connector.connection.MySQLConnection'>
print("python program got connection from MYSQL")
