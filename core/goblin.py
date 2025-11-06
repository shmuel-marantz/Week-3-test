import random

names = ['Tata', 'Vivi', 'Sisi']
weapons = ['sword', 'axe', 'knife']

class Goblin:

    def __init__(self):
        self.name = names[random.randint(0, 2)]
        self.type = 'goblin'
        self.hp = 20
        self.power = random.randint(5, 10)
        self.speed = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = weapons[random.randint(0, 2)]

    def speak(self):
        print(f'This is the {self.type} {self.name}')

    def attack(self):
        pass