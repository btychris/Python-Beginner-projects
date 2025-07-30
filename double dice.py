#Double Six Dice Game - www.101computing.net/double-six-dice-game/
import random

#Complete the code here...

print("""
  __________________________
 |                          |
 |   Double Six Dice Game   |
 |__________________________|

""")

player1 = input("Enter your name Player 1: ")
counter1 = 0

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 == 6 and dice2 == 6:
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print("DOUBLE SIX!")
        break
    else:
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print("Try again!")
        input("Press 'Enter' to continue")
        counter1 += 1
        continue

player2 = input("Enter your name Player 2: ")
counter2 = 0

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 == 6 and dice2 == 6:
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print("DOUBLE SIX!")
        break
    else:
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print("Try again!")
        input("Press 'Enter' to continue")
        counter2 += 1
        continue

if counter1 == counter2:
    print(f"{player1}: {counter1} attempts")
    print(f"{player2}: {counter2} attempts")
    print("The game ends on a draw since you both had the same attempts")
elif counter1 < counter2:
    print(f"{player1}: {counter1} attempts")
    print(f"{player2}: {counter2} attempts")
    print(f"{player1} wins with {counter1} attempts")
elif counter1 > counter2:
    print(f"{player1}: {counter1} attempts")
    print(f"{player2}: {counter2} attempts")
    print(f"{player2} wins with {counter2} attempts")

