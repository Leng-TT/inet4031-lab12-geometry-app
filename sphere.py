# inspiration code for Python Unit Testing Project

import math

def surfaceArea(rad):
    surface_area = 4 * math.pi * (rad * rad)
    return surface_area

def volume(rad):
    volume_sphere = (4/3) * math.pi * (rad * rad * rad)
    return (volume_sphere)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a Cylinder = ", volume(radius))

if __name__ == '__main__':
    prompt()
