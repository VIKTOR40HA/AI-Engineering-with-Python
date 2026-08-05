student_name = input()
fails = 0
grade = 1
summ = 0
while True:
    new_grade = float(input())
    if new_grade < 4.00:
        fails += 1
        if fails >1:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue
    summ += new_grade
    if grade == 12:
        avg = summ/12
        print(f"{student_name} graduated. Average grade: {avg:.2f}")
        break
    grade += 1

