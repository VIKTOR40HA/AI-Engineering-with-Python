word = input()
reversed_word = ""

for character in range(len(word)-1,-1,-1):
    reversed_word += word[character]

print(reversed_word)