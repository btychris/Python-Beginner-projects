username = input("Enter your username: ")

while len(username) < 6 or "_" not in username:
    username = input("Please enter a valid username: ")

if username[:2] == "00":
    print("You are a staff member.")

year = username[1:2]
print(year)

if username[:2] > "00":
    print("You are a student")
    print(f"You are in Year {year}")

print(f"First name initial: {username[2:3]}")
print(f"Last name: {username[3:-2]}")

if username[-1:] == "S":
    print("Student")
elif username[-1:] == "A":
    print("Admin")
elif username[-1:] == "T":
    print("Teacher")