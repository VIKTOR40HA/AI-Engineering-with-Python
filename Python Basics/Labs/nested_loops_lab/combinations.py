n = int(input())
validoperations = 0
for first_number in range(n+1):
    for second_number in range(n+1):
        for third_number in range(n+1):
            if first_number + second_number + third_number == n:
                validoperations += 1
                break

print(validoperations)
