budget = float(input())
PRICE_FOR_ONE_KILO_FLOUR = float(input())
PRICE_ONE_PACK_EGGS = PRICE_FOR_ONE_KILO_FLOUR *0.75
PRICE_ONE_LITER_MILK = PRICE_FOR_ONE_KILO_FLOUR *1.25
eggs = 0
loafs = 0
while True:
    if budget > PRICE_ONE_LITER_MILK / 4 + PRICE_ONE_PACK_EGGS + PRICE_FOR_ONE_KILO_FLOUR:
        loafs += 1
        eggs += 3

        if loafs % 3 ==0:
            eggs -= loafs -2

        budget -= PRICE_FOR_ONE_KILO_FLOUR
        budget -= PRICE_ONE_PACK_EGGS
        budget -= PRICE_ONE_LITER_MILK / 4
    else:
        break
print(f"You made {loafs} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")