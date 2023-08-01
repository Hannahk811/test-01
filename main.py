from pathlib import Path


def get_info():
    file_name = input("What is your file name? ")
    name = input("What is your name? ")
    address = input("What is your street address? ")
    number = input("What is your phone number? ")
    return file_name, name, address, number

file_name, name, adress, number = get_info()

path = Path(file_name)
path.write_text(f" {name},{adress},{number}")

content = path.read_text()

print(f"{file_name}:  ")
print(content)
