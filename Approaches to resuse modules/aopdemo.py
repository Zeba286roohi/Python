#This is a main program, where i am integrating all functions of different modules
from aopmenu import aopmenu
from aopoperations import addop,subop,mulop,divop,expop,modop
import sys
while(True):
    aopmenu()
    ch=int(input("Enter ur Choice:"))
    if(ch==1):
        addop()
    elif(ch==2):
        subop()
    elif(ch==3):
        mulop()
    elif(ch==4):
        divop()
    elif(ch==5):
        modop()
    elif(ch==6):
        expop()
    elif(ch==7):
        print("Thanks for using this program")
        sys.exit()
    else:
        print("Ur selection of operation is wrong--try again")

