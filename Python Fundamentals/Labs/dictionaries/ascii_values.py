characters = input().split(", ")

characters_with_their_code = {character:ord(character) for character in characters }
print(characters_with_their_code)