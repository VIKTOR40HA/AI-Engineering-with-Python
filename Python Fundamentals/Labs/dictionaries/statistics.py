bakery = {}
while True:

    current_input = input()
    if current_input == "statistics":
        break
    current_input = current_input.split(": ")
    key = current_input[0]
    value = int(current_input[1])

    if key not in bakery:
        bakery[key] = value
    else:
        bakery[key] += (value)


sum_of_quantity = sum(bakery.values())
count_all_products = len(bakery.keys())
print("Products in stock:")
for product, value in bakery.items():
    print(f"- {product}: {value}")
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_of_quantity}")