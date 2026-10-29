import re

strings = input().split()
total_sum = 0

for string in strings:
    first_letter = string[0]
    number = int(string[1:-1])
    last_letter = string[-1]

    if first_letter.isupper():
        number /= ord(first_letter) - ord("A") + 1
    else:
        number *= ord(first_letter) - ord("a") + 1

    if last_letter.isupper():
        number -= ord(last_letter) - ord("A") + 1
    else:
        number += ord(last_letter) - ord("a") + 1

    total_sum += number

print(f"{total_sum:.2f}")