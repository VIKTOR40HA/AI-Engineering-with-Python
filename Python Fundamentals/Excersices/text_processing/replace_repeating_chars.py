text = input()
result = text[0]

for index in range(1, len(text)):
    if text[index] != text[index - 1]:
        result += text[index]

print(result)