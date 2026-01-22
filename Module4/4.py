import random

secret=random.randint(1,10)

while True:
    guess=int(input("Guess a number:"))
    if guess<secret:
        print("Too low")
    elif guess>secret:
        print ("Too hight")
    else:
        print ("Correct")
        break