#zero matric demonstration
#zm.py
import numpy as np
m,n=int(input("Enter Number of Rows:")), int(input("Enter Number of Columns:"))
if(m<=0) or (n<=0):
	print("Invalid Dimensions:")
else:
	zm=np.zeros( (m,n),dtype=int) 
	print(zm)
