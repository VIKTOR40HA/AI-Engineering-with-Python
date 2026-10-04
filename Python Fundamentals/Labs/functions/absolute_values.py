numbers = input().split()
numbers_as_numbers = []
for number in numbers:
    numbers_as_numbers.append(abs(float((number))))
print(numbers_as_numbers)
