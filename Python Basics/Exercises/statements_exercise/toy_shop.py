PUZZLE_PRICE = 2.60
DOLLS_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE =8.20
TRUCK_PRICE = 2

price_for_vacation = float(input())
puzzles = int(input())
dolls = int(input())
teddys = int(input())
minions = int(input())
trucks = int(input())

toys = puzzles + dolls + teddys + minions + trucks
toys_price = (puzzles * PUZZLE_PRICE + dolls *DOLLS_PRICE + teddys * TEDDY_BEAR_PRICE + minions * MINION_PRICE + trucks * TRUCK_PRICE)

if toys >=50:
    toys_price = toys_price * 0.75

toys_price = toys_price * 0.90

if toys_price >= price_for_vacation:
    lasts = toys_price - price_for_vacation
    print(f"Yes! {lasts:.2f} lv left.")
else:
    needed = price_for_vacation - toys_price
    print(f"Not enough money! {needed:.2f} lv needed.")