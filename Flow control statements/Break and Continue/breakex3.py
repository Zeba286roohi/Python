#breakex3.py
d={10:"Python",20:"Data Scienece",30:"Django",40:"Java"}
for k,v in d.items():
	if (k==30):
		break
	else:
		print("\t{}--->{}".format(k,v))

