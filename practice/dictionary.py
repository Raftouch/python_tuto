phone = input('Phone : ')

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    # "9": "Nine",
}

output = ""

for character in phone:
    output += digits_mapping.get(character, "_") + " "

print(output)
