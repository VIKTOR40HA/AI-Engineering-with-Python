SPRING_RENT = 3000.00
SUMMER_AND_AUTUMN_RENT = 4200.00
WINTER_RENT = 2600.00

price_for_rent = 0.00
total = 0.00

budget = int(input())
season = input()
quantity = int(input())

if season == "Spring":
    price_for_rent = SPRING_RENT
    if quantity <=6:
        total = price_for_rent - (price_for_rent * 0.10)
    elif 7<=quantity <=11:
        total = price_for_rent - (price_for_rent * 0.15)
    elif quantity >=12:
        total = price_for_rent - (price_for_rent * 0.25)
elif season == "Summer" or season == "Autumn":
    price_for_rent = SUMMER_AND_AUTUMN_RENT
    if quantity <= 6:
        total = price_for_rent - (price_for_rent * 0.10)
    elif 7 <= quantity <= 11:
        total = price_for_rent - (price_for_rent * 0.15)
    elif quantity >= 12:
        total = price_for_rent - (price_for_rent * 0.25)

elif season == "Winter":
    price_for_rent = WINTER_RENT
    if quantity <= 6:
        total = price_for_rent - (price_for_rent * 0.10)
    elif 7 <= quantity <= 11:
        total = price_for_rent - (price_for_rent * 0.15)
    elif quantity >= 12:
        total = price_for_rent - (price_for_rent * 0.25)

if season != "Autumn":
    if quantity % 2 ==0:
        total = total * 0.95

if total <= budget:
    print(f"Yes! You have {(budget-total):.2f} leva left.")
else:
    print(f"Not enough money! You need {(total - budget):.2f} leva.")