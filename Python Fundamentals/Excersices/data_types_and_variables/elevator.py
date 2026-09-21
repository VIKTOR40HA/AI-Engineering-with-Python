persons = int(input())
capacity = int(input())

if capacity >= persons:
    print(1)
elif capacity < persons:
    courses = 0
    while persons > 0:
        courses += 1
        persons -= capacity
    print(courses)