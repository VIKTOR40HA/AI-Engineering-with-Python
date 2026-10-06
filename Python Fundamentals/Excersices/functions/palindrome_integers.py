def isPalindrome(num_: int) -> bool:
    num_as_string = str(num_)

    if num_as_string == num_as_string[::-1]:
        return True
    else:
        return False


numbers_as_string = input().split(", ")
numbers = list(map(int, numbers_as_string))

for num in numbers:
    is_palindrome = isPalindrome(num)
    print(is_palindrome)