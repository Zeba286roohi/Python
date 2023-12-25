#posparamex2.py

def    dispstudinfo(stno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(stno,sname,marks,crs))

#main program
print("="*50)
print("\tStno\tName\tMarks\tCourse")
print("="*50)
dispstudinfo(10,"RS",33.33,"PYTHON")
dispstudinfo(20,"DR",33.33,"PYTHON")
dispstudinfo(30,"RR",43.33,"PYTHON")
dispstudinfo(40,"KV",63.33,"PYTHON")
dispstudinfo(50,"WR",93.93,"PYTHON")
dispstudinfo(60,"PR",83.33,"PYTHON")
print("="*50)