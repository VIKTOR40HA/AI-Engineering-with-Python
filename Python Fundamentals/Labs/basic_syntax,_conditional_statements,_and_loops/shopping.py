budget = int(input())
budget_is_fine = True
while True:
    price = (input())
    if price =="End":
        print("You bought everything needed.")
        break
    budget = budget - int(price)
    if budget <0:
        print("You went in overdraft!")
        budget_is_fine = False
        break