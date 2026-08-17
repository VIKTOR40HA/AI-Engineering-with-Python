
first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number +1):
    even_sum = 0
    odd_sum = 0

    for index , value in enumerate(str(current_number)):
        if index % 2 == 0:
            even_sum += int(value)
        else:
            odd_sum += int(value)

    if even_sum == odd_sum:
        print(current_number, end=" ")
