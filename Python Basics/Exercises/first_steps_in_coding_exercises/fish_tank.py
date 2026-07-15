dyljina= int(input())
width = int(input())
height = int(input())
percentage = float(input())/100

s = dyljina*width * height /1000
kept = s*percentage

water =s-kept

print(water)