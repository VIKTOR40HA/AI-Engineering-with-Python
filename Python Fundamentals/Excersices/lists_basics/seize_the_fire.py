information = input().split("#")
avaible_water = int(input())
total_effort = 0
fires_put_out = []
total_fire = 0
for index in range(len(information)):
        type_and_value = information[index].split(" = ")
        type_of_fire = type_and_value[0]
        value_of_fire = int(type_and_value[1])
        if type_of_fire == "High":
            if 81<=value_of_fire <=125:
                if avaible_water<value_of_fire:
                    continue
                avaible_water -= value_of_fire
                total_effort += value_of_fire/4
                total_fire += value_of_fire
                fires_put_out.append(value_of_fire)
        elif type_of_fire == "Medium":
            if avaible_water < value_of_fire:
                continue
            if 51 <= value_of_fire <=80:
                avaible_water -= value_of_fire
                total_effort += value_of_fire / 4
                total_fire += value_of_fire
                fires_put_out.append(value_of_fire)
        elif type_of_fire == "Low":
            if avaible_water < value_of_fire:
                continue
            if 1<=value_of_fire <=50:
                avaible_water -= value_of_fire
                total_effort += value_of_fire / 4
                total_fire += value_of_fire
                fires_put_out.append(value_of_fire)
print("Cells:")
for fires in fires_put_out:
    print(f" - {fires}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")