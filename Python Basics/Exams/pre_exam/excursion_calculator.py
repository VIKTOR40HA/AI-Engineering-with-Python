people_count = int(input())
season = input()
costs = 0.00

if season =="spring":

    if people_count <=5:
        costs = people_count * 50.00
    else:
        costs = people_count * 48.00
    pass
elif season =="summer":

    if people_count <=5:
        costs = people_count * 48.50
    else:
        costs = people_count * 45.00
    pass
elif season =="autumn":

    if people_count <=5:
        costs = people_count * 60.00
    else:
        costs = people_count * 49.50
    pass
elif season =="winter":

    if people_count <=5:
        costs = people_count * 86.00
    else:
        costs = people_count * 85.00
    pass

if season =="summer":
    costs *=0.85
elif season =="winter":
    costs *=1.08

print(f"{costs:.2f} leva.")