import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
die3 = random.randint(1, 6)

print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Die 3: {die3}")

if die1 == die2 and die2 == die3:
    print("Three of a kind!!!")
elif die1 == die2 or die2 == die3 or die2 == die3:
    print("1 Pair!!!")
else:
    print("Better luck next time!")

if die1 % 2 == 0 and die2 % 2 == 0 and die3 % 2 == 0:
    print("You have three even numbers.")
elif die1 % 2 == 1 and die2 % 2 == 1 and die3 % 2 == 1:
    print("You have three odd numbers.")
