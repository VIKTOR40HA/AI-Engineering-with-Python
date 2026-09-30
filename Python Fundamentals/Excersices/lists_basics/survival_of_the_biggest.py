numbers = input().split()
removes = int(input())
numbers_as_numbers =[]
for number in numbers:
    numbers_as_numbers.append(int(number))
sorted_numbers_as_numbers = sorted(numbers_as_numbers)
numbers_need_to_be_removed = []

for index in range(removes):
    numbers_need_to_be_removed.append(sorted_numbers_as_numbers[index])

for number in numbers_need_to_be_removed:
    numbers_as_numbers.remove(number)

print(", ".join(map(str, numbers_as_numbers)))
