courses = {}
while True:
    command = input()
    if command == "end":
        break
    arguments = command.split(" : ")
    course_name = arguments[0]
    student_name = arguments[1]

    if course_name in courses:
        courses[course_name].append(student_name)
    elif course_name not in courses:
        courses[course_name] = [student_name]


for course,students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")