# numbers = [1, 2, 4, 6, 8, 7, 13, 5, 11]
# maximum = numbers[0]

# for number in numbers:
#     if number > maximum:
#         maximum = number
# print(maximum)

def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
# find_maximum(numbers)
