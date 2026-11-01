import re

pattern = r"\b(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"

text = input()

matches = re.findall(pattern, text)

for day, separator, month, year in matches:
    print(f"Day: {day}, Month: {month}, Year: {year}")