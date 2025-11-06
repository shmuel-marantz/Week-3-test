import random

names = ['Tata', 'Vivi', 'Sisi']
weapons = ['sword', 'axe', 'knife']

class Orc:

    def __init__(self):
        self.name = names[random.randint(0, 2)]
        self.type = 'orc'
        self.hp = 50
        self.power = random.randint(10, 15)
        self.speed = random.randint(0, 5)
        self.armor_rating = random.randint(2, 8)
        self.weapon = weapons[random.randint(0, 2)]

    def speak(self):
        print(f'This is the {self.type} {self.name}')

    def attack(self):
        pass


