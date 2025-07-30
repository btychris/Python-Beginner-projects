pupils = ["Joe", "Sonny", "Yassine", "Emma", "Ines", "Satveer", "Lily", "Reuben", "Lucy", "Tom"]

counter = 0
presentCounter = 0

for name in pupils:
    counter += 1

    present = input(f"Is this {name} present (y/n)? ")
    if present == "y":
        presentCounter += 1

    print(f"Total number of students: {counter}")
    print(f"Present: {presentCounter}")
    print(f"Absent: {counter - presentCounter}")