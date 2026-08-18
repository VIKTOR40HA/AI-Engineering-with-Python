costs_for_the_party = float(input())
love_letters_count = int(input())
roses_count = int(input())
key_holders_count = int(input())
photos_count = int(input())
luck_surpise_count = int(input())

income = love_letters_count * 0.60 + roses_count * 7.20 + key_holders_count * 3.60 + photos_count * 18.20 + luck_surpise_count * 22.00
total_items = love_letters_count + roses_count + key_holders_count + photos_count + luck_surpise_count

if total_items >= 25:
    income *=0.65

income *=0.9

if income >= costs_for_the_party:
    left_money = income - costs_for_the_party
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = costs_for_the_party - income
    print(f"Not enough money! {needed_money:.2f} lv needed.")