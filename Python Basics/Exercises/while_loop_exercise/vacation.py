from operator import truediv
from zoneinfo import available_timezones

vacation_cost = float(input())
avaible_money = float(input())
days = 0

continous_days = 0
while continous_days < 5:
    if vacation_cost <= avaible_money:
        print(f"You saved the money for {days} days.")
        break
    action = input()
    money = float(input())
    if action == "spend":
        continous_days +=1
        avaible_money = avaible_money - money if avaible_money > money else 0
    elif action == "save":
        continous_days = 0
        avaible_money += money

    days += 1
else:
    print("You can't save the money.")
    print(f"{days}")