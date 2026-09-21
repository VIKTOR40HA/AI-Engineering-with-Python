n= int(input())
the_best_snowball = 0
the_best_weight = 0
the_best_time = 0
the_best_quality = 0
for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_snowball = (weight//time)**quality
    if current_snowball >= the_best_snowball:
        the_best_snowball = current_snowball
        the_best_weight = weight
        the_best_time = time
        the_best_quality = quality
print(f"{the_best_weight} : {the_best_time} = {the_best_snowball} ({the_best_quality})")