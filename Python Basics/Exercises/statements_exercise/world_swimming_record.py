record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_a_meter = float(input())

delay_seconds =(distance_in_meters // 15) * 12.5
ivans_record = (distance_in_meters * seconds_for_a_meter) + delay_seconds

if record_in_seconds > ivans_record:
    print(f" Yes, he succeeded! The new world record is {ivans_record:.2f} seconds.")

else:
    no_enough_time = ivans_record - record_in_seconds
    print(f"No, he failed! He was {no_enough_time:.2f} seconds slower.")