#RegExpr10.py
#This program searches for  all except  Upper case alphabets
import re
mat=re.finditer("[^A-Z]" , "cWaBT#6AT&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr10.py
==================================================
start index:0   End Index:1  Value:c
start index:2   End Index:3  Value:a
start index:5   End Index:6  Value:#
start index:6   End Index:7  Value:6
start index:9   End Index:10  Value:&
start index:10   End Index:11  Value:3
start index:11   End Index:12  Value:p
start index:12   End Index:13  Value:k
start index:13   End Index:14  Value:@
start index:14   End Index:15  Value:1
start index:17   End Index:18  Value:8
start index:18   End Index:19  Value:b
=================================================="""