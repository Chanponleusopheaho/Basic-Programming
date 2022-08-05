def cylinderVolume(diameter, height):
    from math import pi
    area = pi * diameter**2 / 4
    volume = area * height
    return volume
i = float(input("Enter the can's diameter: "))
j = float(input("Enter the can's height: "))
vol = round(cylinderVolume(i, j), 2)
print("The can’s volume is", vol)
