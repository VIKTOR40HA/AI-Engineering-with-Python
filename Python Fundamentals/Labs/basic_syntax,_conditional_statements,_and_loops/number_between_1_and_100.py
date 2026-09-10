is_found = False
while True:
    if is_found:
        break
    number = float(input())
    if 1<=number <=100:
        is_found = True
        print(f"The number {number} is between 1 and 100")
        