text = input()

for index in range(len(text) - 1):
    if text[index] == ":":
        print(text[index:index + 2])