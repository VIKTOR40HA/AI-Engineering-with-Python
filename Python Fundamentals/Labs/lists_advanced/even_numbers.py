
numbers_lst = list(map(int,input().split(", ")))

found_indices_or_no = map(
    lambda x: x if numbers_lst[x] % 2 == 0 else 'no',
    range(len(numbers_lst))
)
even_numbers = list(filter(lambda x: x !='no', found_indices_or_no))
print(even_numbers)