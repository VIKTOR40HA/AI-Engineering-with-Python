PEN_PACKET_PRICE = 5.80
MARKERS_PACK_PRICE = 7.20
MEDIX_PRICE_PER_LITER = 1.20

pens_count = int(input())
makers_count = int(input())
liters_medix_count = int(input())
discount_percentage = float(input()) / 100

total_without_discount = pens_count *PEN_PACKET_PRICE+ makers_count *MARKERS_PACK_PRICE + liters_medix_count * MEDIX_PRICE_PER_LITER
total = total_without_discount -(total_without_discount * discount_percentage)
print(total)