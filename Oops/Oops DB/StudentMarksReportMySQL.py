#Program for studentmarks report generation with Classes and Object along Database.
#StudentMarksReportMySQL.py
import mysql.connector
class StudentMarksReportMySQL:
	def  getstudentdetails(self): #getting stno,name,CM,CPPM,PYTM
		#validation of Student Number
		while(True):
			self.sno=int(input("Enter Student Number:"))
			if(self.sno>0) and (self.sno<=100):
				break
		self.sname=input("Enter Student Name:")
		#validation of marks in C
		while(True):
			self.cm=int(input("Enter Marks in C:"))
			if(self.cm>=0) and (self.cm<=100):
				break
		#validation of marks in CPP
		while(True):
			self.cppm=int(input("Enter Marks in CPP:"))
			if(self.cppm>=0) and (self.cppm<=100):
				break
		#validation of marks in PYTHON
		while(True):
			self.pytm=int(input("Enter Marks in PYTHON:"))
			if(self.pytm>=0) and (self.pytm<=100):
				break
	def  decidegrade(self):  # cal totmarks,percentage and grade
		#calculate total and percantage of marks
		self.totmarks=self.cm+self.cppm+self.pytm
		self.percent=(self.totmarks/300)*100
		#decide the grade
		if(self.cm<40) or  (self.cppm<40) or (self.pytm<40):
			self.grade="FAIL"
		else:
			if(self.totmarks>=250) and (self.totmarks<=300):
				self.grade="DISTINCTION"
			elif(self.totmarks>=200) and (self.totmarks<=249):
				self.grade="FIRST"
			elif(self.totmarks>=150) and (self.totmarks<=199):
				self.grade="SECOND"
			elif(self.totmarks>=120) and (self.totmarks<=149):
				self.grade="THIRD"

	def  storedtsudentdata(self):  # Python Data Base Communication code
		try:
			con=mysql.connector.connect(host="localhost",
																user="root",
																passwd="root",
																database="kvr")
			cur=con.cursor()
			#design the query and execute
			iq="insert into result values(%d,'%s',%d,%d,%d,%d,%f,'%s') "
			cur.execute(iq %(self.sno,self.sname,self.cm,self.cppm,self.pytm,self.totmarks,self.percent,self.grade) )
			con.commit()
			print("\n{} Student Record Inserted in Result Table--verify".format(cur.rowcount))
		except mysql.connector.DatabaseError as db:
			print("Problem in Database:",db)

#main program
s=StudentMarksReportMySQL()
s.getstudentdetails()
s.decidegrade()
s.storedtsudentdata()
