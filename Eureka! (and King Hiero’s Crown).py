mass = float(input("Enter the mass of an object in Kg: "))
volume = float(input("Enter the volume of an object in m^3: "))
density = mass / volume

if 2400 <= density <= 2700:
    print("Aluminium")
elif 8100 <= density <= 8300:
    print("Bronze")
elif 10400 <= density <= 10600:
    print("Silver")
elif 11200 <= density <= 11400:
    print("Lead")
elif 17100 <= density <= 17500:
    print("Gold")
elif 21000 <= density <= 21500:
    print("Platinum")

print(density)