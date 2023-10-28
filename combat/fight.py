class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start(self):
        while self.player.alive and self.monster.alive:
            self.player.attack(self.monster)
            if not self.monster.alive:
                experience_gained = self.monster.experience_reward
                print("You defeated the {0._name} and gained {1} experience!".format(self.monster, experience_gained))
                self.player.gain_experience(experience_gained)  # Award experience to the player
                break

            self.monster.attack(self.player)
            if not self.player.alive:
                print("The {0._name} defeated you...".format(self.monster))
                break
