schedule = input().split(", ")

command = input()

while command != "course start":
    command_parts = command.split(":")
    action = command_parts[0]

    if action == "Add":
        lesson = command_parts[1]

        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        lesson = command_parts[1]
        index = int(command_parts[2])

        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif action == "Remove":
        lesson = command_parts[1]
        exercise = lesson + "-Exercise"

        if lesson in schedule:
            schedule.remove(lesson)

        if exercise in schedule:
            schedule.remove(exercise)

    elif action == "Swap":
        first_lesson = command_parts[1]
        second_lesson = command_parts[2]

        if first_lesson in schedule and second_lesson in schedule:
            first_index = schedule.index(first_lesson)
            second_index = schedule.index(second_lesson)

            schedule[first_index], schedule[second_index] = (
                schedule[second_index],
                schedule[first_index]
            )

            first_exercise = first_lesson + "-Exercise"
            second_exercise = second_lesson + "-Exercise"

            if first_exercise in schedule:
                schedule.remove(first_exercise)
                schedule.insert(
                    schedule.index(first_lesson) + 1,
                    first_exercise
                )

            if second_exercise in schedule:
                schedule.remove(second_exercise)
                schedule.insert(
                    schedule.index(second_lesson) + 1,
                    second_exercise
                )

    elif action == "Exercise":
        lesson = command_parts[1]
        exercise = lesson + "-Exercise"

        if lesson in schedule:
            lesson_index = schedule.index(lesson)

            if exercise not in schedule:
                schedule.insert(lesson_index + 1, exercise)

        else:
            schedule.append(lesson)
            schedule.append(exercise)

    command = input()

for index, lesson in enumerate(schedule, start=1):
    print(f"{index}.{lesson}")