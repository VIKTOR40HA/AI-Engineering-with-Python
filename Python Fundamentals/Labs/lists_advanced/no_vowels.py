text = input()

text_without_vowels = [ch for ch in text if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(text_without_vowels))
