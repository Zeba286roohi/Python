#Program accepting two integer values and find biggest by using anonymous functions
#bigex1.py
big=lambda a,b: a if a>b else b # anonymous functions
small=lambda a,b: a if a<b else b   # anonymous functions
#main program
bv=big(float(input("Enter First Value:")),float(input("Enter Second Value:")) )
print("Biggest={}".format(bv))
sv=small(float(input("Enter First Value:")),float(input("Enter Second Value:")) )
print("smallest={}".format(sv))




