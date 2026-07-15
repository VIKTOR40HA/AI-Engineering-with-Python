DEFENCE_NAILON_PRICE_BY_KV_METER = 1.50
PAINT_PER_LITER = 14.50
RAZREDITEL=5.00

nailon_needed = int(input())
paint_needed = int(input())
razreditel_needed = int(input())
hours = int(input())



total = (nailon_needed+2)*DEFENCE_NAILON_PRICE_BY_KV_METER + PAINT_PER_LITER*(paint_needed*1.10) + RAZREDITEL*razreditel_needed +0.4
price_paid_by_the_hour = total*0.3
totaly_total = price_paid_by_the_hour *hours + total
print(totaly_total)