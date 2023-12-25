#matchcaseex.py
wkn=input("Enter the week name:")
match(wkn.lower()):
	case "monday":
		print("{} is working day:".format(wkn))
	case "tuesday":
		print("{} is working day:".format(wkn))
	case "wednessday":
		print("{} is working day:".format(wkn))
	case "thursday":
		print("{} is working day:".format(wkn))
	case "friday":
		print("{} is working day:".format(wkn))
	case "saturday":
		print("{} is Week End:".format(wkn))
	case "sunday":
		print("{} is Holiday day:".format(wkn))
	case _:
		print("{} is not week day:".format(wkn))
