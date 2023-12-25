# This program extracts or retrieve the from given string
#forloopex1.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
	print(s[i])
	i=i+1
print("="*50)
print("By using for loop")
for val in s:
	print(val)
print("="*50)
print("By using while loop")
lst=[10,"Rossum",34.56,"Python"]
i=0
while(i<len(lst)):
	print(lst[i])
	i=i+1
print("="*50)
print("By using for loop")
for val in lst:
	print(val)
print("="*50)
print("By using while loop")
r=range(100,106)
j=0
while(j<len(r)):
	print(r[j])
	j=j+1
print("="*50)
print("By using for loop")
for val in r:
	print(val,end=" ")
