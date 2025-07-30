import time

age = int(input("Enter your age: "))
year = 2022
population = 7850000000

while year < 2050:
    time.sleep(1)
    year += 1
    age += 1
    population = population * 1.01
    print(f"In {year}, the world population will be {population:.0f} and you will be {age}")

print(f"In 2050, there will be {population-7850000000:.0f} more inhabitants than 2022.")
