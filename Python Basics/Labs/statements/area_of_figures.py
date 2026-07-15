from math import pi
type = input()

if type== "square":
    lenght = float(input())
    s = lenght*lenght
    print(s)
elif type== "rectangle":
    lenght1 = float(input())
    lenght2 = float(input())
    s = lenght1*lenght2
    print(s)
elif type== "triangle":
    side = float(input())
    height = float(input())
    s = (side * height) / 2
    print(s)
else:
    radius = float(input())
    s= pi*radius*radius
    print(s)