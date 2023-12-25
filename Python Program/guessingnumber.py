import random
n=random.randint(1,10)

count=0

while n!="guess":
    if count==3:
        print("you lose game" )
        break
    guess=int(input("Enter an integer from 1 to 10:"))
    if guess<n:
        print("guess is low")
        
    elif guess>n:
        print("guess is high")
        
    else:
        print("You guessed it")
        break
    count+=1
