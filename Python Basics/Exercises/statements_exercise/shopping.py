video_card_price = 250

budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_total = video_card_price * video_cards_count
processor_price = video_cards_total * 0.35
ram_price = video_cards_total * 0.10
total_price =  video_cards_total + processor_price * processors_count + ram_price * ram_count
if video_cards_count > processors_count:
    total_price = total_price * 0.85

if total_price >budget:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
else:
    left_money = budget - total_price
    print(f"You have {left_money:.2f} leva left!")