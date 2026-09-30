energy = 100
coins = 100
events = input().split("|")
closed = False

for event in events:
    parameters = event.split("-")
    event_or_ingredient = parameters[0]
    current_energy = int(parameters[1])

    if event_or_ingredient == "rest":
        initial_energy = energy
        energy += current_energy

        if energy > 100:
            energy = 100

        gained_energy = energy - initial_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_or_ingredient == "order":
        if energy >= 30:
            energy -= 30
            coins += current_energy
            print(f"You earned {current_energy} coins.")
        else:
            print("You had to rest!")
            energy += 50
            closed = True
            break

    else:
        if current_energy <= coins:
            coins -= current_energy
            print(f"You bought {event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            closed = True


if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")