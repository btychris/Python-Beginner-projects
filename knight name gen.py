# Knight Name Generator - www.101computing.net/name-knight-generator
import random


def knightNameGenerator():
    # Initialise list of possible first names and nicknames
    firstnames = ["Lancelot", "Charles", "Henry", "William", "James", "Richard", "Edward"]
    nicknames = ["Brave", "Horrific", "Courageous", "Terrific", "Fair", "Conqueror", "Victorious", "Glorious",
                 "Invisible"]

    # Randomly pick one first name and one nickname
    firstname = random.choice(firstnames)
    nickname = random.choice(nicknames)

    # Use String concatenation to generate and return the full name
    return firstname + " The " + nickname


def generateCoatOfArms():
    colours = ["Red", "Golden", "Blue", "Purple", "White", "Silver"]
    animals = ["Lion", "Dragon", "Unicorn", "Horse", "Tiger"]

    colour1 = random.choice(colours)
    colour2 = random.choice(colours)
    animal = random.choice(animals)

    if colour1 == colour2:
        return f"{colour1} {animal}"
    else:
        return f"{colour1} and {colour2} {animal}"


def generateFavouriteWeapon():
    weapons = ["Iron Mace", "Golden Flail", "Silver Axe", "Silver Sword", "Wooden Shield"]

    weapon = random.choice(weapons)

    if weapon == "Iron Mace":
        return f"Your favourite weapon is an {weapon}"
    else:
        return f"Your favourite weapon is a {weapon}"


def live():
    places = ["Haunted Castle", "Hidden Mansion", "Fortified tower"]

    place = random.choice(places)
    return f"You live in a {place}"


# Main code to test our function


player1 = knightNameGenerator()
coat1 = generateCoatOfArms()
weapon1 = generateFavouriteWeapon()
place1 = live()
print("Player 1: Your name is: " + player1)
print(f"Your coat of arms is {coat1}")
print(weapon1)
print(place1)
print("\n")

player2 = knightNameGenerator()
coat2 = generateCoatOfArms()
weapon2 = generateFavouriteWeapon()
place2 = live()
print("Player 2: Your name is: " + player2)
print(f"Your coat of arms is {coat2}")
print(weapon2)
print(place2)
