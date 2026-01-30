import random

tahkot=int(input("Kirjoita tahkojen määrä: "))

def roll_dice(tahkot):
    return random.randint(1,tahkot)

while True:
    result=roll_dice(tahkot)
    print(result)
    if result == tahkot:
        break