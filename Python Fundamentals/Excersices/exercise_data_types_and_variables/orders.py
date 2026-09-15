orders = int(input())
totaly_total = 0
for i in range(orders):
    total = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if (days >31 or days <=0 or capsules_needed_per_day <= 0 or capsules_needed_per_day > 2000
            or price_per_capsule < 0.01 or price_per_capsule > 100.00):
        continue
    total = price_per_capsule * days * capsules_needed_per_day
    totaly_total += total
    print(f"The price for the coffee is: ${total:.2f}")
print(f"Total: ${totaly_total:.2f}")