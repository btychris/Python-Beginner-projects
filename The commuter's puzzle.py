#The commuter's puzzle - www.101computing.net/to-the-moon-and-back

def puzzle():
    dailyCommute = 60 * 2
    weeklyCommute = 5 * dailyCommute
    yearlyCommute = weeklyCommute * 52
    yearlyDistance = yearlyCommute * 1.609
    moonTrip = 38440 * 2
    years = moonTrip / yearlyDistance
    print(f"Yuri would have travelled the equivalent of going to the Moon and back in {years} years")


if __name__ == "__main__":
    puzzle()