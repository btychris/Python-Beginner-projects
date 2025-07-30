# Swapping the content of two variables - www.101computing.net/the-box-swap-puzzle/

number1 = int(input("Enter a number between 1 and 10:"))
number2 = int(input("Enter a number between 1 and 10:"))
number3 = int(input("Enter a number between 1 and 10:"))

# complete the code here...

if number1 < number2:
    temp = number1
    number1 = number2
    number2 = temp

if number2 < number3:
    temp = number2
    number2 = number3
    number3 = temp

if number1 < number2:
    temp = number1
    number1 = number2
    number2 = temp

print(f"number1: {number1}")
print(f"number2: {number2}")
print(f"number3: {number3}")


