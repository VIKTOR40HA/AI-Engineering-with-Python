elements = input().split()
bakery_elements = {}

for index in range (0,len(elements),2):
    product = elements[index]
    quantity = int(elements[index+1])
    bakery_elements[product] = quantity

products_to_check = input().split()

for product in products_to_check:
    if product not in bakery_elements:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {bakery_elements[product]} of {product} left")
