# The Egg Farmer's Puzzle - www.101computing.net/the-egg-farmer-puzzle/

eggs = int(input("How many eggs have you picked up this morning? "))

boxesof12 = eggs // 12
print(f"You will need {boxesof12} cartons of 12 eggs")

if boxesof12 % 12 == 0:
    print(f"You will have {eggs % 12} eggs for breakfast")
else:
    boxesof6 = (eggs % 12) // 6
    print(f"You will need {boxesof6} cartons of 6 eggs")
    print(f"You will have {eggs % 6} eggs for breakfast")