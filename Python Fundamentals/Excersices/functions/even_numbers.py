def is_even(num):
    return num % 2 == 0
given_numbers_as_string = input().split()
given_numbers_as_numbers = list(map(int, given_numbers_as_string))

result = list(filter(is_even,given_numbers_as_numbers))
print(result)