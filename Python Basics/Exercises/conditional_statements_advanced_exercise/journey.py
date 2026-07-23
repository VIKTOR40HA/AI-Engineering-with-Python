budget = float(input())
season = input()
types = " "
destination =" "
price = 0.00
if season == "summer":
    if budget <= 100:
        price = budget * 0.3
        types = "Camp"
        destination = "Bulgaria"
        pass
    elif 100 <budget <=1000:
        price = budget * 0.4
        types = "Camp"
        destination = "Balkans"
        pass
    elif budget >=1000:
        price = budget * 0.9
        types = "Hotel"
        destination = "Europe"
        pass

    pass
elif season == "winter":
    if budget <= 100:
        price = budget * 0.7
        types = "Hotel"
        destination = "Bulgaria"
        pass
    elif 100 < budget <= 1000:
        price = budget * 0.8
        types = "Hotel"
        destination = "Balkans"
        pass
    elif budget >= 1000:
        price = budget * 0.9
        types = "Hotel"
        destination = "Europe"
        pass

    pass
print(f"Somewhere in {destination}")
print(f"{types} - {price:.2f}")
