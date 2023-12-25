x=float(input("Enter your maths marks:"))
y=float(input("Enter your physics marks:"))
z=float(input("Enter your Chemistry marks:"))
if x<35 or y<35 or z<35:
    print("you are failed:")
    exit()
averagemarks=float(x+y+z)/3
if averagemarks>=79:
    print("you have passed with grade A")
elif averagemarks>=69:
    print("You have passed with grade B")
elif averagemarks>=35 and averagemarks>=59:
    print("you have passed with grade C")
