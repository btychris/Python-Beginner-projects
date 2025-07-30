# Ice Cream Price Calculator - www.101computing.net/ice-cream-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+      The Ice Cream Shop       +")
print("+            Welcome            +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

price = 0
container = input("What type of ice cream container would you like: cup or cone?").lower()
while container != "cup" and container != "cone":
    print("Invalid answer please try again!")
    container = input("What type of ice cream container would you like: cup or cone?").lower()


if container == "cup":
    price += 0.50
elif container == "cone":
    price += 0.80


scoops = int(input("How many scoops do you want? "))
while scoops < 1 or scoops > 4:
    print("Please enter a number of scoops between 1 and 4")
    scoops = int(input("How many scoops do you want? "))

for i in range(scoops):
    price += 1.00

flake = input("Do you want flakes with your ice cream? (yes/no)").lower()

if flake == "yes":
    price += 0.40

chocolate = input("Do you want Chocolate sprinkle with your ice cream? (yes/no)").lower()

if chocolate == "yes":
    price += 0.30

strawberry = input("Do you want Strawberry Coulis with your ice cream? (yes/no)").lower()

if strawberry == "yes":
    price += 0.60

print(f"Your total is £{price:.2f}")