def factorial(n):
    result_factorial = 1
    for i in range(1, n+1):
        result_factorial*=i

    return result_factorial
number1 = int(input())
number2 = int(input())

result = factorial(number1) / factorial(number2)
print(f"{result:.2f}")