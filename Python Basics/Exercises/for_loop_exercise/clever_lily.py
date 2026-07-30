age = int(input())
washing_machine_price = float(input())
doll_price = int(input())
dolls = 0
brothers_burlgary = 0
money = 0
for i in range (1,age+1):
    if i % 2 == 0:
        money += 10 * i/2
        brothers_burlgary += 1
    else:
        dolls += 1

money = money - brothers_burlgary + (doll_price* dolls)

if money >= washing_machine_price:
    print(f"Yes! {(money-washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - money):.2f}")