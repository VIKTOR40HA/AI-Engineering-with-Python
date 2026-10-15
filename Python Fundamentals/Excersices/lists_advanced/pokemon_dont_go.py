numbers = list(map(int, input().split()))
sum_removed = 0

while numbers:
    index = int(input())

    if index < 0:
        removed_number = numbers[0]
        numbers[0] = numbers[-1]

    elif index >= len(numbers):
        removed_number = numbers[-1]
        numbers[-1] = numbers[0]

    else:
        removed_number = numbers[index]
        numbers.pop(index)

    sum_removed += removed_number

    for i in range(len(numbers)):
        if numbers[i] <= removed_number:
            numbers[i] += removed_number
        else:
            numbers[i] -= removed_number

print(sum_removed)