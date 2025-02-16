import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ['Bob', 'Ann', 'Lil', 'Kate']
leader = random.choice(members)
print(leader)