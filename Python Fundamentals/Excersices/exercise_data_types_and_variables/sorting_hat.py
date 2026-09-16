command  = input()
sortedRight = True
while command != "Welcome!":
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif command == "Voldemort":
        print("You must not speak of that name!")
        sortedRight = False
        break
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()
if sortedRight:
    print("Welcome to Hogwarts.")