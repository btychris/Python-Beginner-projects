import random

words = ["Barcelona", "Manchester United", "Bayern Munich", "Juventus", "Paris Saint-Germain", "Real Madrid", "Ajax", "Chelsea", "Liverpool", "AC Milan"]
football_team = random.choice(words)

user_guess = input("Enter a guess: ")
guesses = 0


while guesses > 0:
    for _ in football_team:
        if user_guess not in football_team:
            print(f"{user_guess} not in word")
            guesses += 1
        elif user_guess in football_team:
            print(f"{user_guess} is in the word")
            

