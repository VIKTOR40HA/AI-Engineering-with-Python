def is_perfect_number(number):
    divisor_sum = 0
    for divisor in range(1,number):
        if number % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == number:
        return True
    return False
number = int(input())
if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")