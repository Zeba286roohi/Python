#Program accepting three integer values and find biggest by using anonymous functions   
#bigex2.py
big=lambda a,b,c: a if(a>b) and (a>c) else  b  if (b>c) and (b>a) else c

#main program
print("Enter Three values:")
bv=big(int(input()), int(input()), int(input()) )
print("Biggest=",bv)