def addition():
    return num1 + num2


def subtraction():
    return num1 - num2


def multiplication():
    return num1 * num2


def division():
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("It cant be divided")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

op = input("Pick an operator \n1.Add\n2.Sub\n3.Multi\n4.Div\n")

if op == "1" or "add":
    print(f"{addition()}")

elif op == "2" or "sub":
    print(f"{subtraction()}")

elif op == "3" or "Multi":
    print(f"{multiplication()}")

elif op == "4" or "division":
    print(f"{division()}")

