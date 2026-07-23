ROSE_PRICE = 5.00
DALIA_PRICE = 3.80
LALE_PRICE = 2.80
NARCISE_PRICE = 3.00
GALIOLA_PRICE = 2.50

type_flower = input()
quantity = int(input())
budget = int(input())

discount = 0.00
extra_cost = 0.00
total = 0.00
if type_flower == "Roses":
    if quantity > 80:
        discount = 0.10
        cost = ROSE_PRICE * quantity
        total = cost - (cost * discount)
    else:
        total = ROSE_PRICE * quantity
elif type_flower == "Dahlias":
    if quantity > 90:
        discount = 0.15
        cost = DALIA_PRICE * quantity
        total = cost - (cost * discount)
    else:
        total = DALIA_PRICE * quantity
elif type_flower == "Tulips":
    if quantity > 80:
        discount = 0.15
        cost = LALE_PRICE * quantity
        total = cost - (cost * discount)
    else:
        total = LALE_PRICE * quantity
elif type_flower == "Narcissus":
    if quantity < 120:
        extra_cost = 0.15
        cost = NARCISE_PRICE * quantity
        total = cost +(cost * extra_cost)
    else:
        total = NARCISE_PRICE * quantity
elif type_flower == "Gladiolus":
    if quantity < 80:
        extra_cost = 0.20
        cost = GALIOLA_PRICE * quantity
        total = cost + (cost * extra_cost)
    else:
        total = GALIOLA_PRICE * quantity

if budget >=total:
    print(f"Hey, you have a great garden with {quantity} {type_flower} and {(budget - total):.2f} leva left.")
else:
    print(f"Not enough money, you need {(total - budget):.2f} leva more.")