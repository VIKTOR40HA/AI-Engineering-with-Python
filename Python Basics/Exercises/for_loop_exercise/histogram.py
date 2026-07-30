elements = int(input())

below_200 = 0
between_200_and_399 = 0
between_400_and_599 = 0
between_600_and_799 = 0
over_or_800 = 0

for _ in range(elements):
    number = int(input())
    if number < 200:
        below_200 += 1
    elif 200 <= number <=399:
        between_200_and_399 += 1
    elif 400 <= number <= 599:
        between_400_and_599 += 1
    elif 600 <= number <= 799:
        between_600_and_799 += 1
    elif number >= 800:
        over_or_800 += 1

p1 = (below_200/elements) * 100
p2 = (between_200_and_399/elements) * 100
p3 = (between_400_and_599/elements) * 100
p4 = (between_600_and_799/elements) * 100
p5 = (over_or_800/elements) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

