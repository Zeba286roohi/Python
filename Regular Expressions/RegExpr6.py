#RegExpr6.py
#This program searches for  all except either 'a' or 'b' or 'c'
import re
mat=re.finditer("[^abc]" , "cWaBT#6AT&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr6.py
==================================================
start index:1   End Index:2  Value:W
start index:3   End Index:4  Value:B
start index:4   End Index:5  Value:T
start index:5   End Index:6  Value:#
start index:6   End Index:7  Value:6
start index:7   End Index:8  Value:A
start index:8   End Index:9  Value:T
start index:9   End Index:10  Value:&
start index:10   End Index:11  Value:3
start index:11   End Index:12  Value:p
start index:12   End Index:13  Value:k
start index:13   End Index:14  Value:@
start index:14   End Index:15  Value:1
start index:15   End Index:16  Value:L
start index:16   End Index:17  Value:H
start index:17   End Index:18  Value:8
start index:19   End Index:20  Value:J
==================================================

E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>
"""