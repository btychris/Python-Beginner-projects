amountOflight = int(input("Enter the amount of light that the bulb provides: "))
powerConsumption = int(input("Enter the power consumption: "))

efficiencyRatio = amountOflight / powerConsumption

if efficiencyRatio >= 210:
    print("A")
elif efficiencyRatio >= 185:
    print("B")
elif efficiencyRatio >= 160:
    print("C")
elif efficiencyRatio >= 135:
    print("D")
elif efficiencyRatio >= 110:
    print("E")
elif efficiencyRatio >= 85:
    print("F")
else:
    print("G")