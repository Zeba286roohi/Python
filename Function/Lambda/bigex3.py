#Program accepting three integer values and find biggest by using anonymous functions   
#bigex3.py
big=lambda a,b,c: "ALL VALUES EQUAL" if (a==b) and (b==c) else a if(a>b) and (a>c) else  b  if (b>c) and (b>a) else c

#main program
print("Enter Three values:")
bv=big(int(input()), int(input()), int(input()) )
print("Biggest=",bv)