n = int(input())
total = 0

for i in range(n):
    string = input()
    total += ord(string)
print(f"The sum equals: {total}")