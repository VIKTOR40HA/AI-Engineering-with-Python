summ = 0.00
increase = input()
while increase != 'NoMoreMoney':

    if  float(increase) < 0:
        print("Invalid operation!")
        break
    summ += float(increase)
    print(f"Increase: {float(increase):.2f}")
    increase = input()
print(f"Total: {summ:.2f}")