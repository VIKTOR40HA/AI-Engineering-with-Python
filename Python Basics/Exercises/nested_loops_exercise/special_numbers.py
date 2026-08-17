from tokenize import endpats

n = int(input())

for number in range(1111, 9999 +1):
    isSpecial = True

    number = str(number)
    for cifra in number:

        if cifra == '0':
            isSpecial = False
            continue
        elif n % int(cifra) == 0:
            continue
        else:
            isSpecial = False
            continue
    if isSpecial:
        print(number,end =" ")


