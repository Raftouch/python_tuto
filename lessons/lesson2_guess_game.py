# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess : '))
    guess_count += 1

    if guess == secret_number:
        print('You won!😀')
        # exit(0)
        break
else: 
    print('Sorry, you failed...😒')
