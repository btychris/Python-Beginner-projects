import math

shape = input("Enter the shape:\n1.Square\n2.Rectangle\n3.Circle\n4.Triangle\n")

if shape == "Square" or shape == "1":
    width = int(input("Enter the width of the square: "))
    print(f"Square: {width**2}")
elif shape == "Rectangle" or shape == "2":
    width = int(input("Enter the width of the rectangle: "))
    length = int(input("Enter the length of the rectangle: "))
    print(f"Rectangle: {width * length}")
elif shape == "Circle" or shape == "3":
    radius = int(input("Enter the width of the rectangle: "))
    print(f"Circle: {math.pi * (radius**2)}")
elif shape == "Triangle" or shape == "4":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    print(f"Triangle: {int((base * height) / 2)}")
else:
    print("Enter a number between 1-4")
