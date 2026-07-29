import sys
n = int(input())
smallest = sys.maxsize
biggest = -sys.maxsize
for i in range(1, n+1):
    number = int(input())
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")