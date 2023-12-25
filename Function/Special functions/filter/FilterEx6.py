#write a python program which will accept a line of text and filter vowels and print their count
#FilterEx6.py
s=input("Enter line of text:")
vowels=list(filter(lambda ch: ch in ['a','e','o','i','u','A','E','I','O','U'],  s))
print("-------------------------------------------------")
print("Given Line of Text={}".format(s))
print("Vowels={}".format(vowels))
print("Number of vowels={}".format(len(vowels)))
print("-------------------------------------------------")
cons=list(filter(lambda ch: ch not in ['a','e','o','i','u','A','E','I','O','U'] and not ch.isspace() and not ch.isdigit(),  s))
print("consonants={}".format(cons))
print("Number of consonants={}".format(len(cons)))
print("-------------------------------------------------")
