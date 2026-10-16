
students = []
while True:
    command = input()

    if ":" not in command:
        course = command.replace("_", " ")
        break

    name, student_id, student_course = command.split(":")
    students.append((name, student_id, student_course))

for student in students:
    name, student_id, student_course = student

    if student_course == course:
        print(f"{name} - {student_id}")
