#defaultparamex1.py

def    dispstudinfo(stno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(stno,sname,marks,crs))

#main program
print("="*50)
print("\tStno\tName\tMarks\tCourse")
print("="*50)
dispstudinfo(10,"RS",33.33)
dispstudinfo(20,"DR",33.33)
dispstudinfo(30,"RR",43.33)
dispstudinfo(40,"KV",63.33)
dispstudinfo(50,"WR",93.93)
dispstudinfo(60,"PR",83.33)
dispstudinfo(70,"SN",93.33,"JAVA")
dispstudinfo(60,"AJ",73.33)
print("="*50)