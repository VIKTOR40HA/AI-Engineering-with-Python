strings = int(input())

for _ in range(strings):
    string = input()
    isPure = True
    if "," in string or "." in string or "_" in string:
        isPure = False

    if isPure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
