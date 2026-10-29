text = input()
result = ""
strength = 0
index = 0

while index < len(text):
    if text[index] == ">":
        result += ">"
        strength += int(text[index + 1])
        index += 1
    elif strength > 0:
        strength -= 1
        index += 1
    else:
        result += text[index]
        index += 1

print(result)