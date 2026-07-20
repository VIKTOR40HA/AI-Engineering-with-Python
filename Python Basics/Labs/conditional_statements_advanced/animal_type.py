name_of_the_animal = input()

if name_of_the_animal == "dog":
    print("mammal")
elif name_of_the_animal in ["crocodile","tortoise","snake"]:
    print("reptile")
else:
    print("unknown")