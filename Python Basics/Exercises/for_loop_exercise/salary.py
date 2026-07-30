number_of_open_tabs = int(input())
salary = int(input())

for _ in range(number_of_open_tabs):
    open_tab = input()
    if open_tab == "Facebook":
        salary -= 150
    elif open_tab == "Instagram":
        salary -= 100
    elif open_tab == "Reddit":
        salary -= 50

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")