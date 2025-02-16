weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.lower() == 'l':
    converted = weight * 0.45
    print(f'you are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'you are {converted} pounds')
    