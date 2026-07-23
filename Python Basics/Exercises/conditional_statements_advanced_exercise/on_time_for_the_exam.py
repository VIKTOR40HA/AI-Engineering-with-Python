exam_hour = int(input())
exam_minutes = int(input())
arriaval_hour = int(input())
arraival_minutes = int(input())

exam_minutes = (exam_hour * 60) + exam_minutes
arriaval_minutes = (arriaval_hour * 60) + arraival_minutes

time_diff = exam_minutes - arriaval_minutes

if time_diff > 30:
    print("Early")
    pass
elif time_diff < 0:
    print("Late")
    pass
else:
    print("On Time")
    pass

hours = abs(time_diff) // 60
minutes = abs(time_diff) % 60

result = ""

if hours >0:
    result = f"{hours}:{minutes:02d} hours"
elif minutes >0:
    result = f"{minutes} minutes"
    pass

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"
print(result)
