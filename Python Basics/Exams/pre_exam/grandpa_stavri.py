from ast import literal_eval

days = int(input())
degree_avarage = 0.00
total_liters = 0.00
for day in range(days):
    liters = float(input())
    degree = float(input())
    total_liters += liters
    degree_avarage += degree * liters
degree_avarage /= total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {degree_avarage:.2f}")
if degree_avarage <38:
    print(f"Not good, you should baking!")
elif 38<=degree_avarage <= 42:
    print("Super!")
elif degree_avarage >42:
    print("Dilution with distilled water!")