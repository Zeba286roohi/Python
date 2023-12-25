#RegExpr24.py
#This program k+ means searching one k or more k's
import re
mat=re.finditer("k+" , "kvkkvkkkvkv")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr24.py
==================================================
start index:0   End Index:1  Value:k
start index:2   End Index:4  Value:kk
start index:5   End Index:8  Value:kkk
start index:9   End Index:10  Value:k
=================================================="""