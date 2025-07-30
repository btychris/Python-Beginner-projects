# Iterative Sum for number 5


choice = int(input("Enter a number: "))
factorial = 1

for i in range(1, choice + 1):
    factorial = factorial * i

print(f"The factorial for {choice} = {factorial}")
