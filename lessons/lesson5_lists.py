# Lists
# names = ['Raf', 'Bob', 'Lily', 'Kate', 'Mel']
# names[0] ='Rafa'
# print(names)

numbers = [5, 2, 1, 7, 4, 5, 4, 4, 2]
# numbers.append(14)
# numbers.insert(1, 11)
# numbers.remove(7)
# numbers.clear()
# numbers.pop()
# print(numbers.index(4))
# print(numbers.count(5)) # 2
numbers.sort()
numbers.reverse()
# numbers.copy()
print(numbers)
print(24 in numbers) # False

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)