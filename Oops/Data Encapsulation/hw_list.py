#Write a python program which will accept list of names
#and sort them in both ascending and descending order by using classes and objects


class Sort:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return str((self.a, self.b))
  
  
# list of objects
obj = [Sort("Python", 1),
       Sort("Welcome", 3),
       Sort("To", 2),
       Sort("Learn", 4),
       Sort("Coding", 3)]
  
# sorting objects on the basis of value 
# stored at variable a
print(sorted(obj, key=lambda x: x.a))
