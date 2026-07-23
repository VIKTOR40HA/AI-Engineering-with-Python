PREMIERE_PRICE = 12.00
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

projection = input()
rows = int(input())
cols = int(input())

capacity = rows * cols

total = 0.00
if projection =="Premiere":
    total = PREMIERE_PRICE * capacity
elif projection == "Normal":
    total = NORMAL_PRICE * capacity
else:
    total = DISCOUNT_PRICE * capacity

print(f"{total:.2f} leva")