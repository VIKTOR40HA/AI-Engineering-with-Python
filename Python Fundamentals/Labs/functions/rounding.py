numbers = input().split()
rounded_numbers = lambda x: round(float(x))
result = [rounded_numbers(number) for number in numbers]
print(result)