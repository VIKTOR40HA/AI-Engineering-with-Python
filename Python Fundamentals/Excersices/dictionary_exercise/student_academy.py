n = int(input())
good_students = {}
for _ in range(n):
    student = input()
    grade = float(input())
    if student not in good_students:
        good_students[student] = [grade]
    elif student  in good_students:
        good_students[student].append(grade)

for student, grades in good_students.items():
    avarage_grade = sum(grades) / len(grades)
    if avarage_grade >= 4.50:
        print(f"{student} -> {avarage_grade:.2f}")
