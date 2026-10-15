
sequence = list(map(int, input().split(", ")))
current_group = 10
while len(sequence) > 0:
    current_list = []
    remaining_numbers = []
    for number in sequence:
        if number <= current_group:
            current_list.append(number)
        else:
            remaining_numbers.append(number)

    print(f"Group of {current_group}'s: {current_list}")
    sequence = remaining_numbers
    current_group += 10
