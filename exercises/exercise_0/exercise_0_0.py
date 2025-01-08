from pathlib import Path

input_source = input("source directory: ")
input_destination = input("destination directory: ")

print(f"source: {input_source} {'*exist*' if Path(input_source).exists() else '*does not exist*'}")
print(f"destination: {input_destination} {'*exist*' if Path(input_destination).exists() else '*does not exist*'}")
