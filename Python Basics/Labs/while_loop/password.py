username = input()
password = input()
current_password = ""
while current_password != password:
    current_password = input()
    if current_password == password:
        print(f"Welcome {username}!")
        break
