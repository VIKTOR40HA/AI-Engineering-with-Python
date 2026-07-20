import math

series_name = input()
episode_lenght = int(input())
brake_lenght = int(input())

lunch_time = brake_lenght /8
rest_time = brake_lenght /4
brake = brake_lenght - lunch_time - rest_time - episode_lenght
if brake>=0:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(brake)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(abs(brake))} more minutes.")