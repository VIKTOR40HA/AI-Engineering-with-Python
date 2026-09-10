numbers = int(input())
are_even = True
for _ in range(numbers):
    number = int(input())
    if number % 2 == 0:
        continue
    elif number % 2 !=0:
        are_even = False
        print(f"{number} is odd!")
        break
if are_even:
    print("All numbers are even.")