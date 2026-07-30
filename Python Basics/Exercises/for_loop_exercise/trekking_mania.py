groups_count = int(input())

sum_of_people =0
musalla_climbing = 0
monblan_climbing = 0
kalimdjaro_climbing = 0
k2_climbing = 0
everest_climbing = 0

for _ in range(groups_count):
    people_count = int(input())
    sum_of_people += people_count
    if people_count <= 5:
        musalla_climbing += people_count
    elif 6 <= people_count <= 12:
        monblan_climbing += people_count
    elif 13 <= people_count <= 25:
        kalimdjaro_climbing += people_count
    elif 26 <= people_count <= 40:
        k2_climbing += people_count
    elif people_count >= 41:
        everest_climbing += people_count

p_musalla = (musalla_climbing / sum_of_people) * 100
p_monblan = (monblan_climbing / sum_of_people) * 100
p_kalimjaro = (kalimdjaro_climbing / sum_of_people) * 100
p_k2 = (k2_climbing / sum_of_people) * 100
p_everest = (everest_climbing / sum_of_people) * 100

print(f"{p_musalla:.2f}%")
print(f"{p_monblan:.2f}%")
print(f"{p_kalimjaro:.2f}%")
print(f"{p_k2:.2f}%")
print(f"{p_everest:.2f}%")
