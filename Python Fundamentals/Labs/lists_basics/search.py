n = int(input())
word = input()
lst = []
lst_with_words = []
for i in range(n):
    sentence = input()
    lst.append(sentence)
    if word in sentence:
        lst_with_words.append(sentence)
print(lst)
print(lst_with_words)

