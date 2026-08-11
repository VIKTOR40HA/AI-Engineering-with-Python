
    while True:
        destination = input()
        if destination == "End":
            break
        budget = float(input())
        money = 0.00

        while money < budget:
            new_amount = float(input())
            money += new_amount

        print(f"Going to {destination}!")

