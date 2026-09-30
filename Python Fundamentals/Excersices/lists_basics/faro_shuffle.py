from operator import index

deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_of_the_deck = len(deck)//2
    leftside = deck[:middle_of_the_deck]
    rightside = deck[middle_of_the_deck:]
    deck_after_shuffle = []
    for index in range(len(leftside)):

        deck_after_shuffle.append(leftside[index])
        deck_after_shuffle.append(rightside[index])
    deck = deck_after_shuffle
print(deck)


