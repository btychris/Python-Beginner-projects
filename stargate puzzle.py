# Stargate Access Code - Python Challenge - www.101computing.net/stargate-access-code-python-challenge
import time, os, sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")


print("    ___________________________________")
print("   /                                   \\")
print("   |    Stargate Door Access Panel     |")
print("   \\___________________________________/")
print("")

accessCode = 549024  # Replace this code with the code that appears on your access door panel!

time.sleep(1)
typingPrint(" >> 6-digit Access Code: " + str(accessCode))
time.sleep(1)
typingPrint(" >>")
time.sleep(1)
typingPrint(" >> Starting Brute Force Code Breaking Algorithm to retrieve 3-Letter combination...")
time.sleep(1)

# Complete the code here to test all 3-letter combinations from AAA to ZZZ and check if their "ASCII product" matches the given accessCode.

