data = input().split()

command = input()

while command != "3:1":
    command_parts = command.split()
    action = command_parts[0]

    if action == "merge":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])

        start_index = max(0, start_index)
        end_index = min(len(data) - 1, end_index)

        if start_index <= end_index and start_index < len(data):
            merged_string = "".join(data[start_index:end_index + 1])

            data = (
                data[:start_index]
                + [merged_string]
                + data[end_index + 1:]
            )

    elif action == "divide":
        index = int(command_parts[1])
        partitions = int(command_parts[2])

        if partitions > 0:
            current_string = data[index]
            partition_length = len(current_string) // partitions

            divided_strings = []

            for partition_index in range(partitions - 1):
                start = partition_index * partition_length
                end = start + partition_length

                divided_strings.append(current_string[start:end])

            divided_strings.append(
                current_string[(partitions - 1) * partition_length:]
            )

            data = (
                data[:index]
                + divided_strings
                + data[index + 1:]
            )

    command = input()

print(" ".join(data))