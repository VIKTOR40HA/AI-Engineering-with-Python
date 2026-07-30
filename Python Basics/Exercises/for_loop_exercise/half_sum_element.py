import sys
numbers = int(input())

biggest_number = -sys.maxsize
sum = 0
for _ in range(numbers):
    current_number = int(input())
    if biggest_number <= current_number:
        biggest_number = current_number
    sum += current_number

if sum-biggest_number==biggest_number:
    print("Yes")
    print(f"Sum = {biggest_number}")
else:
    print("No")
    print(f"Diff = {abs((sum-biggest_number)-biggest_number)}")
