wagons = int(input())
train = [0] *wagons

while True:
    line = input().split()
    command = line[0]
    if command == 'End':
        break
    elif command == 'add':
        people = int(line[1])
        train[-1]+=people
        continue
    elif command == 'insert':
        index = int(line[1])
        people = int(line[2])
        train[index]+=people
        continue
    elif command == 'leave':
        index = int(line[1])
        people = int(line[2])
        train[index] -= people
        continue
print(train)