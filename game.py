import random

import core.player as pl
import core.orc as orc
import core.goblin as gb

monsters =[orc.Orc, gb.Goblin]

class Game:

    def show_menu(self):
        return input('Battle or Exit?')

    def create_player(self):
        player = pl.Player()
        return player

    def choose_random_monster(self):
        monster = monsters[random.randint(0, 1)]()
        return monster

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def start(self):
        if self.show_menu() != 'Battle':
            return
        else:
            player = self.create_player()
            monster = self.choose_random_monster()
            self.battle(player, monster)

    def battle(self, player, monster):
        sum_player = self.roll_dice(6) + player.speed
        sum_monster = self.roll_dice(6) + monster.speed
        if sum_player >= sum_monster:
            flag = 'player'
        else:
            flag = 'monster'








game = Game()
print(game.choose_random_monster().type)