def calculate(operation_to_do,first_number,second_number):
    if operation_to_do == 'multiply':
        result = first_number * second_number
        return round(result)
    elif operation_to_do == 'divide':
        if second_number != 0:
            result = first_number / second_number
            return round(result)
    elif operation_to_do == 'add':
        return first_number + second_number
    elif operation_to_do == 'subtract':
        return first_number - second_number
operation = input()
num1 = int(input())
num2 = int(input())
print(calculate(operation,num1,num2))
