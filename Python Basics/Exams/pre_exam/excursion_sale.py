sea_excurtions = int(input())
mountain_excursions = int(input())
profit = 0
while True:
    command = input()
    if command == "Stop":
        break
    elif command == "sea":
        if sea_excurtions >0:
            profit +=680
            sea_excurtions -=1
        else:
            continue
    elif command == "mountain":
        if mountain_excursions >0:
            profit += 499
            mountain_excursions -=1
        else:
            continue
        pass
    if sea_excurtions == 0 and mountain_excursions == 0:
        print(f"Good job! Everything is sold." )
        break

print(f"Profit: {profit} leva.")