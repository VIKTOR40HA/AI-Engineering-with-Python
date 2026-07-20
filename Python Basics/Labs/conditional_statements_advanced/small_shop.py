product = input()
town = input()
quantity = float(input())
price = 0.00

if town == "Sofia":
    if product == "coffee":
        price = 0.50
        pass
    elif product == "water":
        price = 0.80
        pass
    elif product == "beer":
        price = 1.20
        pass
    elif product == "sweets":
        price = 1.45
        pass
    elif product == "peanuts":
        price = 1.60
        pass
elif town == "Plovdiv":
    if product == "coffee":
        price = 0.40
        pass
    elif product == "water":
        price = 0.70
        pass
    elif product == "beer":
        price = 1.15
        pass
    elif product == "sweets":
        price = 1.30
        pass
    elif product == "peanuts":
        price = 1.50
        pass
elif town == "Varna":
    if product == "coffee":
        price = 0.45
        pass
    elif product == "water":
        price = 0.70
        pass
    elif product == "beer":
        price = 1.10
        pass
    elif product == "sweets":
        price = 1.35
        pass
    elif product == "peanuts":
        price = 1.55
        pass
total = price * quantity
print(total)