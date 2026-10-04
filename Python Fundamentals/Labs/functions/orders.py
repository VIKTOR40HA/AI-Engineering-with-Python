def total_price_calculator(quantity_,price_):
    total_price = quantity_ * price_

    return f"{total_price:.2f}"
COFFEE_PRICE =1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00

product = input()
quantity = int(input())

if product == "coffee":
    print(total_price_calculator(quantity,COFFEE_PRICE))
elif product == "water":
    print(total_price_calculator(quantity,WATER_PRICE))
elif product == "coke":
    print(total_price_calculator(quantity,COKE_PRICE))
elif product == "snacks":
    print((total_price_calculator(quantity,SNACKS_PRICE)))