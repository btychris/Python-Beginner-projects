import random
import string


def password(length):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    password = "".join(random.choice(characters) for i in range(length))
    return password


length = int(input("Enter the length of your password: "))
print(f"Your password is: {password(length)}")