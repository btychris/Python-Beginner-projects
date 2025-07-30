def lego():
    width = 16
    length = 16
    height = 10
    lego_brick = width * length * height

    radius = 6371
    radius = radius * 1000000
    print(f"Earth Radius = {radius} mm")
    planet_earth = 4 * 3.14 * (radius ** 3) / 3

    print(f"Volume of Planet Earth: {planet_earth} mm^3")
    print(f"Volume of a Lego brick {lego_brick} + mm^3")
    numberOfBricks = planet_earth / lego_brick
    print(f"To build planet Earth out of Lego, you will need {numberOfBricks} bricks")


if __name__ == "__main__":
    lego()
