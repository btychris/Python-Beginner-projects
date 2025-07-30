import random


computer = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess (1 to 10): "))

    if guess > 10 or guess < 1:
        print("You are out of range, Try again")
    elif guess < computer:
        print("Low")
        continue
    elif guess > computer:
        print("High")
        continue
    else:
        print(f"You win the guess was {computer}")
        break