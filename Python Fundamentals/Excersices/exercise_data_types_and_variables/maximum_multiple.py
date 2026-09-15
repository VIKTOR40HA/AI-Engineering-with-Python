divisor = int(input())
boundary = int(input())

largest_dividable = 0
for number in range(1, boundary + 1,1):
    if number % divisor == 0:
        if largest_dividable < number:
            largest_dividable = number
print(largest_dividable)
