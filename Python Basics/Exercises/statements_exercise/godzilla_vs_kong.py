budget_movie = float(input())
number_statists = int(input())
statists_clothes = float(input())

decor_price = budget_movie * 0.1
clothes_price = statists_clothes * number_statists

if number_statists > 150:
    clothes_price -= (clothes_price * 0.1)

needed_money = clothes_price + decor_price

if needed_money > budget_movie:
    print("Not enough money!")
    print(f"Wingard needs {needed_money-budget_movie:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget_movie-needed_money:.2f} leva left.")

