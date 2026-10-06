number1 = int(input())
number2 = int(input())
number3 = int(input())

def smallest_of_three_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    minimum = min(numbers)
    return minimum
print(smallest_of_three_numbers(number1, number2, number3))