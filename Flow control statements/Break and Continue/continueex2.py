#continueex1.py
s="PYTHON"      
# want to display    PYTON  
i=0
while(i<len(s)):
	if(s[i]=="H"):
		i=i+1
		continue
	else:
		print(s[i])
		i=i+1
print("-"*60)
# want to display    PYTN  
i=0
while(i<len(s)):
	if(s[i]=="H") or (s[i]=="O"):
		i=i+1
		continue
	else:
		print(s[i])
		i=i+1