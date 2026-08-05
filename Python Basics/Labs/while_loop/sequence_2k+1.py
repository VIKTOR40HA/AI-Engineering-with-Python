n = int(input())

iterator = 1

print(iterator)
while iterator < n:
    iterator =iterator*2 +1
    if (iterator>n):
        break
    print(iterator)
