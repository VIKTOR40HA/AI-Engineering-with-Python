import math
attended_tournaments = int(input())
starting_points = int(input())

wins = 0
points = starting_points
for_avarage_points = 0
for _ in range(attended_tournaments):
    current_tournament_outcome = input()
    if current_tournament_outcome == "W":
        wins += 1
        points += 2000
        for_avarage_points += 2000
    elif current_tournament_outcome == "F":
        for_avarage_points += 1200
        points += 1200
    elif current_tournament_outcome == "SF":
        points += 720
        for_avarage_points += 720
avarage_points = for_avarage_points/ attended_tournaments
wins_percentage = wins / attended_tournaments * 100
print(f"Final points: {points}")
print(f"Average points: {math.floor(avarage_points)}")
print(f"{wins_percentage:.2f}%")