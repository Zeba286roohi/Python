#RegExpr22.py
#This program searching for all  except  digits
import re
mat=re.finditer("\D" , "$cWa BT#6AT-&3pk @1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)


"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr22.py
==================================================
start index:0   End Index:1  Value:$
start index:1   End Index:2  Value:c
start index:2   End Index:3  Value:W
start index:3   End Index:4  Value:a
start index:4   End Index:5  Value:
start index:5   End Index:6  Value:B
start index:6   End Index:7  Value:T
start index:7   End Index:8  Value:#
start index:9   End Index:10  Value:A
start index:10   End Index:11  Value:T
start index:11   End Index:12  Value:-
start index:12   End Index:13  Value:&
start index:14   End Index:15  Value:p
start index:15   End Index:16  Value:k
start index:16   End Index:17  Value:
start index:17   End Index:18  Value:@
start index:19   End Index:20  Value:L
start index:20   End Index:21  Value:H
start index:22   End Index:23  Value:b
start index:23   End Index:24  Value:J
==================================================

"""



















