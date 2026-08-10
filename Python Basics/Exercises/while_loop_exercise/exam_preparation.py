possible_bad_grades = int(input())
number_of_problems = 0
total_sum = 0
last_problem = ""
number_bad_grades = 0

while possible_bad_grades > number_bad_grades:
    command = input()
    if command == "Enough":
        avarage_grade = total_sum / number_of_problems
        print(f"Average score: {avarage_grade:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())

    if grade <=4:
        number_bad_grades += 1

    total_sum += grade
    number_of_problems += 1
    last_problem = command

else:
    print(f"You need a break, {possible_bad_grades} poor grades.")
