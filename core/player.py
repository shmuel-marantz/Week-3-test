import random

names = ['Zaza', 'Gogo', 'Dede']
professions = ['fighter', 'Healer']


class Player:

    def __init__(self):
        self.name = names[random.randint(0, 2)]
        self.profession = professions[random.randint(0, 1)]
        if self.profession == 'fighter':
            self.hp = 50
            self.power = random.randint(7, 12)
        else:
            self.hp = 60
            self.power = random.randint(5, 10)
        self.speed = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)

    def speak(self):
        print(self.name)

    def attack(self, monster):
        sum_battle = random.randint(1, 20) + self.speed
        if sum_battle <= monster.armor_rating:
            return None
        else:

