"""
Module defining the combat system.
"""
from saving_data import save_and_load_player as x
class Fight:
    def __init__(self, player, monster):
        """
        Initialize a new fight.

        Args:
            player (Player): The player character.
            monster (Monster): The monster character.
        """
        self.player = player
        self.monster = monster

    def start(self):
        """
        Start the fight.
        """
        try:
            while self.player.alive and self.monster.alive:
                self.player.attack(self.monster)
                if self.monster.alive:
                    self.monster.attack(self.player)
            if self.player.alive:
                print(f"{self.player.name} won the fight!")
                gold = self.monster.gold_reward()  
                self.player.gold += gold
                self.player._experience += self.monster.exp_reward()
                print(f"{self.player.name} received {gold} gold and experience {self.monster.exp_reward()}")
                x.save_player_to_json(self.player)
            else:
                print(f"{self.monster.name} won the fight!")
        except Exception as e:
            (print(f"Error {e}"))
