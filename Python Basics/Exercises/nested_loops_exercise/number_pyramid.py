n = int(input())
current = 1
is_bigger_than_n = False
for row in range(1, n +1):
    for col in range(1, row+1):
        if current > n:
            break
        print(current, end=" ")
        current = current + 1
    print()
    if current > n:
        break
