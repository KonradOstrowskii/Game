import random

class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start(self):
        while self.player.alive and self.monster.alive:
            self.player.attack(self.monster)
            if not self.monster.alive:
                print("You defeated the {0._name}!".format(self.monster))
                break

            self.monster.attack(self.player)
            if not self.player.alive:
                print("The {0._name} defeated you...".format(self.monster))
                break
