
fist_seconds = int(input())
second_seconds = int(input())
third_seconds = int(input())

summarry = fist_seconds + second_seconds + third_seconds

minutes = summarry // 60
seconds = summarry % 60

if seconds <10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")