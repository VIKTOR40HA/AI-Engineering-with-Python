import math
name = input()
points_from_the_academy = float(input())
jury = int(input())

points = points_from_the_academy
for _ in range(jury):
    name_of_jury = input()
    points_from_jury = float(input())

    points += (len(name_of_jury) * points_from_jury)/ 2
    if points > 1250.5:
       print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
       break
if points < 1250.5:
    print(f"Sorry, {name} you need {(1250.5 - points):.1f} more!")

