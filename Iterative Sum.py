# Iterative Sum for number 5


choice = int(input("Enter a number"))
sum = 0

for i in range(1, choice):
    sum = sum + i

print(f"Iterative Sum for {choice} = " + str(sum))
