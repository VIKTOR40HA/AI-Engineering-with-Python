total_tickets = 0
student_tickets =0
standart_tickets = 0
kids_tickets = 0

while True:
    movie = input()
    if movie == 'Finish':
        break
    free_places = int(input())
    places_taken = 0

    while True:
        ticket = input()
        if ticket == 'End':
            break
        places_taken += 1
        total_tickets += 1

        if ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standart_tickets += 1
        elif ticket == 'kid':
            kids_tickets += 1

        if free_places <= places_taken:
            break
    print(f"{movie} - {((places_taken/free_places)*100):.2f}% full.")
print(f"Total tickets: {total_tickets}")
print(f"{((student_tickets/total_tickets)*100):.2f}% student tickets.")
print(f"{((standart_tickets/total_tickets)*100):.2f}% standard tickets.")
print(f"{((kids_tickets/total_tickets)*100):.2f}% kids tickets.")
