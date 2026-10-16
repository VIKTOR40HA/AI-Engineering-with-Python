elements = input().split()
bakery_elements = {}

for index in range (0,len(elements),2):
    product = elements[index]
    quantity = int(elements[index+1])
    bakery_elements[product] = quantity

print(bakery_elements)
