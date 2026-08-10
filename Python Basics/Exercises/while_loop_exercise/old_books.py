old_book = input()
checked_books = 0
while(True):
    book_guess = input()
    if book_guess == old_book:
        print(f"You checked {checked_books} books and found it.")
        break
    elif book_guess == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    checked_books += 1