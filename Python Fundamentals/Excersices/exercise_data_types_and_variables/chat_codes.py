massages = int(input())

for _ in range(massages):
    number = int(input())
    if number == 88:
        print("Hello")
        continue
    elif number == 86:
        print("How are you?")
        continue
    elif number <88:
        print("GREAT!")
        continue
    elif number > 88:
        print("Bye.")
        continue
