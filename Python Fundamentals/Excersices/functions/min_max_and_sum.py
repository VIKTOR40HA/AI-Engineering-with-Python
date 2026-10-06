def min_max_and_sum(numbers_as_numbers):

    print(f"The minimum number is {min(numbers_as_numbers)}")
    print(f"The maximum number is {max(numbers_as_numbers)}")
    print(f"The sum number is: {sum(numbers_as_numbers)}")
given_numbers = input().split()
numbers = list(map(int, given_numbers))

min_max_and_sum(numbers)