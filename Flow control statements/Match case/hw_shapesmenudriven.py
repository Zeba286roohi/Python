#program which will implement the following menu driven application.area of different figures.
#1.circle,2.Rectangle,3.Square,4.Triangle,5.Exit
print("1.Circle:")
print("2.Rectangle:")
print("3.Square:")
print("4.Triangle:")
print("5.Exit:")
print("-"*50)
area=int(input("Enter your choice"))
match(area):
    case 1:
                    r=float(input("Enter the value of radius"))
                    print("area of circle  is",3.14*(r**2))
    case 2:
            l=float(input("Enter the value of length"))
            b=float(input("Enter the value of breadth"))
            print("Area of Rectangle is", l*b)
    case 3:
        s=float(input("Enter the value of sides of square:"))
        print("Area of Square",s*s)
    case 4:
        b=float(input("Enter the breadth of Triangle"))
        h=float(input("Enter the height of Triangle"))
        print("Area of Triangle is",0.5*b*h)
    case 5:
        print("Thanks for using python")
        sys.exit()
    case _:
        print("Your choice is invalid")
        
        
        
