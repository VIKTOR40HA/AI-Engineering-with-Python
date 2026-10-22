users_and_cars = {}
n = int(input())
for i in range(n):
    command = input().split(" ")

    if command[0] == "register":
        username = command[1]
        license_number = command[2]
        if username not in users_and_cars:
            users_and_cars[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif command[0] == "unregister":
        username = command[1]
        if username in users_and_cars:
            del users_and_cars[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_number in users_and_cars.items():
    print(f"{username} => {license_number}")
