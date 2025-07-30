print("Adult tickets: £15\nChild tickets: £11")
adult = int(input("How many adult tickets do you need? "))
child = int(input("How many children tickets do you need? "))

adult_ticket = adult * 15  # Also here
children_ticket = child * 11  # Check here too

total_cost = adult_ticket + children_ticket

if total_cost > 50:
    total_cost = total_cost * (1-0.05)

print(f"Child tickets: {child}")
print(f"Adult tickets: {adult}")
print(f"Your total cost is £{total_cost:.2f}")