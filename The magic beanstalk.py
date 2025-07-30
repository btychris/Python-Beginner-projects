import sys
import time

print("The magic beanstalk")


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)


height = 100
hours = int(input("Enter the number of hours"))
typingPrint("After one hour, the beanstalk was 100cm tall\n")

for i in range(2, hours):
    height = height * 1.5 + 30
    typingPrint(f"After {i} hours, the beanstalk was {height} cm tall\n")

typingPrint("And its still growing!!!")