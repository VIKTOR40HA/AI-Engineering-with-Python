n = int(input())
left_sum = 0
right_sum = 0
for i in range(n * 2):
    number = int(input())
    if i >= n:
        left_sum += number
    if i < n:
        right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")