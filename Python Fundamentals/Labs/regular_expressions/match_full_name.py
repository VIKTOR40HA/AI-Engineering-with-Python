import re

pattern = r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b"

text = input()

matches = re.findall(pattern, text)

print(" ".join(matches))