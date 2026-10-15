message = input().split()

result = []

for word in message:
    first_digit_index = 0

    while word[first_digit_index].isdigit():
        first_digit_index += 1

    character_code = int(word[:first_digit_index])
    word = chr(character_code) + word[first_digit_index:]

    if len(word) > 2:
        word = word[0] + word[-1] + word[2:-1] + word[1]

    result.append(word)

print(" ".join(result))