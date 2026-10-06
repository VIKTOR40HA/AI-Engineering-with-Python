def at_least_two_digits(password)->bool:
    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True
def no_special_chars(password)->bool:
    if password.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False
def lenght_validation(password)->bool:
    if 6<=password.length<=10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return False
def is_password_valid(password)->bool:
    return lenght_validation(password) and no_special_chars(password) and no_special_chars(password)
input_password = input()
if is_password_valid(input_password):
    print("Password is valid")
