money_as_string = input().split(", ")
beggars = int(input())
money_as_int =[]
start_index = 0
beggar_sum = []
for money in money_as_string:
    money_as_int.append(int(money))
for current_beggar in range(beggars):
    current_beggar_sum =0
    for index in range(start_index, len(money_as_int),beggars):
        current_beggar_sum += money_as_int[index]

    beggar_sum.append(current_beggar_sum)
    start_index +=1
print(beggar_sum)