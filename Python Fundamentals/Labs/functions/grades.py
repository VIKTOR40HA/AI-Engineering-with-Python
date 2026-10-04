def print_grade(current_grade:float):
    if 2<=current_grade <=2.99:
        print("Fail")
    elif 3 <= current_grade <= 3.49:
        print("Poor")
    elif 3.50 <= current_grade <= 4.49:
        print("Good")
    elif 4.50 <= current_grade <= 5.49:
        print("Very Good")
    elif 5.50 <= current_grade <= 6.00:
        print("Excellent")
grade = float(input())

print_grade(grade)