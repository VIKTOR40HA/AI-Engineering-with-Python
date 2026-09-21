lines = int(input())
tank_current = 0
for i in range(0,lines):
    liter_per_line = int(input())
    if tank_current + liter_per_line > 255:
        print("Insufficient capacity!")
        continue
    tank_current = tank_current + liter_per_line
print(tank_current)