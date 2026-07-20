day = input()

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")