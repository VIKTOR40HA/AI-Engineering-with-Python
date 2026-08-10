change = int(float(input()) * 100)

coin_count = 0

while change > 0:
    if change >=200:
        change = change - 200
        coin_count += 1
    elif change >= 100:
        change = change - 100
        coin_count += 1
    elif change >= 50:
        change = change - 50
        coin_count += 1
    elif change >= 20:
        change = change - 20
        coin_count += 1
    elif change >= 10:
        change = change - 10
        coin_count += 1
    elif change >= 5:
        change = change - 5
        coin_count += 1
    elif change >= 2:
        change = change - 2
        coin_count += 1
    elif change >= 1:
        change = change - 1
        coin_count += 1
print(coin_count)