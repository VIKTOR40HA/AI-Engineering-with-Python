values = input().split()
inverted_values = []
for num in values:
    inverted_num = - int(num)
    inverted_values.append(inverted_num)
print(inverted_values)