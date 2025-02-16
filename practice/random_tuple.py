import random

class Dice:
    def roll(self):
        first = random.randint(0, 9)
        second = random.randint(0, 9)

        # return (first, second)
        return first, second
      

dice = Dice()
print(dice.roll())
    