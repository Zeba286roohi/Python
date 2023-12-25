#Program accepting list of integer values and find biggest and sammlest by using anonymous functions  
#bigsmall.py

big= lambda lst:max(lst) # anonymous functions  
small=lambda hyd: min(hyd) # anonymous functions  

#main program
print("Enter List of Values separated by space:")
lst=[int(val)  for val in input().split()]
bv=big(lst)
sv=small(lst)
print("biggest({})={}".format(lst,bv))
print("smallest({})={}".format(lst,sv))

