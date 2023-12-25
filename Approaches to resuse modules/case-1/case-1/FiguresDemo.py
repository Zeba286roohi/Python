#main program where we can integrate all areas of different figures
#FiguresDemo.py
import circle,square,rect,sys
from figareamenu import menu
while(True):
	menu()
	ch=int(input("Enter ur Choice:"))
	match(ch):
		case 1:
					circle.area()
		case 2:
					rect.area()
		case 3:
					square.area()
		case 4:
					print("Thanks for using this program")
					sys.exit()
		case _:
			print("Ur Selection of Operation is wrong-try again")
		   