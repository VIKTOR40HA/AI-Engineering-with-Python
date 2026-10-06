def add_and_subtract(num1:int,num2:int,num3:int ) -> int:
    result = sum_numbers(num1,num2) - num3
    return result

def sum_numbers(num1:int,num2:int)-> int:
    result = num1 + num2
    return result
number1 = int(input())
number2 = int(input())
number3 = int(input())
print(add_and_subtract(number1,number2,number3))
