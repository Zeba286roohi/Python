#RegExpr7.py
#This program searches for  all lower alphabets
import re
mat=re.finditer("[a-z]" , "cWaBT#6AT&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr7.py
==================================================
start index:0   End Index:1  Value:c
start index:2   End Index:3  Value:a
start index:11   End Index:12  Value:p
start index:12   End Index:13  Value:k
start index:18   End Index:19  Value:b
=================================================="""
