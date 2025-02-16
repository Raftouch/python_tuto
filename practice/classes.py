class Person:
    def __init__(self, name):
        self.name  = name
    def talk(self):
        print(f"Hi, I'm {self.name}") 

# first instance of Person class
person_one = Person('Bob')
person_one.talk()

# second instance of Person class
person_two = Person('John')
person_two.talk()
