deposit = float(input())
srok = int(input())
lihven_procent = float(input()) /100

sum = deposit + srok * ((deposit * lihven_procent)/12)
print(sum)