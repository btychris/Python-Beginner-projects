money = float(input("Enter the amount you want to convert: "))
choice = input("Type\n1.Pounds to dollars\n2.Dollars to pounds")

if choice == "1":
    print(f"Your currency in dollars is: {money*1.25}")
elif choice == "2":
    print(f"Your currency in pounds is: {money / 1.25 }")