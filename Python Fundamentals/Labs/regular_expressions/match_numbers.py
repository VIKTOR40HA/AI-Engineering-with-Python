import re

pattern = r"(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?($|(?=\s))"

text = input()

matches = re.finditer(pattern, text)

numbers = [match.group() for match in matches]

print(" ".join(numbers))