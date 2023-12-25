#RegExpr19.py
#This program searches for all word character
import re
mat=re.finditer("\w" , "$cWa BT#6AT-&3pk @1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr19.py
==================================================
start index:1   End Index:2  Value:c
start index:2   End Index:3  Value:W
start index:3   End Index:4  Value:a
start index:5   End Index:6  Value:B
start index:6   End Index:7  Value:T
start index:8   End Index:9  Value:6
start index:9   End Index:10  Value:A
start index:10   End Index:11  Value:T
start index:12   End Index:13  Value:3
start index:13   End Index:14  Value:p
start index:14   End Index:15  Value:k
start index:17   End Index:18  Value:1
start index:18   End Index:19  Value:L
start index:19   End Index:20  Value:H
start index:20   End Index:21  Value:8
start index:21   End Index:22  Value:b
start index:22   End Index:23  Value:J
=================================================="""