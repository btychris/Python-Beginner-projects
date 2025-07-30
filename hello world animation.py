# Hello World Animation -  www.101computing.net/text-based-animations/
import os
import time


def animate_text(text):
    numberOfCharacters = 1
    while True:
        print("\n")
        print(text[0:numberOfCharacters])
        numberOfCharacters += 1
        if numberOfCharacters > len(text):
            numberOfCharacters = 0
        time.sleep(0.2)
        os.system('clear')

    # Main Program Starts Here....


animate_text("Hello World!")
