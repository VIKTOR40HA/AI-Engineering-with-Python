while(True):
    text = input()
    if text == "SoftUni":
        continue
    elif text == "End":
        break
    else:
        for char in text:
            print(char, end="")
            print(char, end="")
    print()

