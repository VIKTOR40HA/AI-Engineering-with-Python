def is_valid_lenght(current_username):
    if 3 <= len(current_username) <= 16:
        return True
    else:
        return False


def is_valid_correct_symobls(current_username):
    for symbol in current_username:
        if not (symbol.isalnum() or symbol == "-" or symbol == "_"):
            return False
    return True


def has_no_redunant_symobls(current_username):
    return True


def is_valid(current_username) -> bool:
    if (is_valid_lenght(current_username)
            and is_valid_correct_symobls(current_username)
            and has_no_redunant_symobls(current_username)):
        return True
    else:
        return False


usernames = input().split(", ")

for username in usernames:
    if is_valid(username):
        print(username)