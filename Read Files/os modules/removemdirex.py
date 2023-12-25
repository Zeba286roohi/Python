#Program for  removing a folders Hierarchy	
#removemdirex.py
import os
try:
	os.removedirs("D:\\India/Hyd\Ameerpet/Python/django")
	print("Folders Hierarhcy removed successfully--verify")
except FileNotFoundError:
	print("Specified Folders does not exists")
except OSError:
	print("Specified Folders is not empty--not possible to remove")