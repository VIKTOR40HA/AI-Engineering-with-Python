dollars_for_processor = float(input())
dollars_for_video_card = float(input())
dollars_for_ram = float(input())
ram_count = int(input())
discount = float(input())

total_in_dollars = ((dollars_for_processor) - (dollars_for_processor * discount) )+( (dollars_for_video_card) - (dollars_for_video_card * discount)) +(dollars_for_ram * ram_count)

total = (total_in_dollars * 1.57)
print(f"Money needed - {total:.2f} leva.")