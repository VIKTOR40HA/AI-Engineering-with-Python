STUDIO_MAY_OCTOBER = 50.00
APARTMENT_MAY_OCTOBER = 65.00
STUDIO_JUNE_SEPTEMBER = 75.20
APARTMENT_JUNE_SEPTEMBER = 68.70
STUDIO_MAY_JULY_AUGUST = 76.00
APARTMENT_MAY_JULY_AUGUST = 77.00

month = input()
nights = int(input())

apartment_cost = 0.00
studio_cost = 0.00
if month == "May" or month == "October":
    apartment_cost = APARTMENT_MAY_OCTOBER * nights
    studio_cost = STUDIO_MAY_OCTOBER * nights
    if nights > 14:
        studio_cost = studio_cost * 0.7
    elif nights > 7:
        studio_cost = studio_cost * 0.95
    pass

elif month == "June" or month == "September":
    apartment_cost = APARTMENT_JUNE_SEPTEMBER * nights
    studio_cost = STUDIO_JUNE_SEPTEMBER * nights
    if nights > 14:
        studio_cost = studio_cost * 0.8
    pass

elif month == "July" or month == "August":
    apartment_cost = APARTMENT_MAY_JULY_AUGUST * nights
    studio_cost = STUDIO_MAY_JULY_AUGUST * nights
    pass

if nights > 14:
    apartment_cost = apartment_cost * 0.9
print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")