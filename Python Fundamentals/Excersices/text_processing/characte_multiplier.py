strings = input().split()
first_string = strings[0]
second_string = strings[1]
total_sum = 0

if len(first_string) == len(second_string):
    for index in range(len(first_string)):
        multiply = ord(first_string[index]) * ord(second_string[index])
        total_sum += multiply

elif len(first_string) > len(second_string):
    for index in range(len(second_string)):
        multiply = ord(first_string[index]) * ord(second_string[index])
        total_sum += multiply

    for i in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[i])

else:
    for index in range(len(first_string)):
        multiply = ord(first_string[index]) * ord(second_string[index])
        total_sum += multiply

    for i in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[i])

print(total_sum)