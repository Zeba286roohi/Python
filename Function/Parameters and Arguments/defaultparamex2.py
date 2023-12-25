#defaultparamex2.py

def    dispstudinfo(stno,sname,marks,crs="PYTHON",city="HYD"):
	print("\t{}\t{}\t{}\t{}\t{}".format(stno,sname,marks,crs,city))

#main program
print("="*50)
print("\tStno\tName\tMarks\tCourse\City")
print("="*50)
dispstudinfo(10,"RS",33.33)
dispstudinfo(20,"DR",33.33)
dispstudinfo(30,"RR",43.33)
dispstudinfo(40,"KV",63.33)
dispstudinfo(50,"WR",93.93)
dispstudinfo(60,"PR",83.33)
dispstudinfo(70,"SN",93.33,"JAVA")
dispstudinfo(80,"AJ",73.33)
dispstudinfo(90,"RR",33.33,"JAVA")
dispstudinfo(35,"KB",33.33,"DJ","Bang")
print("="*50)