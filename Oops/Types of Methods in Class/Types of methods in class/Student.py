#write a python program which will implement pickling and unpickling concept by using classes and object
#Student.py-----file name and acts as module name
class Student:
	def  setstudvalues(self,sno,sname,marks):
		self.sno=sno
		self.sname=sname
		self.marks=marks

	def   dispstuddata(self):
		print("\t{}\t{}\t{}".format(self.sno,self.sname,self.marks))

