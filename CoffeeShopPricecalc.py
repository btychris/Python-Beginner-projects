#The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0
order = int(input("How many coffees are being ordered?: "))

for i in range(order):
    while True:
        coffee = input("What type of coffee would you like?: ").title()
        if coffee == "Espresso":
            price = price + 2.50
            break
        elif coffee == "Americano":
            price = price + 3.00
            break
        elif coffee == "Latte":
            price = price + 2.50
            break
        elif coffee == "Cappuccino":
            price = price + 3.00
            break
        elif coffee == "Macchiato":
            price = price + 2.50
            break
        elif coffee == "Mocha":
            price = price + 3.50
            break
        elif coffee == "Flat White":
            price = price + 2.50
            break
        else:
            print("Invalid option. Please select a type of coffee from the menu.")
            continue

    size = input("What size of coffee would you like (M/L/XL)?")
    if size in ["Medium", "M"]:
        price += 0
    elif size in ["Large", "L"]:
        price = price + 1.00
    elif size == "XL":
        price = price + 1.50

    choice = input("Do you want to Takeaway (yes/no)?: ").lower()
    if choice == "yes":
        price = price + 1.00


print("----------------------------")
print(f"Total Cost: £ {price:.2f}")
