words = input().split()
dictionary = {}

for word in words:
    word = word.lower()
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

list_answear = []
for word,appearances in dictionary.items():
    if appearances % 2 != 0:
        list_answear.append(word)

print(" ".join(list_answear))