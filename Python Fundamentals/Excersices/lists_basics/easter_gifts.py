gifts_to_buy = input().split()
command = input().split()
while command[0] != "No" and command[1] != "Money":
    command_to_do = command[0]
    gift = command[1]
    if command_to_do == "OutOfStock":
        while gift in gifts_to_buy:
            gift_index = gifts_to_buy.index(gift)
            gifts_to_buy.pop(gift_index)
            gifts_to_buy.insert(gift_index, 'None')
    elif command_to_do == "Required":
        index = int(command[2])
        if 0 <=index < len(gifts_to_buy) - 1:
            gifts_to_buy[index] = gift
    elif command_to_do == "JustInCase":
        gifts_to_buy[len(gifts_to_buy)-1] = gift
    command = input().split()

for gift in gifts_to_buy:
    if gift != "None":
        print(f"{gift}", end=" ")