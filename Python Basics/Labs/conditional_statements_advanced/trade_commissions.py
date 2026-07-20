town = input()
sales = float(input())
percentage = 0
if (town =="Sofia") or (town =="Plovdiv") or (town =="Varna"):
    if town == "Sofia":
        if 0<=sales<=500:
            percentage = 0.05
        elif 500<=sales<=1000:
            percentage = 0.07
        elif 1000<=sales<=10000:
            percentage = 0.08
        elif sales > 10000:
            percentage = 0.12
        else:
            print("error")
            pass
    elif town == "Plovdiv":
        if 0<=sales<=500:
            percentage = 0.055
        elif 500<=sales<=1000:
            percentage = 0.08
        elif 1000<=sales<=10000:
            percentage = 0.12
        elif sales > 10000:
            percentage = 0.145
        else:
            print("error")
            pass
    elif town == "Varna":
        if 0<=sales<=500:
            percentage = 0.045
        elif 500<=sales<=1000:
            percentage = 0.075
        elif 1000<=sales<=10000:
            percentage = 0.10
        elif sales > 10000:
            percentage = 0.13
        else:
            print("error")
            pass

    total = sales * percentage
    if percentage!=0:
     print(f"{total:.2f}")
else:
    print("error")