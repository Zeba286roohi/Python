#RegExpr5.py
#This program searches for either 'a' or 'b' or 'c' only
import re
mat=re.finditer("[abc]" , "cWaBT#6AT&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr5.py
==================================================
start index:0   End Index:1  Value:c
start index:2   End Index:3  Value:a
start index:18   End Index:19  Value:b
==================================================
"""