text = input().split("|")
budget = int(input())
bought_items = 0
new_prices = []
profit = 0
for item in text:
    type_and_cost = item.split("->")
    type = type_and_cost[0]
    cost = float(type_and_cost[1])
    if type == "Clothes":
        if cost <= 50.00:
            if budget >= cost:
                budget -= cost
                bought_items += cost
                new_price = cost * 1.4
                new_prices.append(new_price)
    if type == "Shoes":

        if cost <=35.00:
            if budget >= cost:
                budget -= cost
                bought_items += cost
                new_price = cost * 1.4
                new_prices.append(new_price)

    if type == "Accessories":
        if cost <=20.50:
            if budget >= cost:
                budget -= cost
                bought_items += cost
                new_price = cost * 1.4
                new_prices.append(new_price)
sold_items = bought_items*1.4
profit = (sold_items-bought_items)


print(" ".join(f"{price:.2f}" for price in new_prices))
print(f"Profit: {profit:.2f}")
if budget + sum(new_prices) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")