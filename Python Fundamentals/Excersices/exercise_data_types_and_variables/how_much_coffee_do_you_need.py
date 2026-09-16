coffecounter = 0
while True:
    text= input()
    if text == "END":
        break
    elif text == "coding":
        coffecounter += 1
    elif text == "CODING":
        coffecounter += 2
    elif text == "dog" or text == "cat":
        coffecounter += 1
    elif text == "DOG" or text == "CAT":
        coffecounter += 2
    elif text == "movie":
        coffecounter += 1
    elif text == "MOVIE":
        coffecounter += 2
    else:
        continue
if coffecounter > 5:
    print("You need extra sleep")
else:
    print(coffecounter)