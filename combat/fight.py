class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start(self):
        print("***** Fight Start! *****")
        print(f"{self.player.name} vs. {self.monster.name}")
        print(f"{self.player.name} - Level: {self.player._level}, Hit Points: {self.player._hit_points}")
        print(f"{self.monster.name} - Hit Points: {self.monster.hit_points}")
        print("*"*25)

        while self.player.alive and self.monster.alive:
            self.player.attack(self.monster)

            if not self.monster.alive:
                experience_gained = self.monster.experience_reward
                print(f"You defeated the {self.monster.name} and gained {experience_gained} experience!")
                self.player.gain_experience(experience_gained)
                break

            self.monster.attack(self.player)

            if not self.player.alive:
                print(f"The {self.monster.name} defeated {self.player.name}...")
                break
