import re

text = input()
matches = re.findall(r"(\D+)(\d+)", text)

rage_message = ""

for string, count in matches:
    rage_message += string.upper() * int(count)

unique_symbols = len(set(rage_message))

print(f"Unique symbols used: {unique_symbols}")
print(rage_message)