file_path = input()

file_name = file_path.split("\\")[-1]
name, extension = file_name.rsplit(".", 1)

print(f"File name: {name}")
print(f"File extension: {extension}")