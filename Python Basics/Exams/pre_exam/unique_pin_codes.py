border_first_number = int(input())
border_second_number = int(input())
border_third_number = int(input())

for first_number in range(2,border_first_number+1):
    is_first_number_valid =False
    if first_number % 2 == 0:
        is_first_number_valid = True
    for second_number in range(2,border_second_number+1):
        is_second_number_valid = False
        if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
            is_second_number_valid = True
        for third_number in range(2,border_third_number+1):
            is_third_number_valid = False
            if third_number % 2 == 0:
                is_third_number_valid = True
            if is_first_number_valid and is_second_number_valid and is_third_number_valid:
                print(first_number,second_number,third_number)





