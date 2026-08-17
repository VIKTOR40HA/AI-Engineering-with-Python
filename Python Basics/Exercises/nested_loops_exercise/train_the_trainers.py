jury_members = int(input())
avarage_grades_for_all = 0.00
counter = 0.00
while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break
    counter += 1
    avarage_grade = 0
    for number in range(1, jury_members + 1):
        grade = float(input())
        avarage_grade += grade
    avarage_grade = avarage_grade / jury_members
    avarage_grades_for_all += avarage_grade
    print(f"{presentation_name} - {avarage_grade:.2f}.")

avarage_grades_for_all = avarage_grades_for_all / counter
print(f"Student's final assessment is {avarage_grades_for_all:.2f}." )