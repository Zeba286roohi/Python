#RegExpr14.py
#This program searches for  all except lower and upper case alphabets
import re
mat=re.finditer("[^A-Za-z]" , "cWaBT#6AT&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr14.py
==================================================
start index:5   End Index:6  Value:#
start index:6   End Index:7  Value:6
start index:9   End Index:10  Value:&
start index:10   End Index:11  Value:3
start index:13   End Index:14  Value:@
start index:14   End Index:15  Value:1
start index:17   End Index:18  Value:8
=================================================="""