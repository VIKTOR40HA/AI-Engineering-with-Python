def ascii_symbols(character1,character2)->list:
    ascii_symbols = []
    for char in range(ord(character1 ) +1,ord(character2)):
        ascii_symbols.append(chr(char))
    return ascii_symbols
char1 = input()
char2 = input()

result = ascii_symbols(char1,char2)

print(" ".join(result))