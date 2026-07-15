import math
book_pages = int(input())
hour_read = int(input())
days_for_a_book = int(input())

hours_per_day_needed = (book_pages / hour_read) /days_for_a_book

print(hours_per_day_needed.__floor__())
