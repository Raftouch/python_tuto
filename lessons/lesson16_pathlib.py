from pathlib import Path

# path = Path('ecommerce')
# print(path.exists())

# path = Path('emails')
# print(path.mkdir())

# path = Path('emails')
# print(path.rmdir())

path = Path()
# print(path.glob('*.*'))
# print(path.glob('*.py'))
# print(path.glob('*.xls'))

# for file in path.glob('*.py'):
for file in path.glob('*'):
    print(file)