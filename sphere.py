# sphere.py
# This program calculates the volume and surface area of a sphere from its radius.
# By: Tristen Sima

def main():
    print("This program calculates the volume and surface area")
    print("of a sphere from its radius.")
    r = eval(input("Enter the sphere's radius: "))
    import math
    V = (4/3) * math.pi * (r ** 3)
    A = 4 * math.pi * (r ** 2)
    print("Volume:", V)
    print("Surface area:", A)

main()
