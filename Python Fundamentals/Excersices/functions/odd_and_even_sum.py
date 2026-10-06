def calculate_odd_and_even_sum(given_number_as_string) -> str:
    even_sum = 0
    odd_sum = 0
    for number_ in given_number_as_string:
        if int(number_) % 2 == 0:
            even_sum += int(number_)
        else:
            odd_sum += int(number_)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()

print(calculate_odd_and_even_sum(number))