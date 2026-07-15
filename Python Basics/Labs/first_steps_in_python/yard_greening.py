kv_meters = float(input())

total=kv_meters*7.61
discount = total*0.18
total = total-discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")